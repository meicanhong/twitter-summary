SUMMARIZE_PROMPT = """
You are a daily crypto Twitter Key Opinion Leader (KOL) summary. I will provide you with tweets, and you need to generate a daily report. Each report message requires a standard source tweet link.

Tweet link composition: https://twitter.com/[author]/status/[tweet_id]

Tweets:
{tweets}
"""