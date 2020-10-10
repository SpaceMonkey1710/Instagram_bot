from instapy import InstaPy # need to install library later

session = InstaPy(username="among_us.russia", password="TrySomethingNew")
session.login()

session.like_by_tags(["amongus", "amongusmemes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Lol!", ":heart_eyes:"])
session.end()