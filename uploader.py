import datetime
import sqlite3
import time
import requests
from cryptography.fernet import Fernet
import json

def decrypter(insta_business_id):
    def load_key():
        file = open("key" + ".key", "rb")
        key = file.read()
        file.close()
        return key

    key = load_key()
    fer = Fernet(key)
    decrpyted = fer.decrypt(insta_business_id.encode()).decode()
    '''print(decrpyted)'''

    return decrpyted



def publish(business_acc_id,accesstoken,reel_id):
    url = "https://graph.facebook.com/v16.0/"+business_acc_id+"/media_publish"
    params = {
        "creation_id": reel_id,

        "access_token": accesstoken,

    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        print("New Reel Uploaded successfully!")
        conn = sqlite3.connect("Instadata.db")

        c = conn.cursor()
        c.execute("UPDATE instagramdata SET status ='Successful' WHERE rowid = (?) ", (id))
        conn.commit()
    else:
        print("Error creating new Reel:", response.json()["error"]["message"])
        conn = sqlite3.connect("Instadata.db")

        c = conn.cursor()
        c.execute("UPDATE instagramdata SET status ='Failed' WHERE rowid = (?) ", (id))
        conn.commit()


def get_media_status(media_id, accesstoken):
    url = "https://graph.facebook.com/v16.0/" + media_id +"?fields=status_code,status&access_token=" +accesstoken
    '''params = {
        "fields": 'status_code,status',
        "access_token": str(accesstoken)

    }'''
    response = requests.get(url)
    data = response.json()['status_code']

    return data

def upload_reel(accesstoken,id):
    def get_business_id(id):
        conn = sqlite3.connect("Instadata.db")
        c = conn.cursor()
        c.execute("SELECT encrypted_instagram_id FROM instagramdata WHERE rowid = (?) ",(id))
        insta_business_id = str(c.fetchall())
        decrypted_id = decrypter(insta_business_id)
        return decrypted_id
    '''print(decrypted_id)'''
    def geturl(id):
        conn = sqlite3.connect("Instadata.db")
        c = conn.cursor()
        urlds = [job[0] for job in c.execute("SELECT url FROM instagramdata WHERE rowid = (?) ",(id))]
        '''print(type(urlds))'''
        urldse = ''
        for ur in urlds:
            urldse += ur
        '''print(urldse)'''

        return urldse
    def get_caption(id):
        conn = sqlite3.connect("Instadata.db")
        c = conn.cursor()
        caps = [job[0] for job in c.execute("SELECT caption FROM instagramdata WHERE rowid = (?) ", (id))]
        captions = ''
        for cap in caps:
            captions += cap
        '''print(captions)'''

        return captions



    reel_url = geturl(id)
    decrpyted_id = get_business_id(id)
    caption = get_caption(id)
    url = "https://graph.facebook.com/v16.0/" + decrpyted_id + "/media"
    params = {
        "media_type": "REELS",
        "share_to_feed": "false",
        "access_token": str(accesstoken),
        "video_url": reel_url,
        "caption": caption,

    }

    response = requests.post(url, data=params)
    if response.status_code == 200:
        '''print("New Reel created successfully!")
        print(response.content)'''
        '''json_data = json.loads(response.content)
        response_json_data_pretty = json.dumps(json_data, indent=4)
        reel_id = response_json_data_pretty'''
        reel_id = response.json()["id"]

        media_status = get_media_status(reel_id, accesstoken)
        while media_status != 'FINISHED' :
            media_status = get_media_status(reel_id,accesstoken)
            print(media_status)
            time.sleep(10)

        print(reel_id)
        publish(decrpyted_id,accesstoken,reel_id)


    else:
        print("Error creating new Reel:", response.json()["error"]["message"])
        conn = sqlite3.connect("Instadata.db")

        c = conn.cursor()
        c.execute("UPDATE instagramdata SET status ='Failed' WHERE rowid = (?) ", (id))
        conn.commit()


conn = sqlite3.connect("Instadata.db")

c = conn.cursor()
c.execute("SELECT date FROM instagramdata ")
items = c.fetchall()


def get_accesstoken(id):
    conn = sqlite3.connect("Instadata.db")
    c = conn.cursor()
    acts = [job[0] for job in c.execute("SELECT ll_accesstoken FROM instagramdata WHERE rowid = (?) ", (id))]
    actoken = ''
    for act in acts:
        actoken += act
    '''print(actoken)'''

    return actoken


for item in items:
    print(item)
    now = datetime.datetime.now()
    date_now = now.strftime("('%d/%m/20%y',)")
    print(date_now)
    if str(item) == date_now:

        c.execute("SELECT rowid FROM instagramdata WHERE date = (?) ",(item))
        ids = c.fetchall()
        for id in ids:
            print("Match")
            accesstoken = get_accesstoken(id)
            status = [job[0] for job in c.execute("SELECT status FROM instagramdata WHERE rowid = (?) ", (id))]
            stats = ''
            for stat in status:
                stats += stat
            print(stats)
            if stats != "Successful":
                upload_reel(accesstoken,id)
                '''print(id)'''
            else:
                continue

        break



    else:
        print("No Match")
        continue

conn.close()


