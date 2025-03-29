# Use a Python base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Add Ollama to PATH (if needed)
ENV PATH="/root/.ollama/bin:$PATH"

# Copy all project files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Pull the TinyLlama model
RUN ollama pull tinyllama:1.1b

# Set the default command to run your app
CMD ["python", "app.py"]
