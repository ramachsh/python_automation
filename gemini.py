import google.generativeai as genai

# Replace with your actual Gemini API key
# Replace with your actual Gemini API key
API_KEY = "AIzaSyAU5Vs6mLn9rRkxdYCNX7Jw_sJkS956AhE"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')
topic = input("Enter a topic: ")
prompt = f"Summarize recent research trends about {topic}."

response = model.generate_content(prompt)

print("Gemini Research Summary:")
print(response.text)
