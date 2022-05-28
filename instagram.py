from instapy import InstaPy
import schedule
import time

def job():
    try:
        insta_username = ''  # <- enter username here
        insta_password = ''  # <- enter password here

        # get an InstaPy session!
        # set headless_browser=True to run InstaPy in the background
        session = InstaPy(username="perfumery_67",
                  password="Wasim123",
                  headless_browser=True,
                  want_check_browser=False,
                  nogui=True)
        # Follows the followers of each given user
        # The usernames can be either a list or a string
        # The amount is for each account, in this case 30 users will be followed
        # If randomize is false it will pick in a top-down fashion

        session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False)

        # default sleep_delay=600 (10min) for every 10 user following, in this case
        # sleep for 60 seconds

        # session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False, sleep_delay=60)
    

        # Follow user based on hashtags (without liking the image)

        # session.follow_by_tags(['tag1', 'tag2'], amount=10)

        # but if you like you unfollow only the users followed by InstaPy WHO do not follow you back, use the track- "nonfollowers";
        session.unfollow_users(amount=60, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=90*60*60, sleep_delay=501)

        # Skipping user for private account, no profile picture, business account
        session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=False,
                       no_profile_pic_percentage=100,
                       skip_business=False,
                       business_percentage=100,
                       skip_business_categories=[],
                       dont_skip_business_categories=[])

        session.end()          
    except:
        import traceback
        print(traceback.format_exc())

schedule.every().day.at("02:22").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)







    