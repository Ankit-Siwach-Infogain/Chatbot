import google.generativeai as genai

API_KEY = "AIzaSyCnWkEUFPZGOueHfyU4Gpkmp_dd30sQPLc"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

def chat():
    print("Gemini Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("Ask the question: ")
        if user_input.lower() == 'exit':
            print("Exiting....")
            break
        
        try:
            response = model.generate_content(user_input)
            clean_text = response.text.replace("**", "")
            print("Answer:", clean_text)
        except Exception as e:
            print("Error during generation:", e)

if __name__ == "__main__":
    chat()
