import json

from constant import PATH
from prompt import prompt_dict
from util.openai_util import chat_response
from util.twitter_util import pull_tweets
import datetime
from unstructured.cleaners.core import clean


def get_tweets(username: str):
    data = pull_tweets(username)

    timestamp = datetime.datetime.now().timestamp()
    filename = f"{username}-{timestamp}.txt".lower()
    result = []
    for tweet in data['timeline']:
        published_at = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y')
        author = data['user']['name']
        quoted = tweet.get('quoted', None)
        # 如果有引用的话，就把引用的内容也加进去
        content = tweet['text'] if not quoted else f"{tweet['text']} Quoted:({quoted['text']})"
        content = clean(content, extra_whitespace=True, dashes=True, bullets=True, lowercase=True)

        item = {
            "author": author,
            "published_at": published_at.strftime("%Y-%m-%d %H:%M:%S"),
            "content": str(content)
        }
        result.append(item)
    with open(PATH + filename, 'w') as f:
        f.write(json.dumps(result, ensure_ascii=False))
    return result


def summarize_tweets(tweets, analyze_type: str = "summarize"):
    prompt = prompt_dict[analyze_type].format(tweets=tweets)
    return chat_response(prompt)


def main(username: str, analyze_type: str = 'summarize'):
    if analyze_type not in prompt_dict:
        raise ValueError(f"Invalid analyze_type. Expected one of {list(prompt_dict.keys())}, but got {analyze_type}")

    tweets = get_tweets(username)
    return summarize_tweets(tweets, analyze_type=analyze_type)


if __name__ == "__main__":
    result = main(username="hellosuoha", analyze_type="token")
    print(result)
