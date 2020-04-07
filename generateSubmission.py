import praw
from praw.models import MoreComments


# Generates a Reddit submission of at least 50 comments and analyses the comments.
def generateSub():
    counter = 0
    subComments = []

    reddit = praw.Reddit(client_id='SJN5UEqC9iaFHg', client_secret='KYw-MSxoypI3EezUab-V4X_qAO4',
                         user_agent='FYP-RedditClassifier by /u/Frothpot')
    submission = reddit.subreddit('worldnews').random()

    while submission.comments.__len__() < 100:
        #submission = reddit.submission(id='')
        submission = reddit.subreddit('worldnews').random()

    redditTitle = submission.title
    sub = reddit.submission(id=submission)

    for comment in sub.comments:
        if counter == 100:
            break
        if isinstance(comment, MoreComments):
            continue
        if comment.author != 'autotldr' and comment.author != 'AutoModerator' and comment.body != '[deleted]' and comment.body != '[removed]':
            subComments.append(comment.body)
            counter += 1

    return redditTitle, subComments
