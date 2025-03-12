# YouTube Fabric AI Analysis

A Streamlit application that analyzes YouTube video transcripts using Fabric AI patterns. This tool allows you to apply various Fabric AI analysis patterns to YouTube video content.

## Features

- Extract transcripts from YouTube videos
- Apply any Fabric AI pattern to analyze the content
- User-friendly web interface built with Streamlit
- Support for all available Fabric AI patterns
- Real-time analysis results

## Prerequisites

- MacOS (Homebrew required for Fabric AI installation)
- Python 3.7+
- Fabric AI installed via Homebrew
- pip (Python package manager)

## Installation

1. Install Homebrew (if not already installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install Fabric AI using Homebrew:
```bash
brew install fabric-ai
```

3. Clone this repository:
```bash
git clone https://github.com/yourusername/youtube-fabric-analysis.git
cd youtube-fabric-analysis
```

4. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run streamlit_app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Enter a YouTube URL in the input field

4. Select a Fabric AI pattern from the dropdown menu

5. Click "Analyze Video" to process the content

6. View the transcript and analysis results

## Project Structure

- `streamlit_app.py`: Main Streamlit application interface
- `fabric_app.py`: Core functionality for Fabric AI integration
- `requirements.txt`: Python package dependencies
- `patterns-for-gui/`: Directory containing Fabric AI patterns

## Supported Patterns

The application supports all Fabric AI patterns available in your patterns-for-gui directory. Some examples include:
- extract_wisdom
- analyze_claims
- create_summary
- And many more...

## Troubleshooting

If you encounter any issues:

1. Ensure Fabric AI is properly installed:
```bash
fabric --version
```

2. Check that your Python environment has all required packages:
```bash
pip list
```

3. Verify that the YouTube video has available transcripts/subtitles

4. Make sure your internet connection is active

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.