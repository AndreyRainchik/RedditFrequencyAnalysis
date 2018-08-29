# Reddit Frequency Analysis

Reddit powerusers typically make multiple posts in a given subreddit to increase their account visibility and karma count. However,  there's a fine balance between posting too much and looking like a spammer, and posting too little and not getting enough visibility. This Python script looks at the top 1000 posts in a given subreddit and finds users who've submitted to it multiple times. Then, it finds the average time between posts for all of these unique users and averages them, resulting in an overall average time differential.

## Requirements
This script relies on the [PRAW](https://praw.readthedocs.io/en/v5.4.0/index.html) package, which gives us access to the Reddit API. Prior to usage, this package must be installed with pip.
The user also needs a Reddit account so that they can request a client ID and client secret from Reddit. The process of doing so can be found [here](https://github.com/reddit-archive/reddit/wiki/OAuth2).
Once the user has these client tokens, they will need to store them in the environment variables pyscript_id and pyscript_secret.
Please be respectful and change the user-agent to reflect the username of the Reddit account that you used.

## Improvements
In the future, I will be adding command-line support for choosing the subreddit, vote threshold, and time range to look through.
