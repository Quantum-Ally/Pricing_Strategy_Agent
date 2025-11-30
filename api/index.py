"""
Vercel serverless function entry point for FastAPI app
"""
import sys
from pathlib import Path

# Add parent directory to path so we can import src
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.main import app

# Vercel will automatically detect and serve the FastAPI app

