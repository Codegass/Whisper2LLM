from SEC import OPENAI_API_KEY
from API.openai_endpoint import OpenAPI


if __name__ == "__main__":
    ai_api = OpenAPI(OPENAI_API_KEY)
    prompt = "Explain the Transformer to me"
    response = ai_api.get_chat_response(prompt=prompt)
    print(response)

