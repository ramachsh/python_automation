import os
import google.generativeai as genai
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment variable
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_topic_details(topic):
    prompt = f"Share some details about {topic}."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        #model="gpt-4.1-nano",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    topic   = input("Enter a topic for which you need to research : ")
    print(f"1.OpenAI")
    print(f"2.Gemini")
    print(f"3.Both")
    choice  = input("Enter which LLM you want to use : ")
    if choice in ['1', '3']:
        details = get_topic_details(topic)
        print("Open AI Research Summary:")
        print("-------------------------")
        print(details)
    if choice in ['2', '3']:
        API_KEY = "AIzaSyAU5Vs6mLn9rRkxdYCNX7Jw_sJkS956AhE"
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(topic)
        print("Gemini Research Summary:")
        print("-----------------------")        
        print(response.text)
    if choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter Correct option.")