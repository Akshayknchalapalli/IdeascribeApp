from flask import Flask
import openai

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

from app import routes