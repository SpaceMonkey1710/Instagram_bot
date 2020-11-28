# Instagram_bot
This bot is made to ease routine tasks like getting info about account followers and follows, unsubscribing from people, who doesn't follow back.
For personal use only, don't violate Instagram rules.

## What it does
- Logs in to your Instagram account (Install Mozilla Firefox, download here https://www.mozilla.org/ru/firefox/)
- Skips notifications windows
- Goes to your hope page
- Presses follows button
- 'compare_follows.py' creates list of follows in 'follows.txt'
- Presses followers button
- 'compare_followers.py' creates list of followers in 'followers.txt'
- 'unfollow.py' creates list of accounts which didn't follow you back in 'unfollow.txt'
- Using 'unfollow.txt' goes to each account page and clicks unfollow button

Also you can use 'instabot.py' for likes, subscribes and comments.
```python
# Here you can set up comments bot needs to leave under posts
# of tags you choose
session.set_do_follow(True, percentage=20)        # percentage of following
session.set_do_comment(True, percentage=50)       # percentage of liking
session.set_comments(["Nice!", "Lol!", ":joy:"])  # write your comments text
session.like_by_tags(["tag", "tag"], amount=5)    # number of posts of certain tags you want to leave a like
session.set_dont_like(["naked", "nsfw", "art"])   # stop-tags you don't want to see
```

## How to set up private data
In the same directory create 'secrets.py' file with your Instagram account password and username so webdriver was able to log you in
```python
from secrets import password, username
```
Also download geckodriver from here https://github.com/mozilla/geckodriver/releases and write it's path 
```python
driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
```
## Important!
According to the Instagram security measures against bots try not to exceed 100 unfollows per day or service will hide your follows/followers data from you for up to 3 days. 
In this case bot won't be able to continue it's task.

## License
[MIT](https://choosealicense.com/licenses/mit/)
