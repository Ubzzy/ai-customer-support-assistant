
from chatbot import create_chat, ask_ai

chat = create_chat()

print("Fresh Cuts AI Assistant")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ").strip()

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question:
        continue

    answer = ask_ai(chat, question)
    print(f"\nAI: {answer}\n")
