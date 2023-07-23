import openai, sys

openai.api_key = "Your API key"

with open(str(sys.argv[1])) as f:
    content = f.read()

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.2,
    max_tokens = 3333,  
    messages = [
      {"role": "system", "content": "You are a computer programmer"},
      {"role": "user", "content": content}
    ]
)

print(completion.choices[0].message["content"]) 
