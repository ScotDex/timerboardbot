#!/bin/bash

# Build the Docker image
docker build -t my_discord_bot .

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from the Discord Developer Portal
BOT_TOKEN="YOUR_BOT_TOKEN"

# Run the Docker container with environment variable for bot token
docker run -e BOT_TOKEN="$BOT_TOKEN" my_discord_bot
