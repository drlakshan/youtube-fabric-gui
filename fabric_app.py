import streamlit as st
import subprocess
import os
import shutil

def extract_video_id(url):
    """Extract YouTube video ID from URL."""
    # Regular expressions to match various YouTube URL formats
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu.be\/|youtube.com\/embed\/)([^&\n?#]+)',
        r'youtube.com\/shorts\/([^&\n?#]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_youtube_transcript(video_id):
    """Get transcript from YouTube video."""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        # Combine all transcript pieces into a single text
        full_transcript = ""
        for entry in transcript_list:
            full_transcript += entry['text'] + " "
        return full_transcript.strip()
    except Exception as e:
        st.error(f"Error getting transcript: {str(e)}")
        return None

def check_dependencies():
    """Check if required dependencies are available."""
    # Check if fabric command is available
    fabric_available = shutil.which("fabric") is not None
    
    if not fabric_available:
        st.error("""
        The 'fabric' command was not found in your PATH.
        
        To install Fabric AI on MacOS:
        1. Install Homebrew if you haven't already:
           /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        
        2. Install Fabric AI using Homebrew:
           brew install fabric-ai
        
        3. Make sure your PATH includes the Homebrew binary location
        
        After installation, restart your terminal and try running the app again.
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

def run_fabric_pattern(pattern_name, youtube_url):
    """Run a Fabric AI pattern on the YouTube URL."""
    try:
        # First get the transcript using fabric -y
        cmd_transcript = f'fabric -y "{youtube_url}"'
        transcript_result = subprocess.run(cmd_transcript, shell=True, capture_output=True, text=True)
        
        if transcript_result.returncode != 0:
            st.error(f"Error getting YouTube transcript: {transcript_result.stderr}")
            return None
            
        # Now pipe the transcript through the selected pattern
        cmd_pattern = f'echo "{transcript_result.stdout}" | fabric -p {pattern_name}'
        pattern_result = subprocess.run(cmd_pattern, shell=True, capture_output=True, text=True)
        
        if pattern_result.returncode != 0:
            st.error(f"Error running fabric pattern: {pattern_result.stderr}")
            return None
            
        return pattern_result.stdout
    except Exception as e:
        st.error(f"Error running fabric pattern: {str(e)}")
        return None