# The Endpoint to interact With OPENAI API
import openai
from SECRET_KEY import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# Create a new stream
stream = openai.Stream.create(
  engine="text-davinci-003",
  prompt="Once upon a time, in a kingdom far, far away,",
  max_tokens=1000
)

# Fetch the stream output incrementally
for output in stream:
    print(output.choices[0].text.strip())
