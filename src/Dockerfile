# Use a base image with Python
FROM python:3.10

# Set working directory
WORKDIR /src

# Copy project files
COPY . /src

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Ensure Ollama service starts before pulling the model
RUN ollama serve & sleep 5 && ollama pull tinyllama:1.1b

# Expose port if needed
EXPOSE 5000

# Run Ollama in the background before starting the app
CMD ["bash", "-c", "ollama serve & sleep 5 && python myapp.py"]
