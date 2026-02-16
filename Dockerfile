FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY sip_calculator.py ./

# Define the command to run the script when the container starts
CMD ["python", "./sip_calculator.py"]
