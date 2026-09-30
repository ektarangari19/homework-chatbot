from ollama import chat


def get_answer(question):

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": """
                You are Homework Helper AI.
                Help students with their homework.
                Explain answers clearly and simply.
                For mathematics, show step-by-step solutions.
                For programming, explain the code clearly.
                """
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]