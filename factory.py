from openai import OpenAI

from config.config import appConfig

openai_client = OpenAI(api_key=appConfig.get('openai').get('api_key'))