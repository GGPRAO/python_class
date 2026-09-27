import ollama

response = ollama.chat(
    model="qwen2:1.5b",
    messages=[
        {"role": "user", "content": "Hello, summarize jobs"}
    ]
)

print(response["message"]["content"])