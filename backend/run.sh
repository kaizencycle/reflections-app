#!/bin/bash

# Lab7 OAA Backend Startup Script

echo "Starting Lab7 - Open Attestation Authority Backend..."
echo "Version: 1.0.1"
echo ""

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/upgrade dependencies
echo "Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Start the server
echo ""
echo "Starting FastAPI server on http://0.0.0.0:8000"
echo "Documentation available at http://0.0.0.0:8000/docs"
echo ""

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000