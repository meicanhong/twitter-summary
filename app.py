from crawler.twitter.twitter import get_tweets
from config.config import appConfig
import datetime

def main():
    print(appConfig.get_all())

    screenname = appConfig.get('rapidapi').get('screenname')
    data = get_tweets(screenname)

    timestamp = datetime.datetime.now().timestamp()
    filename = f"{screenname}-{timestamp}.txt"
    for tweet in data['timeline']:
        item = {"author": data['user']['name'], "created_at": tweet['created_at'], "text": tweet['text']}
        with open(filename, 'a') as f:
            f.write(str(item) + '\n')
            
    
if __name__ == "__main__":
    main()

