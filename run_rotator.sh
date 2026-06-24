#!/bin/bash

# Navigate to the project directory
cd /Users/keithdoesmedia/Documents/Programming/frostylicious-opencode-agent/api-key-rotator

# Activate the virtual environment
source venv/bin/activate

# Execute the script
# We use the python executable from inside the virtual environment
./venv/bin/python rotator.py
