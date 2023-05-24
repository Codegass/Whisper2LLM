from SEC import OPENAI_API_KEY
from API.openai_endpoint import OpenAPI


if __name__ == "__main__":
    openai = OpenAPI(OPENAI_API_KEY)
    prompt = "Explain the Transformer to me"
    response = openai.get_response(prompt=prompt)
    print(response)

