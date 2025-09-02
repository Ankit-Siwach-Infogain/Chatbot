import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
TOKENS = 30

def token(his):
    return len(his.split())

def summarize(his):
    token_count = token(his)
    
    if token_count > TOKENS:
        
        prompt = f"Please summarize the following conversation while retaining the key context. The total conversation is over {TOKENS} tokens, so provide a concise summary:\n\n{his}"
        try:
            res = model.generate_content(prompt)
            summary = res.text
            return summary  
        except Exception as e:
            print(f"Error during summarization: {e}")
            return his  
    return his  



if not API_KEY:
    raise ValueError("API_KEY not found.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

def chat():
    print("Gemini Chatbot (type 'exit' to quit)")

    history = ""
    while True:
        ques = input("Ask the question: ")
        if ques.lower() == 'exit':
            print("Exiting....")
            break
        
        try:
            history += f"\n {ques}\n"
            history = summarize(history)
            print("="*10 + " Context " + "="*10)
            print(history)
            print("="*30)
            response = model.generate_content(history)
            clean_text = response.text.replace("**", "")
            print("Answer:", clean_text)
            print("="*30)
        except Exception as e:
            print("Error during generation:", e)

if __name__ == "__main__":
    chat()
