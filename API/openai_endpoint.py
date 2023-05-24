# The Endpoint to interact With OPENAI API
import openai
import logging


class OpenAPI:
    
    def __init__(self, OPENAI_API_KEY):
        openai.api_key = OPENAI_API_KEY
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_chat_response(self, prompt):
        openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a interviewee who are aksing coding questions related to Python"},
                {"role": "user", "content": "Please answering the following interview questions detailedly, and if possible, plese provide the code with it."},
                {"role": "asisstant", "content": "Sure, I will try my best to answer your coding interview questions."},
            ]
        )

    def response_parser(self, response):
        '''
        Parse the chat response from the openai api 
        and analyze the stop condition for further processing
        '''

        if response['choices'][0]['finish_reason'] == 'stop':
            return response['choices'][0]['message']['content']

        if response['choices'][0]['finish_reason'] == 'length':
            self.logger.info("The response is too long, please consider to use the continue prompt")
            return response['choices'][0]['message']['content']

        if response['choices'][0]['finish_reason'] == 'content_filter':
            self.logger.info("The content is blocked due to the content policy in the openai")
            return response['choices'][0]['message']['content']
      
        if response['choices'][0]['finish_reason'] == 'null':
            self.logger.info("API response still in progress or incomplete")
            return response['choices'][0]['message']['content']
