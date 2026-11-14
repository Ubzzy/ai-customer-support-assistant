
from chatbot import ask_ai

print("Fresh Cuts AI Assistant")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ").strip()

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question:
        continue

    try:
        answer = ask_ai(question)
        print(f"\nAI: {answer}\n")
    except Exception as error:
        print(f"\nError: {error}\n")
