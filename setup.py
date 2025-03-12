# setup.py
from setuptools import setup, find_packages

setup(
    name="youtube-fabric-gui",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fabric>=2.6.0",
        "streamlit>=1.10.0",
        "PyYAML>=6.0",
        "pillow>=9.0.0",
    ],
    python_requires=">=3.7",
)