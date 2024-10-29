from openai import OpenAI

# Initialize the client with your API key
client = OpenAI()

# Function to maintain the ongoing conversation
def ongoing_conversation():
    # Messages list to hold the conversation history
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("Chat with GPT-4o. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Add user's message to the conversation history
        messages.append({"role": "user", "content": user_input})

        # Get the assistant's response
        completion = client.chat.completions.create(
            model="gpt-4-turbo-preview",  # This is the latest model as of October 2024
            messages=messages
        )

        # Extract the response
        assistant_response = completion.choices[0].message.content
        print(f"GPT-4o: {assistant_response}")

        # Append assistant's response to the conversation history
        messages.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    ongoing_conversation()
