#!/bin/bash

# Deployment script for production

echo "Starting deployment..."

# Pull the latest code from the repository
git pull origin main

# Install any new dependencies
pip install -r requirements.txt

# Run database migrations (if applicable)
# python manage.py migrate

# Restart the application (assuming a systemd service)
sudo systemctl restart your_application.service

echo "Deployment complete."
