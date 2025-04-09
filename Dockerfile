# Use official Python runtime as the base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY generate_qr.py .

# Ensure the qr_codes directory is available in the container
VOLUME /app/qr_codes

# Run the script when the container launches
CMD ["python", "generate_qr.py"]
