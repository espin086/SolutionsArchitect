import argparse
from openai import OpenAI


def initialize_openai_client():
    """Initializes the OpenAI client."""
    # Initialize the OpenAI client
    return OpenAI()


def generate_response(client, messages, user_prompt):
    """Generates a response to the user's question."""
    # Add the user's question to the messages as a User Role
    messages.append({"role": "user", "content": user_prompt})
    # Generate a completion using the user's question
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
    )
    # Get the response
    model_response = completion.choices[0].message.content
    # Add the response to the messages as an Assistant Role
    messages.append({"role": "assistant", "content": model_response})
    return model_response


def main(question, content):
    """The main function."""
    # Define the System Role
    messages = [
        {
            "role": "system",
            "content": content,
        }
    ]

    # Initialize the OpenAI client
    client = initialize_openai_client()

    # Generate the response
    model_response = generate_response(client, messages, question)

    return model_response


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description="GPT Chatbot")
    parser.add_argument("question", type=str, help="The question to ask the chatbot")
    parser.add_argument(
        "content",
        type=str,
        help="Clearly define the type of content the chatbot should generate.",
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    response = main(args.question, args.content)
    print(response)
