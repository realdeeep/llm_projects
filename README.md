# LLM Projects Repository

This repository contains three LLM-based projects built using OpenAI's GPT models, LangChain, and Streamlit. These projects demonstrate different applications of LLMs, including PDF querying, chatbot development, and sequential chains for recommendations.

## Projects

### 1. PDF Query Tool
- Extracts text from PDFs and stores them efficiently using Astra DB.
- Uses LangChain to create a vector database for querying document content.
- Allows users to ask questions about the document and receive relevant answers.

📂 **Folder:** `pdf_query_tool`

### 2. LLM Chatbot
- A simple chatbot built using LangChain and Streamlit.
- Takes user input and generates responses using OpenAI's GPT model.
- Interactive web-based interface.

📂 **Folder:** `llm_chatbot`

### 3. Sequential Chain Recommendation System
- Uses LangChain's `SequentialChain` to generate book recommendations.
- Given a career choice, suggests a relevant book and summarizes it.
- Includes a Streamlit interface for user interaction.

📂 **Folder:** `sequential_chain_recommendation`

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- An OpenAI API Key
- Astra DB credentials (for the PDF Query Tool)

### Installation
Clone this repository and install dependencies:

```bash
git clone https://github.com/your_username/llm_projects.git
cd llm_projects
pip install -r requirements.txt
```

### Running the Projects
Each project has its own folder. Navigate to a project folder and run the respective script:

#### PDF Query Tool
```bash
cd pdf_query_tool
python pdf_query.py
```

#### LLM Chatbot
```bash
cd llm_chatbot
streamlit run chatbot.py
```

#### Sequential Chain Recommendation
```bash
cd sequential_chain_recommendation
streamlit run recommendation_app.py
```

---

## Dependencies
All required dependencies are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

---

## Folder Structure
```
llm_projects/
│── pdf_query_tool/
│   ├── pdf_query.py
│   ├── README.md
│
│── llm_chatbot/
│   ├── chatbot.py
│   ├── README.md
│
│── sequential_chain_recommendation/
│   ├── recommendation_app.py
│   ├── README.md
│
│── requirements.txt
│── README.md
```

---
