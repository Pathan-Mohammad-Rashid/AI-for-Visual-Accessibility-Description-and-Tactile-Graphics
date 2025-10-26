"""
AI for Visual Accessibility - Tactile Graphics
Main Streamlit Web Application

Run with: streamlit run app.py
"""

import streamlit as st
import sys
from pathlib import Path
import numpy as np
from PIL import Image
import io
import json

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

# Import configurations and modules
from config import UI_CONFIG, TACTILE_CONFIG, IMAGE_CONFIG, VLM_CONFIG
from src.tactile_converter import TactileImageConverter

# Page Configuration
st.set_page_config(
    page_title=UI_CONFIG["page_title"],
    page_icon=UI_CONFIG["page_icon"],
    layout=UI_CONFIG["layout"]
)

# Custom CSS
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    font-weight: bold;
}
.tactile-point-on {
    display: inline-block;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #4CAF50;
    margin: 2px;
}
.tactile-point-off {
    display: inline-block;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #ddd;
    border: 1px solid #999;
    margin: 2px;
}
</style>
""", unsafe_allow_html=True)

# Title and Description
st.title("👁️ AI for Visual Accessibility")
st.markdown("### Transform Images into Tactile Graphics")
st.markdown("""
This tool converts visual images into tactile patterns for visually impaired users 
using **3mm magnetic balls** and **AI-enhanced processing**.
""")

# Sidebar Configuration
st.sidebar.header("⚙️ Configuration")

# Grid Size Selection
st.sidebar.subheader("Grid Size")
grid_size = st.sidebar.selectbox(
    "Select grid resolution:",
    options=TACTILE_CONFIG["grid_sizes"],
    index=TACTILE_CONFIG["grid_sizes"].index(TACTILE_CONFIG["default_grid_size"]),
    help="Higher resolution = more detail but more complex hardware"
)

# Display specifications
st.sidebar.info(f"""
**{grid_size}×{grid_size} Specifications:**
- Total points: {grid_size*grid_size}
- Size: {grid_size*3.5:.1f}mm × {grid_size*3.5:.1f}mm
- Weight: ~{grid_size*grid_size*0.11:.1f}g
""")

# Processing Method
st.sidebar.subheader("Image Processing")
processing_method = st.sidebar.selectbox(
    "Processing method:",
    options=IMAGE_CONFIG["processing_methods"],
    index=IMAGE_CONFIG["processing_methods"].index(IMAGE_CONFIG["default_method"]),
    help="Different methods work better for different image types"
)

# Invert option
invert_pattern = st.sidebar.checkbox("Invert pattern", value=False)

# VLM Settings
st.sidebar.subheader("🤖 AI Enhancement")
use_vlm = st.sidebar.checkbox(
    "Use Vision-Language Model", 
    value=False,
    help="Requires API key or GPU. Provides intelligent object extraction."
)

if use_vlm:
    vlm_backend = st.sidebar.selectbox(
        "VLM Backend:",
        options=["None (Traditional CV)", "OpenAI GPT-4V", "Hugging Face (Local)"],
        index=0
    )
    
    if vlm_backend == "OpenAI GPT-4V":
        api_key = st.sidebar.text_input("OpenAI API Key:", type="password")
        if api_key:
            st.sidebar.success("✓ API Key provided")
else:
    vlm_backend = "None (Traditional CV)"

# Export Format
st.sidebar.subheader("📁 Export Format")
export_format = st.sidebar.selectbox(
    "Hardware file format:",
    options=["arduino", "txt", "json", "csv"],
    index=0
)

# Main Content
col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=IMAGE_CONFIG["supported_formats"],
        help="Upload any image to convert to tactile format"
    )
    
    if uploaded_file is not None:
        # Display original image
        image = Image.open(uploaded_file)
        # st.image(image, caption="Original Image", use_column_width=True)
        st.image(image, caption="Original Image", use_container_width=True)
        
        # Image info
        st.info(f"Size: {image.size[0]}×{image.size[1]} pixels | Mode: {image.mode}")

with col2:
    st.subheader("👆 Tactile Pattern Preview")
    
    if uploaded_file is not None:
        # Automatically process image if any relevant option changes or new file is uploaded
        process_needed = False
        # Check if any relevant parameter or file has changed
        if (
            'last_uploaded_file' not in st.session_state or
            st.session_state.get('last_uploaded_file') != uploaded_file or
            st.session_state.get('last_grid_size') != grid_size or
            st.session_state.get('last_processing_method') != processing_method or
            st.session_state.get('last_invert_pattern') != invert_pattern or
            st.session_state.get('last_use_vlm') != use_vlm or
            st.session_state.get('last_vlm_backend') != vlm_backend
        ):
            process_needed = True

        if process_needed:
            with st.spinner("Processing image..."):
                # Initialize converter
                converter = TactileImageConverter(
                    grid_size=grid_size,
                    use_vlm=use_vlm
                )
                
                # VLM description (placeholder)
                vlm_description = None
                if use_vlm and vlm_backend != "None (Traditional CV)":
                    st.info("🤖 AI Analysis: Analyzing image with Vision-Language Model...")
                    # TODO: Add actual VLM integration
                    vlm_description = "This image contains shapes and objects."
                
                # Process image
                matrix = converter.process_image(
                    image,
                    method=processing_method.lower(),
                    invert=invert_pattern,
                    vlm_description=vlm_description
                )
                
                # Store in session state
                st.session_state['matrix'] = matrix
                st.session_state['converter'] = converter
                st.session_state['processed'] = True
                st.session_state['last_uploaded_file'] = uploaded_file
                st.session_state['last_grid_size'] = grid_size
                st.session_state['last_processing_method'] = processing_method
                st.session_state['last_invert_pattern'] = invert_pattern
                st.session_state['last_use_vlm'] = use_vlm
                st.session_state['last_vlm_backend'] = vlm_backend
                st.success("✓ Conversion complete!")

    # Display results if processed
    if 'processed' in st.session_state and st.session_state['processed']:
        matrix = st.session_state['matrix']
        converter = st.session_state['converter']
        
        # Visual representation
        st.markdown("**Pattern Visualization:**")
        
        # Create visual grid
        rows, cols = matrix.shape
        html_grid = "<div style='background:#f0f0f0; padding:10px; border-radius:5px;'>"
        for i in range(rows):
            html_grid += "<div>"
            for j in range(cols):
                if matrix[i][j] == 1:
                    html_grid += "<span class='tactile-point-on' title='Raised'></span>"
                else:
                    html_grid += "<span class='tactile-point-off' title='Lowered'></span>"
            html_grid += "</div>"
        html_grid += "</div>"
        
        st.markdown(html_grid, unsafe_allow_html=True)
        
        # Text representation
        with st.expander("📝 Text Representation"):
            pattern_text = converter.visualize_pattern(matrix, style='unicode')
            st.text(pattern_text)
        
        # Statistics
        stats = converter.get_statistics(matrix)
        st.markdown("**Statistics:**")
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Points Raised", f"{stats['points_raised']}/{stats['total_points']}")
        with col_b:
            st.metric("Coverage", f"{stats['coverage_percent']}%")
        with col_c:
            st.metric("Size", f"{stats['display_width_mm']}mm")
        
        # Download section
        st.markdown("---")
        st.subheader("💾 Download Hardware Files")
        
        # Generate hardware file
        output_buffer = io.StringIO()
        
        if export_format == 'txt':
            for row in matrix:
                output_buffer.write(''.join(map(str, row)) + '\\n')
            file_content = output_buffer.getvalue()
            file_name = f"tactile_pattern_{grid_size}x{grid_size}.txt"
            mime_type = "text/plain"
            
        elif export_format == 'arduino':
            rows, cols = matrix.shape
            output_buffer.write(f"// Tactile Display - {rows}×{cols}\\n")
            output_buffer.write(f"const int ROWS = {rows};\\n")
            output_buffer.write(f"const int COLS = {cols};\\n\\n")
            output_buffer.write(f"const int pattern[ROWS][COLS] = {{\\n")
            for i, row in enumerate(matrix):
                row_str = '  {' + ', '.join(map(str, row)) + '}'
                if i < len(matrix) - 1:
                    row_str += ','
                output_buffer.write(row_str + '\\n')
            output_buffer.write("};\\n")
            file_content = output_buffer.getvalue()
            file_name = f"tactile_pattern_{grid_size}x{grid_size}.ino"
            mime_type = "text/plain"
            
        elif export_format == 'json':
            data = {
                'grid_size': {'rows': int(rows), 'cols': int(cols)},
                'pattern': matrix.tolist(),
                'statistics': stats
            }
            file_content = json.dumps(data, indent=2)
            file_name = f"tactile_pattern_{grid_size}x{grid_size}.json"
            mime_type = "application/json"
            
        elif export_format == 'csv':
            for row in matrix:
                output_buffer.write(','.join(map(str, row)) + '\\n')
            file_content = output_buffer.getvalue()
            file_name = f"tactile_pattern_{grid_size}x{grid_size}.csv"
            mime_type = "text/csv"
        
        # Download button
        st.download_button(
            label=f"⬇️ Download {export_format.upper()} File",
            data=file_content,
            file_name=file_name,
            mime=mime_type,
            type="primary"
        )
        
        # Additional info
        with st.expander("ℹ️ Hardware Implementation Guide"):
            st.markdown(f"""
            ### Using this {grid_size}×{grid_size} Pattern
            
            **Hardware Requirements:**
            - {grid_size*grid_size} × 3mm magnetic/steel balls
            - {grid_size*grid_size} × Electromagnets or solenoids
            - Microcontroller (Arduino Mega/ESP32)
            - Power supply (12V, ~2-5A)
            - Driver circuits (MOSFETs/H-bridges)
            
            **Physical Display:**
            - Size: {stats['display_width_mm']}mm × {stats['display_height_mm']}mm
            - Weight: ~{stats['display_weight_g']}g
            - Ball spacing: 3.5mm center-to-center
            
            **Next Steps:**
            1. Download the hardware file
            2. Upload to your microcontroller
            3. Connect electromagnets/solenoids
            4. Test pattern display
            5. Iterate and refine
            """)

# Information section
st.markdown("---")
st.header("📚 About This Project")

tab1, tab2, tab3 = st.tabs(["Overview", "How It Works", "Technical Details"])

with tab1:
    st.markdown("""
    ### AI for Visual Accessibility - Tactile Graphics
    
    This project converts visual images into tactile representations that can be felt 
    by visually impaired users. Using **3mm magnetic balls** controlled by electromagnets,
    we create dynamic, refreshable tactile displays.
    
    **Key Features:**
    - 🤖 AI-enhanced image processing (optional VLM support)
    - 📐 Variable resolution (4×4 to 32×32)
    - 💾 Multiple hardware export formats
    - 🎨 Real-time pattern preview
    - 📊 Detailed statistics and specifications
    """)

with tab2:
    st.markdown("""
    ### Processing Pipeline
    
    1. **Image Upload** - Upload any image (photo, drawing, icon)
    2. **AI Analysis** (Optional) - Vision-Language Model analyzes image content
    3. **Simplification** - Convert to binary (black/white) using edge detection or thresholding
    4. **Grid Mapping** - Downsample to selected grid size (4×4, 8×8, 16×16, 32×32)
    5. **Pattern Generation** - Create tactile pattern (1=raised, 0=lowered)
    6. **Export** - Generate hardware files for microcontroller
    
    **Image Processing Methods:**
    - **Edge**: Detects outlines and contours
    - **Threshold**: Simple black/white conversion
    - **High Contrast**: Enhanced contrast then threshold
    - **Adaptive**: Smart local thresholding
    """)

with tab3:
    st.markdown(f"""
    ### Technical Specifications
    
    **Tactile Display:**
    - Ball diameter: {TACTILE_CONFIG['ball_diameter_mm']}mm
    - Ball spacing: {TACTILE_CONFIG['ball_spacing_mm']}mm center-to-center
    - Ball material: Steel/ferromagnetic
    - Ball weight: {TACTILE_CONFIG['ball_weight_g']}g each
    
    **Grid Sizes Available:**
    {', '.join([f"{s}×{s}" for s in TACTILE_CONFIG['grid_sizes']])}
    
    **Supported Image Formats:**
    {', '.join(IMAGE_CONFIG['supported_formats'])}
    
    **Export Formats:**
    - **Arduino (.ino)**: Direct upload to Arduino/ESP32
    - **Text (.txt)**: Human-readable pattern
    - **JSON (.json)**: Structured data with metadata
    - **CSV (.csv)**: Spreadsheet-compatible
    
    **VLM Options:**
    - OpenAI GPT-4 Vision (API)
    - Hugging Face open-source models
    - Traditional computer vision (no AI)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>AI for Visual Accessibility Project</strong> | Session 1 Implementation</p>
    <p>Using 3mm Magnetic Balls | Powered by Python, Streamlit, and AI</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'processed' not in st.session_state:
    st.session_state['processed'] = False