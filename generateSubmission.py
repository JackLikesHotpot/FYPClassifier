import praw
from praw.models import MoreComments


# Generates a Reddit submission of at least 100 comments and analyses the comments.
def generateSub():
    counter = 0                                                 # keep a track of how many comments
    subComments = []                                                        

    reddit = praw.Reddit(client_id='SJN5UEqC9iaFHg', client_secret='KYw-MSxoypI3EezUab-V4X_qAO4',
                         user_agent='FYP-RedditClassifier by /u/Frothpot')              # api details
    submission = reddit.subreddit('worldnews').random()                                 # get a random submission from /r/worldnews

    while submission.comments.__len__() < 100:                         
        #submission = reddit.submission(id='')                  
        submission = reddit.subreddit('worldnews').random()             # select another submission until it has at least 100 comments

    redditTitle = submission.title                                      # get the title of the submission
    sub = reddit.submission(id=submission)

    for comment in sub.comments:                                        # iterate through each comment
        if counter == 100:                                              # break if 100 comments
            break
        if isinstance(comment, MoreComments):                           # if it is a comment object then continue
            continue
        if comment.author != 'autotldr' and comment.author != 'AutoModerator' and comment.body != '[deleted]' and comment.body != '[removed]':
            subComments.append(comment.body)                            # ignore specific comments
            counter += 1

    return redditTitle, subComments                                     # return the title of the submission and comments
