# python -m pip install "pymongo[srv]"
""" from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://fariasgastondavid:Bi3KxdMRfywdAzaZ@mongodb-base.8cqh7nc.mongodb.net/?retryWrites=true&w=majority&appName=mongodb-base"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e) """

# 9nnex1Th86TRS8jcFFg4BLdusryYDoVi3xdIiF3jWGxhsgR3EjtjHmVHqDLHg7Wi

import requests
import json
url = "https://sa-east-1.aws.data.mongodb-api.com/app/data-wzene/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "listingsAndReviews",
    "database": "sample_airbnb",
    "dataSource": "mongodb-base",
    "projection": {
        "_id": 10006546
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': '9nnex1Th86TRS8jcFFg4BLdusryYDoVi3xdIiF3jWGxhsgR3EjtjHmVHqDLHg7Wi',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
