# Use a base image that includes common build tools
FROM python:3.10-slim
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set up directories for I/O as specified in the challenge
RUN mkdir -p /app/input /app/output

# The command to run the application
CMD ["python", "main.py"]