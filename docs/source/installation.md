
# Installation Guide

## Prerequisites

- Python 3.8 or higher
- Ollama server running locally
- Sufficient storage for vector databases

## Step-by-Step Installation


1. Clone the repository:
```bash
git clone <your-repository-url>
```

2. Install dependencies : 
```bash
pip install -r requirements.txt
```

3. Start Ollama server : 
```bash
ollama serve
```

4. Pull required models : 
```bash
ollama pull llama3.1
ollama pull mistral
ollama pull gemma:7b
```
