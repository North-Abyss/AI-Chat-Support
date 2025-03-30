# Use official Python base image
FROM python:3.10

# Set working directory
WORKDIR /src

# Copy project files
COPY . /src

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama in the background and wait for it to initialize
RUN bash -c "ollama serve & sleep 5"

# Pull a valid model (change to "mistral" if TinyLlama is unavailable)
RUN ollama pull tinyllama:1.1b

# Expose port if needed
EXPOSE 5000

# Start Ollama service and run the app
CMD ["bash", "-c", "ollama serve & sleep 5 && python myapp.py"]
