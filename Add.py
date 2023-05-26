import sqlite3
from cryptography.fernet import Fernet
import os
from getAccount import instabID
from deifne import getCreds
from long_lived_access_token import get_long_lived_access_token

'''def write_key():
    key = Fernet.generate_key()
    with open("key" + ".key", "wb") as key_file:
        key_file.write(key)
    os.system('attrib +h key.key')'''

def load_key():
    file = open("key" + ".key", "rb")
    key = file.read()
    file.close()
    return key
def encrypt(instaid):

    '''write_key()'''
    key = load_key()
    fer = Fernet(key)
    encry_id = fer.encrypt(instaid.encode()).decode()
    return encry_id


def date():
    day = input('Enter the "day of the month" reel has to be uploaded into your Instagram Account = ')
    month = input('Enter the "month of the year" reel has to be uploaded into your Instagram Account = ')
    year = input('Enter the "year" reel has to be uploaded into your Instagram Account = ')
    x = day+"/"+month+"/"+year
    return x

def datainput(accesstoken):
    at = accesstoken
    client_id = input('Enter Your Client Id: ')
    client_secret = input('Enter Your Client Secret: ')
    ll_at = get_long_lived_access_token(client_id,client_secret,at)
    username = input('Enter Username of your Instagram Account = ')
    id = instabID(ll_at)
    encryp_id = encrypt(id)
    insta_id = encryp_id
    reelname = input('Enter Name of the Reel which is to be Uploaded = ')
    caption = input('Enter Caption for the Reel = ')
    url = input('Enter the "URL" where the reel is stored = ')
    print('Enter the Date at which the reel has to be uploaded into your Instagram Account = ')
    date_full = date()

    conn = sqlite3.connect("Instadata.db")

    c = conn.cursor()
    c.execute("INSERT INTO instagramdata VALUES (?,?,?,?,?,?,?,?,?,?,?)",(at,client_id,client_secret,ll_at,username, insta_id, reelname, caption, url, date_full, 'to be executed'))
    c.execute("SELECT rowid,* FROM instagramdata ")

    items = c.fetchall()
    for item in items:
        print(item)

    print("created")
    conn.commit()
    conn.close()
accesstoken = input("Please Enter Your Access Token: ")

datainput(accesstoken)
'''
conn = sqlite3.connect("Instadata.db")
c = conn.cursor()
c.execute(" CREATE TABLE instagramdata(access_token text,client_id text, client_secret text, ll_accesstoken text, username text,encrypted_instagram_id text,reel_name text,caption text,url text,date text,status text)")'''






