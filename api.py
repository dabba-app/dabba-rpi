import requests
from pymongo import MongoClient

def getMongoClient():
    return MongoClient(host=os.environ['HOST'], port=int(os.environ['PORT']),
                       username=os.environ['USER'], password=os.environ['PASS']) #add params

def send_to_API(data):
    URL = "http://dabba.us-west-2.elasticbeanstalk.com/bins/"
    r = requests.post(URL, data)

def get_username(macID):
    client = getMongoClient()
    admin = client.admin
    posts = admin.posts
    username = posts.find_one({"U_ID": str(macID)})['USER_NAME']
    client.close()
    return username

def get_location(macID):
    client = getMongoClient()
    telegram_db = client.telegram_db
    posts = telegram_db.posts
    lat = posts.find_one({"U_ID": str(macID)})['LAT']
    lon = posts.find_one({"U_ID": str(macID)})['LON']
    client.close()
    return lat, lon

def get_type(macID):
    client = getMongoClient()
    telegram_db = client.telegram_db
    posts = telegram_db.posts
    bin_type = posts.find_one({"U_ID":str(macID)})['TYPE']
    client.close()
    return bin_type