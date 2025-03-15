# LLM Chatbot 🤖  

This project is a **chatbot application** built using **LangChain** and **Streamlit**, powered by **OpenAI's GPT-3.5-turbo**. The chatbot provides real-time responses based on user input.  

---

## Features  

- Built with LangChain for LLM interaction
- Streamlit UI for a user-friendly interface
- Customizable temperature setting for response creativity  
- Supports dynamic user input

---

## Technologies Used  

| Technology  | Purpose  |
|-------------|--------------------------------|
| **Python**  | Core programming language  |
| **LangChain**  | LLM-powered chatbot development  |
| **OpenAI API**  | GPT-based response generation  |
| **Streamlit**  | Web UI for chatbot interaction  |
| **dotenv**  | Secure environment variable management  |

---

## Environment Variables  

Before running the chatbot, set up your **OpenAI API key**.  

1. **Create a `.env` file** in the project directory:  
   ```
   OPENAI_API_KEY=your-openai-api-key
   ```

2. Alternatively, store the API key in a separate **`openai_key.py`** file:  
   ```python
   another_key = "your-openai-api-key"
   ```

---

## Usage  

### Interact with the Chatbot  
- Enter a question in the input box  
- Click **"Get Response"**  
- Receive an AI-generated reply  

---


