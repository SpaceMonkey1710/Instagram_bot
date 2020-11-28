from instapy import InstaPy
import os
from secrets import username, password

# Delete cookies so Instagram doesn't block bot for massliking
# username - your Instagram account name

location = "C:/Users/name/InstaPy/logs/username/"
file = "username_cookie.pkl"
path = os.path.join(location, file)
try:
    os.remove(path)
    print('Cookie file "username_cookie.pkl" has been deleted')
except:
    print("Cookies file doesn't exist")

session = InstaPy(username=username, password=password)
session.login()

# Here you can set up comments bot needs to leave under posts
# of tags you choose
session.set_do_follow(True, percentage=20)        # percentage of following
session.set_do_comment(True, percentage=50)       # percentage of liking
session.set_comments(["Nice!", "Lol!", ":joy:"])  # write your comments text
session.like_by_tags(["tag", "tag"], amount=5)    # number of posts of certain tags you want to leave a like
session.set_dont_like(["naked", "nsfw", "art"])   # stop-tags you don't want to see

session.end()
