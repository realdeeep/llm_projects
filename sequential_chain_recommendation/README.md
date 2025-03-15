# Career Book Recommendation App

## Overview
This project uses the power of OpenAI's language model to provide personalized career book recommendations. By inputting a career goal, users receive a book recommendation and a brief summary of the book. The project uses Langchain for chaining LLMs (Language Models) and Streamlit for building the web interface.

## Features
- **Career Book Recommendation:** Based on your career goal, get a book suggestion to help you grow in your field.
- **Book Summary:** Get a concise 60-word summary of the recommended book in bullet points.
- **Interactive Web Interface:** A simple and intuitive Streamlit-based UI for easy interaction with the system.

## Installation

### Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.7 or later
- Pip (Python package installer)

### Environment Variables
- **OpenAI API Key**: You need to set up your OpenAI API key to access OpenAI's language model. Create an `.env` file in the project root with the following variable:
  ```bash
  OPENAI_API_KEY=your_openai_api_key
  ```

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/realdeeep/llm_projects.git
   cd sequential_chain_recommendation
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**: Create an `.env` file in the project root directory and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

The web app should now be live on `localhost:8501`.

## Usage
1. Enter a career goal (e.g., "data scientist," "software engineer") in the input field.
2. Click on "Get Recommendation" to receive a personalized book recommendation and summary.
3. The book name and its 60-word summary will appear below the input field.

## Technologies Used
- **Python**: The primary programming language.
- **Langchain**: For chaining multiple LLMs and prompts to create a sequential recommendation process.
- **OpenAI GPT**: For generating book recommendations and summaries.
- **Streamlit**: For building the interactive web interface.
- **Dotenv**: For loading environment variables securely.

---

This template provides a clean and informative readme for your project. You can update the sections based on your repo specifics and future changes!
