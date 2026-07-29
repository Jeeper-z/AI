while True :
    user = input ("you:" )

    if user.lower() == "Bye":
        print("Bot: Goodbye! have a nice day.")
        break

    print("Bot: you said:",user)





    responses={
    "hello":"Hi! How are you?",
    "good morning":"Good morning! How are you today?",
    "hi":"Hello!",
    "how are you":"I am doing great!",
    "bye":"Goodbye!"
}    
while True:
    user = input("You: ").lower()

    if user.lower() == "bye":
        print("Bot:",responses["bye"])
        break

    print("Bot:",responses.get(user, "Sorry,I dont understand that."))


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