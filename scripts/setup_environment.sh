#!/bin/bash

# Script to set up the development environment

echo "Setting up the development environment..."

# Update package lists
sudo apt-get update

# Install Python and pip
sudo apt-get install -y python3 python3-pip

# Install required Python packages
pip3 install -r requirements.txt

# Create necessary directories
mkdir -p logs
mkdir -p data
mkdir -p backups

echo "Development environment setup complete."
