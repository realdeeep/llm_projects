# LLM Chatbot 🤖  

This project is a **chatbot application** built using **LangChain** and **Streamlit**, powered by **OpenAI's GPT-3.5-turbo**. The chatbot provides real-time responses based on user input.  

---

## Features  

**Built with LangChain** for LLM interaction  
**Streamlit UI** for a user-friendly interface  
**Customizable temperature setting** for response creativity  
**Supports dynamic user input**  

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

## Installation  

### lone the Repository  
```bash
git clone https://github.com/your-repo/llm_chatbot.git
cd llm_chatbot
```

### Set Up a Virtual Environment (Optional)  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3Install Dependencies  
```bash
pip install -r requirements.txt
```

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

### Run the Chatbot  
```bash
streamlit run chatbot.py
```

### Interact with the Chatbot  
- Enter a question in the input box  
- Click **"Get Response"**  
- Receive an AI-generated reply  

---

## Example Interaction  

```text
User: "Tell me a fun fact about space!"
Chatbot: "Did you know that a day on Venus is longer than a year on Venus?"
```

---
