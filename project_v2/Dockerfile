FROM python:3

# Set working directory
WORKDIR /app

COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy other required files if any (e.g., templates, static files)
COPY templates/ ./templates/
COPY static/ ./static/

# Command to run the application
CMD ["python", "app.py"]
