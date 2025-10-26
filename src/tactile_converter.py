"""
Tactile Image Converter with VLM Support
Converts images to tactile display patterns using AI-enhanced processing
"""

import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import json
from typing import Tuple, Optional, Dict
import sys
sys.path.append('..')
from config import TACTILE_CONFIG

class TactileImageConverter:
    """
    Convert images to tactile display format with optional VLM enhancement
    Using 3mm magnetic balls as tactile points
    """
    
    def __init__(self, grid_size: Tuple[int, int] | int = 4, use_vlm: bool = False):
        """
        Initialize converter with grid size and VLM option
        
        Args:
            grid_size: tuple (rows, cols) or single int for square grid
            use_vlm: Whether to use Vision-Language Model for enhancement
        """
        if isinstance(grid_size, int):
            self.grid_size = (grid_size, grid_size)
        else:
            self.grid_size = grid_size
        
        self.use_vlm = use_vlm
        self.ball_diameter = TACTILE_CONFIG["ball_diameter_mm"]
        self.ball_spacing = TACTILE_CONFIG["ball_spacing_mm"]
        
        print(f"✓ Tactile Converter Initialized: {self.grid_size[0]}×{self.grid_size[1]}")
        if use_vlm:
            print("✓ VLM Enhancement: ENABLED")
    
    def load_image(self, image_path: str) -> Image.Image:
        """Load image from file or PIL Image object"""
        if isinstance(image_path, str):
            return Image.open(image_path)
        elif isinstance(image_path, Image.Image):
            return image_path
        else:
            raise ValueError("Input must be file path or PIL Image")
    
    def preprocess_with_vlm(self, image: Image.Image, vlm_description: Optional[str] = None) -> Image.Image:
        """
        Use VLM description to guide image preprocessing
        
        Args:
            image: Input PIL Image
            vlm_description: Optional VLM description of image
        
        Returns:
            Enhanced PIL Image focused on important features
        """
        # If VLM description mentions specific objects, we could:
        # 1. Focus on those regions
        # 2. Enhance their edges
        # 3. Reduce background noise
        
        # For now, apply enhanced preprocessing
        # (Full VLM integration will be in vlm_handler.py)
        
        if vlm_description:
            print(f"📝 VLM Insight: {vlm_description[:100]}...")
        
        # Enhance contrast for better edge detection
        enhancer = ImageEnhance.Contrast(image.convert('L'))
        enhanced = enhancer.enhance(2.0)
        
        return enhanced
    
    # def preprocess_image(self, image: Image.Image, method: str = 'threshold', 
    #                     vlm_description: Optional[str] = None) -> Image.Image:
    #     """
    #     Convert image to 2-color (binary) format
        
    #     Args:
    #         image: PIL Image
    #         method: 'edge', 'threshold', 'high_contrast', or 'adaptive'
    #         vlm_description: Optional VLM description for guidance
        
    #     Returns:
    #         Binary PIL Image (mode '1')
    #     """
    #     # Apply VLM-guided preprocessing if available
    #     if vlm_description and self.use_vlm:
    #         image = self.preprocess_with_vlm(image, vlm_description)
        
    #     # Convert to grayscale
    #     if image.mode != 'L':
    #         gray = image.convert('L')
    #     else:
    #         gray = image
        
    #     if method == 'edge':
    #         # Edge detection
    #         edges = gray.filter(ImageFilter.FIND_EDGES)
    #         threshold = 30
    #         binary = edges.point(lambda x: 255 if x > threshold else 0, mode='1')
            
    #     elif method == 'threshold':
    #         # Simple binary threshold
    #         threshold = 127
    #         binary = gray.point(lambda x: 255 if x > threshold else 0, mode='1')
            
    #     elif method == 'high_contrast':
    #         # Enhanced contrast then threshold
    #         enhancer = ImageEnhance.Contrast(gray)
    #         enhanced = enhancer.enhance(2.5)
    #         binary = enhanced.point(lambda x: 255 if x > 127 else 0, mode='1')
            
    #     elif method == 'adaptive':
    #         # Adaptive thresholding (pseudo-implementation using PIL)
    #         # Convert to numpy for more advanced processing
    #         import cv2
    #         gray_np = np.array(gray)
    #         binary_np = cv2.adaptiveThreshold(
    #             gray_np, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    #             cv2.THRESH_BINARY, 11, 2
    #         )
    #         binary = Image.fromarray(binary_np).convert('1')
        
    #     else:
    #         # Default: simple threshold
    #         binary = gray.point(lambda x: 255 if x > 127 else 0, mode='1')
        
    #     return binary
    
    def preprocess_image(self, image: Image.Image, method: str = 'threshold', 
                        vlm_description: Optional[str] = None) -> Image.Image:
        """Convert image to 2-color (binary) format - FIXED VERSION"""
        
        # Apply VLM-guided preprocessing if available
        if vlm_description and self.use_vlm:
            image = self.preprocess_with_vlm(image, vlm_description)
        
        # Convert to grayscale
        if image.mode != 'L':
            gray = image.convert('L')
        else:
            gray = image
        
        if method == 'edge':
            # FIXED: Better edge detection
            enhancer = ImageEnhance.Contrast(gray)
            enhanced = enhancer.enhance(2.0)
            edges = enhanced.filter(ImageFilter.FIND_EDGES)
            threshold = 20  # More sensitive
            binary = edges.point(lambda x: 255 if x > threshold else 0, mode='1')
            
        elif method == 'threshold':
            # FIXED: Invert for colored shapes on white background
            threshold = 200
            binary = gray.point(lambda x: 255 if x < threshold else 0, mode='1')
            
        elif method == 'high_contrast':
            enhancer = ImageEnhance.Contrast(gray)
            enhanced = enhancer.enhance(2.5)
            binary = enhanced.point(lambda x: 255 if x < 200 else 0, mode='1')
            
        elif method == 'adaptive':
            try:
                import cv2
                gray_np = np.array(gray)
                binary_np = cv2.adaptiveThreshold(
                    gray_np, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                    cv2.THRESH_BINARY_INV, 11, 2
                )
                binary = Image.fromarray(binary_np).convert('1')
            except ImportError:
                binary = gray.point(lambda x: 255 if x < 200 else 0, mode='1')
        
        else:
            binary = gray.point(lambda x: 255 if x < 200 else 0, mode='1')
        
        return binary

    
    def convert_to_grid(self, binary_image: Image.Image, invert: bool = False) -> np.ndarray:
        """
        Convert binary image to grid matrix
        
        Args:
            binary_image: Binary PIL Image
            invert: Flip 0s and 1s
        
        Returns:
            numpy array of 0s and 1s (1 = raised point)
        """
        rows, cols = self.grid_size

        # Ensure image is in grayscale for consistent numpy conversion
        if binary_image.mode != 'L':
            img_gray = binary_image.convert('L')
        else:
            img_gray = binary_image

        # Resize image to grid size
        resized = img_gray.resize((cols, rows), Image.Resampling.LANCZOS)

        # Convert to numpy array
        arr = np.array(resized)

        # Convert to binary matrix (0 or 1)
        matrix = (arr < 128).astype(int)  # 1 for dark (raised), 0 for light (lowered)

        if invert:
            matrix = 1 - matrix

        return matrix
    
    def visualize_pattern(self, matrix: np.ndarray, style: str = 'unicode') -> str:
        """
        Create text visualization of tactile pattern
        
        Args:
            matrix: Binary matrix
            style: 'unicode', 'ascii', or 'emoji'
        
        Returns:
            String representation
        """
        if style == 'unicode':
            on_char, off_char = '●', '○'
        elif style == 'ascii':
            on_char, off_char = '#', '.'
        elif style == 'emoji':
            on_char, off_char = '🔵', '⚪'
        else:
            on_char, off_char = '1', '0'
        
        lines = []
        for i, row in enumerate(matrix):
            line = f"Row {i+1:2d}: " + " ".join([on_char if x else off_char for x in row])
            lines.append(line)
        
        return "\n".join(lines)
    
    def get_statistics(self, matrix: np.ndarray) -> Dict:
        """Calculate statistics about tactile pattern"""
        rows, cols = matrix.shape
        total = rows * cols
        raised = int(np.sum(matrix))
        lowered = total - raised
        coverage = (raised / total) * 100
        
        # Physical dimensions
        width = cols * self.ball_spacing
        height = rows * self.ball_spacing
        weight = total * TACTILE_CONFIG["ball_weight_g"]
        
        return {
            "grid_size": f"{rows}×{cols}",
            "total_points": total,
            "points_raised": raised,
            "points_lowered": lowered,
            "coverage_percent": round(coverage, 1),
            "display_width_mm": round(width, 1),
            "display_height_mm": round(height, 1),
            "display_weight_g": round(weight, 1),
        }
    
    def generate_hardware_file(self, matrix: np.ndarray, output_path: str, 
                              file_format: str = 'txt') -> str:
        """
        Generate hardware-compatible file
        
        Args:
            matrix: numpy array
            output_path: file path to save
            file_format: 'txt', 'csv', 'json', or 'arduino'
        
        Returns:
            Path to generated file
        """
        rows, cols = matrix.shape
        
        if file_format == 'txt':
            with open(output_path, 'w') as f:
                f.write(f"# Tactile Display Pattern\\n")
                f.write(f"# Grid: {rows}×{cols}\\n")
                f.write(f"# Ball: {self.ball_diameter}mm, Spacing: {self.ball_spacing}mm\\n")
                f.write(f"# 0=down, 1=up\\n\\n")
                for row in matrix:
                    f.write(''.join(map(str, row)) + '\\n')
                    
        elif file_format == 'arduino':
            with open(output_path, 'w') as f:
                f.write(f"// Tactile Display Pattern - {rows}×{cols}\\n")
                f.write(f"// {self.ball_diameter}mm balls, {self.ball_spacing}mm spacing\\n")
                f.write(f"// Generated by AI Visual Accessibility System\\n\\n")
                f.write(f"const int ROWS = {rows};\\n")
                f.write(f"const int COLS = {cols};\\n\\n")
                f.write(f"const int tactilePattern[ROWS][COLS] = {{\\n")
                for i, row in enumerate(matrix):
                    row_str = '  {' + ', '.join(map(str, row)) + '}'
                    if i < len(matrix) - 1:
                        row_str += ','
                    f.write(row_str + '\\n')
                f.write("};\\n\\n")
                f.write("// Usage: if (tactilePattern[row][col] == 1) raiseBall(row, col);\\n")
                
        elif file_format == 'json':
            data = {
                'metadata': {
                    'grid_size': {'rows': int(rows), 'cols': int(cols)},
                    'ball_diameter_mm': self.ball_diameter,
                    'ball_spacing_mm': self.ball_spacing,
                    'total_points': int(rows * cols),
                    'points_raised': int(np.sum(matrix)),
                },
                'pattern': matrix.tolist()
            }
            with open(output_path, 'w') as f:
                json.dump(data, f, indent=2)
                
        elif file_format == 'csv':
            with open(output_path, 'w') as f:
                f.write(f"# Grid Size: {rows}×{cols}\\n")
                f.write(f"# Ball Specs: {self.ball_diameter}mm diameter, {self.ball_spacing}mm spacing\\n")
                for row in matrix:
                    f.write(','.join(map(str, row)) + '\\n')
        
        return output_path
    
    def process_image(self, image_input, method: str = 'threshold', 
                     invert: bool = False, vlm_description: Optional[str] = None) -> np.ndarray:
        """
        Complete pipeline: load → preprocess → convert
        
        Args:
            image_input: path to image file or PIL Image
            method: preprocessing method
            invert: invert the pattern
            vlm_description: optional VLM description
        
        Returns:
            numpy array (binary matrix)
        """
        img = self.load_image(image_input)
        binary = self.preprocess_image(img, method=method, vlm_description=vlm_description)
        matrix = self.convert_to_grid(binary, invert=invert)
        return matrix