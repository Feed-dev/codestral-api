# 1. Fill in the middle
import os
from mistralai.client import MistralClient

api_key = os.getenv("CODESTRAL_API_KEY")
client = MistralClient(api_key=api_key)

model = "codestral-latest"
prompt = "def fibonacci(n: int):"
suffix = "n = int(input('Enter a number: '))\nprint(fibonacci(n))"

response = client.completion(
    model=model,
    prompt=prompt,
    suffix=suffix,
)

print(
    f"""
{prompt}
{response.choices[0].message.content}
{suffix}
"""
)

# 2. Completion
prompt = "def is_odd(n): \n return n % 2 == 1 \ndef test_is_odd():"

response = client.completion(
    model=model,
    prompt=prompt
)

print(
    f"""
{prompt}
{response.choices[0].message.content}
"""
)

# 3. Stop tokens
prompt = "def is_odd(n): \n return n % 2 == 1 \ndef test_is_odd():"
suffix = "n = int(input('Enter a number: '))\nprint(fibonacci(n))"

response = client.completion(
    model=model,
    prompt=prompt,
    suffix=suffix,
    stop=["\n\n"]
)

print(
    f"""
{prompt}
{response.choices[0].message.content}
"""
)

# 4. Instruct endpoint
from mistralai.models.chat_completion import ChatMessage
messages = [
    ChatMessage(role="user", content="Write a function for fibonacci")
]
chat_response = client.chat(
    model=model,
    messages=messages
)
print(chat_response.choices[0].message.content)
