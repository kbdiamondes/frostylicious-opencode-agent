#!/bin/bash

# Navigate to the project directory
cd ~/Documents/Programming/frostylicious-opencode-agent/api-key-rotator

# Activate the virtual environment
# Assumes your venv folder is named 'venv'
source venv/bin/activate

# Execute the script
python3 rotator.py
