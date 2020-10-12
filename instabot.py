from instapy import InstaPy
import os

# Delete cookies so Instagram doesn't block bot for massliking

location = "C:/Users/bochk/InstaPy/logs/among_us.russia/"
file = "among_us.russia_cookie.pkl"
path = os.path.join(location, file)
try:
    os.remove(path)
    print('Cookie file "among_us.russia_cookie.pkl" has been deleted')
except:
    print("Cookies file doesn't exist")


session = InstaPy(username="among_us.russia", password="TrySomethingNew")
session.login()

session.set_do_follow(True, percentage=20)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Lol!", ":joy:"])
session.like_by_tags(["amongus", "amongusmemes"], amount=5)
session.set_dont_like(["naked", "nsfw", "art"])


session.end()