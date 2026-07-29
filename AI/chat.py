import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6IF9vn2ta5WHmUfIe5ilhN3CdX0VGX_vDb2Wnsi2Q2jQA")

model = genai.GenerativeModel("gemini-flash-latest")

print("AI Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot : Goodbye!")
        break
    response = model.generate_content(user)

    print("Bot:",response.text)