#!/bin/bash

# Build the Docker image
docker build -t my_discord_bot .

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from the Discord Developer Portal
BOT_TOKEN="MTEzMzc1NDc3NjQ2MzYyNjI4MA.GOB_gq.Y0kNW-W2XDmpznOwesFycVDLKRsWw1YSqFndSA"

# Run the Docker container with environment variable for bot token
docker run -e BOT_TOKEN="$BOT_TOKEN" my_discord_bot
