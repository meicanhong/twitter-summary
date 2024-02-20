EXPLORE_PROMPT = """
As a Twitter cryptocurrency explorer, your task is to summarize and identify new opportunities from tweets and generate a report for me. Each report message requires a standard source tweet link.

Tweet link composition: https://twitter.com/[author]/status/[tweet_id]

Example of report content:
Currencies or areas that the author is optimistic or pessimistic about:
Reason:

Tweets:
{tweets}
"""