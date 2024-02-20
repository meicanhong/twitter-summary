import json

from constant import PATH
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


def summarize_tweets(data):
    prompt = f"""
You are a daily crypto Twitter Key Opinion Leader (KOL) summary. I will provide you with tweets, and you need to generate a daily report:

Tweet:
{data}
    """
    return chat_response(prompt)

def main(username):
    tweets = get_tweets(username)
    return summarize_tweets(tweets)


if __name__ == "__main__":
    result = main(username="Phyrex_Ni")
    print(result)
