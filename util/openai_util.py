from factory import openai_client


def chat_response(content: str, role: str = "user") -> str:
    result = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": role, "content": content},
        ]
    )
    return result.choices[0].message.content
