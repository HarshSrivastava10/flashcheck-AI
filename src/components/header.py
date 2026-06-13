import streamlit as st
import base64
import os

def get_image_base64():
    """Dynamically resolves the absolute path to the main-logo image."""
    try:
        # Finds the path of header.py, moves 2 levels up to root, then enters images/
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
        file_path = os.path.join(root_dir, "static/images", "main-logo.png")
        
        with open(file_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            return f"data:image/png;base64,{encoded}"
    except Exception as e:
        # Returns the error as text so you can debug in the browser if it fails
        return f"Error loading image: {str(e)}"

def header_home():
    logo_data_url = get_image_base64()
    
    # If a file error happened, display it for debugging
    if logo_data_url.startswith("Error"):
        st.error(logo_data_url)
        return

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;">
            <img src="{logo_data_url}" alt="InstaAttendance Logo" style="height:100px;">
            <h1 style="text-align:center; color:#E0E3FF;">Insta<br/>ATTENDANCE</h1>
        </div>
    """, unsafe_allow_html=True)
