#!/bin/bash

if ! command -v python3 &>/dev/null || ! command -v pip3 &>/dev/null; then
    echo "Python3 and pip3 are required. Please install them first."
    exit 1
fi

VENV_DIR="venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

echo "Activating the virtual environment..."
source "$VENV_DIR/bin/activate"

echo "Installing required Python modules..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "Installed packages:"
pip3 list

echo "Virtual environment setup and dependencies installed successfully."

deactivate