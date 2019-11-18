import socket
# import PythonSDK
from PythonSDK.facepp import API,File
api = API()

socket.setdefaulttimeout(60)

dict = {}

for i in range(90004, 90063, 2):
    image_file_detect = './gallery_compress_final/'+str(i)+'.jpg'
    res = api.detect(image_file = File(image_file_detect), return_attributes="none")
    dict[str(i)] = res.faces[0].face_token;

print(dict)

import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.biometrics
collection = db.gallery

result = collection.insert_one(dict)
print(result)
result1 = collection.find()
result2 = result1[0]
print(result1)
print(result2)
