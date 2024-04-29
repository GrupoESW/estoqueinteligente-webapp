FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# Add current directory content to /app in the container
ADD ./app /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org Flask==2.0.3

#RUN apt update && apt install -y git && rm -rf /var/lib/apt/lists/*

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
