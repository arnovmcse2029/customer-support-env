FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Prevent Python buffering
ENV PYTHONUNBUFFERED=1

# Expose port (Hugging Face uses 7860)
EXPOSE 7860

# Run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]