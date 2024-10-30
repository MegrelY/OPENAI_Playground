# Your existing code (modified to read prompt from a file)
from openai import OpenAI

# Initialize the client with your API key
client = OpenAI()

# Read prompt from a file named 'prompt.txt'
with open('input.txt', 'r' ,encoding='utf8') as file:
    user_prompt = file.read().strip()  # Strip any trailing newline or spaces

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "Summarize content you are provided with for a second-grade student."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": user_prompt  # Replace hardcoded text with the content from 'prompt.txt'
        }
      ]
    }
  ],
  temperature=0,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)

# Print only the content of the response
print(response.choices[0].message.content)