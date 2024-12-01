# API Reference

## Core Functions

### load_documents(uploaded_files)

Loads and processes uploaded documents.

Parameters:
- `uploaded_files`: List of uploaded file objects

Returns:
- List of processed documents

### create_vector_store(documents, model_name)

Creates a vector store from processed documents.

Parameters:
- `documents`: List of processed documents
- `model_name`: String name of the LLM model

Returns:
- Tuple of (vector_store, embed_model)

## Main Application

### main()

Main Streamlit application function that handles:
- Model selection
- File uploading
- Document processing
- Q&A interface
