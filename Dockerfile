FROM python:3.9

# Copy requirements.txt first for efficient caching
COPY requirements.txt .


# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy the pipeline.py file
COPY ingest_data.py ingest_data.py

# Override the entrypoint
ENTRYPOINT [ "python","ingest_data.py" ]
