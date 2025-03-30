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

# Pull TinyLlama model
RUN ollama pull tinyllama:1.1b

# Expose port if needed
EXPOSE 5000

# Start Ollama service and ensure it's ready before running the app
CMD ["bash", "-c", "ollama serve & while ! ollama list >/dev/null 2>&1; do sleep 1; done && python myapp.py"]
