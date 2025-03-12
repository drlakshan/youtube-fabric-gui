import streamlit as st
import subprocess
from fabric_app import (
    check_dependencies,
    get_available_patterns,
    run_fabric_pattern
)

def main():
    st.title("YouTube Fabric AI Analysis")
    st.write("Analyze YouTube video transcripts using Fabric AI patterns")
    
    # Check if fabric is installed and available
    if not check_dependencies():
        st.stop()
    
    # Get available patterns
    patterns = get_available_patterns()
    if not patterns:
        st.error("No Fabric AI patterns found. Please check your patterns-for-gui directory.")
        st.stop()
    
    # YouTube URL input
    youtube_url = st.text_input("Enter YouTube URL:", 
                               help="Enter the URL of the YouTube video you want to analyze")
    
    # Pattern selection
    selected_pattern = st.selectbox(
        "Select Fabric AI Pattern:",
        patterns,
        help="Choose the Fabric AI pattern to apply to the transcript"
    )
    
    if st.button("Analyze Video"):
        if not youtube_url:
            st.error("Please enter a YouTube URL")
            return
            
        # First get transcript and show it
        with st.spinner("Getting video transcript..."):
            cmd_transcript = f'fabric -y "{youtube_url}"'
            transcript_result = subprocess.run(cmd_transcript, shell=True, capture_output=True, text=True)
            
            if transcript_result.returncode != 0:
                st.error(f"Error getting YouTube transcript: {transcript_result.stderr}")
                return
                
            # Show transcript
            with st.expander("Video Transcript"):
                st.text_area("Transcript", transcript_result.stdout, height=200)
            
        # Run fabric pattern
        with st.spinner(f"Analyzing video with pattern '{selected_pattern}'..."):
            result = run_fabric_pattern(selected_pattern, youtube_url)
            
            if result:
                st.success("Analysis complete!")
                st.markdown("### Analysis Result")
                st.markdown(result)
            else:
                st.error("Failed to analyze video. Please check the error messages above.")

if __name__ == "__main__":
    main()