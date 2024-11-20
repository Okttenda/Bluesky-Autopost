import string
from atproto import Client
import sys
import os
from dotenv import load_dotenv

def TestPost():
    post = client.send_post("This is a Test Post sended by a Programm")
    print("Post sended... pasting post.uri and post.cid..." + post.uri + "/n" + post.cid)

def login():
    load_dotenv()
    handle = os.getenv("HANDLE")
    password = os.getenv("PASSWORD")
    client = Client()
    try:
        client.login(handle, password)
        print("Login complete...")
    except handle == None or password == None:
        print("[ERROR]Missing Bluesky Handle or/and Password.")
        sys.exit()
    
def action():
    print("What do you want to do?")
    print("Test Post | exit")
    doing = input()
    if doing == "Test Post" or doing == 1:
       TestPost()
    elif doing == "exit" or doing == 2:
        sys.exit()
    else:
        sys.exit()

def getDID():
    data = Client.get_profile(actor=["Okttenda.bsky.social"])
    did = data.did
    displayName = data.display_name
    return did, displayName