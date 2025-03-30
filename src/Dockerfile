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

# Expose necessary ports
EXPOSE 5000 11434

# Start Ollama service in the background, wait until it's ready, then pull the model and start the app
CMD ollama serve & \
    until curl --silent --fail http://127.0.0.1:11434 > /dev/null; do sleep 1; done && \
    ollama pull tinyllama:1.1b && \
    python myapp.py
