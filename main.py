import os
from dotenv import load_dotenv
import openai

load_dotenv()   

API_KEY = os.getenv("api_key") 
MODEL = os.getenv("model")

openai.api_key = API_KEY

def main():
    prompt = """How big is the sun?
    ---
    How long will take us to populate mars?
    """
    res = openai.Completion.create(
        prompt = prompt,
        model = MODEL,
        max_tokens = 1000, # Max tokens input
        temperature=0.9,
        n=2, # Number of output returns
        stop=['---']
    )
    
    print(res.choices)

if __name__ == "__main__":
    main()