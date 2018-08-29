import datetime
import os
import praw

def get_reddit():
    # Return a read-only Reddit instance given the user's
    # generated client id and client secrets stored in
    # environment variables
    cid = os.getenv("pyscript_id")
    csecret = os.getenv("pyscript_secret")
    cua = "Windows 10:Python script:v0.0.1 (by /u/<INSERT YOUR REDDIT USERNAME>)"
    return praw.Reddit(client_id = cid,
                         client_secret = csecret,
                         user_agent = cua)

def get_submissions(reddit, subreddit, vote_limit, time):
    # Return 1000 submissions from a given subreddit's user-chosen
    # top of day, week, month, year, or all-time with scores greater
    # or equal to a given vote threshold. The 1000 submission limit
    # is due to a Reddit policy.
    posts = []
    for submission in reddit.subreddit(subreddit).top(time, limit=1000):
        if submission.score >= vote_limit:
            posts.append(submission)
        else:
            break
    return posts

def get_date(submission):
    # Return the datetime object corresponding to a submission's
    # creation date
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

def get_author(submission):
    # Return the author of a given submission
    try:
        author = submission.author.name
    except AttributeError:
        author = "[Deleted]"
    return author

def get_author_frequency(submissions):
    # Return the frequency of which unique authors post on a subreddit
    posters = {}
    for submission in submissions:
        author = get_author(submission)
        if author not in posters and author != "[Deleted]":
            posters[author] = [get_date(submission)]
        elif author != "[Deleted]":
            posters[author].append(get_date(submission))
    return posters

def get_multi_authors(auths):
    # Return all authors that post multiple times on a subreddit
    multi = []
    for k, v in auths.items():
        if len(v) > 1:
            multi.append([k, v])
    return multi

def get_post_differential(multi):
    # Return the time differentials between unique authors' consecutive posts
    difs = []
    for i in multi:
        i[1].sort()
        for j in range(len(i[1])-1):
            difs.append(i[1][j+1] - i[1][j])
    return difs

def get_differential_average(difs):
    # Return the average differential for all unique authors' consecutive posts
    total = difs[0]
    for i in range(1, len(difs)):
        total += difs[i]
    return total / len(difs)
        
def main():
    # Main function
    reddit = get_reddit()
    posts = get_submissions(reddit, "pics", 100, "year")
    auths = get_author_frequency(posts)
    multi = get_multi_authors(auths)
    difs = get_post_differential(multi)
    avg = get_differential_average(difs)
    print(avg)

if __name__ == "__main__":
    main()
