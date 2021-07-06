#Reddit post and comment deleter
import praw
import sys

reddit = praw.Reddit(
    client_id="-----", #Enter your account information here
    client_secret="-----",
    password="-----",
    user_agent="Reddit post and comment deleter by github.com/Piyush3131",
    username="-----",
)

user = reddit.user.me()

def comment():                                  #Function for deleting comments
    for x in user.comments.new():
        x.edit("Testing")
        x.delete()
    print("Comments successfully deleted!")

def post():                                    #Function for deleting post
    for x in user.submissions.new():
        x.delete()
    print("Posts successfully deleted!")

def main(argv):
    for argument in argv:
        if(argument == argv[0]):
            continue
        if(argument == "-c"):
            print("Deleting Comment")
            comment()
        if(argument == "-p"):
            print("Deleting Post")
            post()
        if(argument != "-c" and argument != "-p"):
            print("Invalid argument\nUse:\n-p to delete post\n-c to delete comments")

main(sys.argv)



