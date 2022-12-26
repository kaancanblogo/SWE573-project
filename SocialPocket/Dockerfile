FROM python:3.8

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add code for the Django app
COPY . .

# Set the working directory to the root directory of the Django project
WORKDIR /app

# Create a start script to start the Django development server and the MongoDB database
CMD ["sh", "./start.sh"]