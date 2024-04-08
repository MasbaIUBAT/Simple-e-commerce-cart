FROM ubuntu:latest

# Update package lists and install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install --upgrade pip

# Set the working directory
WORKDIR /app/Simple-e-commerce-cart

# Copy the contents of the host's Simple-e-commerce-cart directory to the container's working directory
COPY . /app/Simple-e-commerce-cart

# Install Python dependencies


# Set the default command to run the Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
