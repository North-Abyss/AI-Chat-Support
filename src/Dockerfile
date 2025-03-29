# Use a base Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies inside a virtual environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Upgrade pip and install requirements
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama in the background, then pull the model
RUN ollama serve & sleep 5 && ollama pull tinyllama:1.1b

# Expose the port (if needed)
EXPOSE 5000

# Run the app
CMD ["bash", "-c", "ollama serve & sleep 5 && python myapp.py"]
