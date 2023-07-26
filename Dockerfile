# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Create the required directories (empty) to satisfy the platform's expectations
RUN mkdir -p /workspace/_static /workspace/dist /workspace/public /workspace/build

# Copy the Python bot script and requirements.txt to the container
COPY eve_timer_bot.py .
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python bot script
CMD ["python", "eve_timer_bot.py"]
