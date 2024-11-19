from atproto import Client
import sys

client = Client()
client.login('okttenda.bsky.social', '3266-s42a-s4ra-ximv')
print("Login complete...")

def TestPost():
    post = client.send_post("This is a Test Post sended by a Programm")
    print("Post sended... pasting post.uri and post.cid..." + post.uri + "/n" + post.cid)


print("What do you want to do?")
print("Test Post | exit")
doing = input()
if doing == "Test Post" or 1:
    TestPost()
elif doing == "exit" or 2:
    sys.exit()