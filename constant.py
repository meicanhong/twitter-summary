import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__))))
TWEET_RAW_PATH = './data/'
PROMPT_PATH = './prompts/'

if __name__ == '__main__':
    print(PROJECT_PATH)