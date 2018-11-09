from github import Github
from github import GithubException
import getpass
import time

def get_login():
    loggedin = False
    while loggedin is False:
        try:
            user = input("\nPlease enter your username:\n")
            pw = getpass.getpass('Please enter your password: ')
            g = Github(user, pw)
            account = g.get_user()
            account.login
            loggedin = True

            print("Cheers! Gathering some info now...")
            user = "foo"
            pw = "bar" # this probably doesn't make the program any safer but sure lookit may as well
            return account
        except GithubException:
            print("bad login, try again pls hun x")
            time.sleep(1.5)


def get_login_direct(user, pw):
    retval = Github(user, pw)
    user = "foo"
    pw = "bar" # this probably doesn't make the program any safer but sure lookit may as well
    return retval

def main():
    account = get_login()

    repos = account.get_repos()

    print("\n\n You've got " + str(repos.totalCount) + " repositories (Including your pins!). Here's a list of them:")

    for repo in repos:
        print("- " + repo.name + " - " + str(repo.stargazers_count) + " Stars - " + str(len(repo.get_contents(""))) + " Files & Folders.")


    followers = account.get_followers()
    following = account.get_following()

    print("\nYou've got " + str(followers.totalCount) + " followers, and you are currently following " + str(following.totalCount) + " users.")
    ftof = followers.totalCount / following.totalCount

    if(ftof > 1):
        print("For every user you follow, " + str(ftof) + " users follow you. Nice!")
    elif(ftof < 1):
        print("For every user you follow, " + str(ftof) + " users follow you. oof.")
    else:
        print("(sweet follow for follow ratio!)\n")




if __name__ == '__main__':
    main()
