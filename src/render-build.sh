#!/bin/bash
pip install -r requirements.txt
ollama pull $OLLAMA_MODEL  # Uses the environment variable
