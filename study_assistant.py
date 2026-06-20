import ollama

def ask_ai(question):
    response = ollama.chat(
        model='llama3.2:1b',
        messages=[
            {
                'role': 'system',
                'content': 'You are a helpful study assistant for an Electrical Engineering student. Explain concepts clearly and simply.'
            },
            {
                'role': 'user',
                'content': question
            }
        ]
    )
    return response['message']['content']

def main():
    print("=== AI Study Assistant ===")
    print("Type 'exit' to quit\n")

    while True:
        user_question = input("Ask your question: ")

        if user_question.lower() == 'exit':
            print("Goodbye!")
            break

        print("\nThinking...\n")
        answer = ask_ai(user_question)
        print("Answer:", answer)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()