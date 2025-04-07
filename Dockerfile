# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 3000
EXPOSE 3000

# Start Gunicorn WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "wsgi:app"]
