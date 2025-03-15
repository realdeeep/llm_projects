# PDF Query Tool

## Overview  
The **PDF Query Tool** leverages **LangChain, OpenAI LLM, and Astra DB** to extract and query information from PDF documents. It processes text, stores vector embeddings, and allows for intelligent question-answering based on the document's content.

## Features  
- Extracts text from PDF documents using `PyPDF2`.  
- Splits text into manageable chunks for efficient storage.  
- Uses **OpenAI's embeddings** to store and retrieve relevant information.  
- Queries the stored document using an LLM to provide context-aware responses.  

## Installation  

### Prerequisites  
Ensure you have **Python 3.8+** installed. Then, install the required dependencies:  

```bash
pip install -r requirements.txt
```
### Environment Variables
Before running the script, set up your API keys as environment variables:
```bash
export ASTRA_DB_APPLICATION_TOKEN="your_astra_db_token"
export ASTRA_DB_ID="your_astra_db_id"
export OPENAI_API_KEY="your_openai_api_key"
```
Alternatively, you can store these in a .env file.

### Usage
- Place the PDF file in the project directory.
- Modify the pdf_path variable in pdf_query.py to match your file.
- Run the script:
```bash
python pdf_query.py
```
- The script will extract text, store it in a vector database, and allow you to query it.

### Technologies Used
- LangChain – For handling LLM-based queries
- OpenAI LLM – For generating intelligent responses
- Astra DB (Cassandra) – For efficient vector storage
- PyPDF2 – For PDF text extraction
