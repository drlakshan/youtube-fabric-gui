# fabric_app.py
import streamlit as st
import subprocess
import re
import os
import glob
import shutil

def check_dependencies():
    """Check if required dependencies are available."""
    # Check if fabric command is available
    fabric_available = shutil.which("fabric") is not None
    
    if not fabric_available:
        st.error("""
        The 'fabric' command was not found in your PATH.
        
        Please make sure:
        1. You have installed Fabric AI
        2. Your virtual environment is activated (if you're using one)
        3. The fabric command is available in your PATH
        
        You can install Fabric AI with: `pip install fabric-ai`
        """)
        return False
    return True

def get_available_patterns():
    """Get list of available Fabric AI patterns from the patterns directory."""
    # Use the local patterns-for-gui folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    patterns_dir = os.path.join(current_dir, "patterns-for-gui")
    
    # Get pattern folders
    try:
        if not os.path.exists(patterns_dir):
            st.warning(f"Patterns directory not found: {patterns_dir}")
            return []
        
        # Get all subdirectories in the patterns-for-gui folder
        pattern_folders = [d for d in os.listdir(patterns_dir) 
                          if os.path.isdir(os.path.join(patterns_dir, d))]
        
        # Filter to only include folders that contain system.md or user.md
        valid_patterns = []
        for folder in pattern_folders:
            folder_path = os.path.join(patterns_dir, folder)
            if (os.path.exists(os.path.join(folder_path, "system.md")) or 
                os.path.exists(os.path.join(folder_path, "user.md"))):
                valid_patterns.append(folder)
        
        valid_patterns.sort()  # Sort alphabetically for better UI
        
        if not valid_patterns:
            st.warning(f"No valid pattern folders found in {patterns_dir}")
        
        return valid_patterns
    except Exception as e:
        st.error(f"Error loading patterns: {str(e)}")
        return []