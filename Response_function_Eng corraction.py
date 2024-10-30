from openai import OpenAI

# Initialize the client with your API key
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You will be provided with statements, and your task is to convert them to standard English."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "She no went to the market."
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
# Add this line to print the response in the terminal
print(response.choices[0].message.content)
