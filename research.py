import os
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
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    details = get_topic_details(topic)
    print(f"Details about {topic}:\n{details}")
