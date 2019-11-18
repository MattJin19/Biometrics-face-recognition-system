import socket;
from PythonSDK.facepp import API
api = API()
socket.setdefaulttimeout(60)
import pymongo
client = pymongo.MongoClient(host='localhost', port=26025)
db = client.biometrics

collection = db.gallery
result1 = collection.find()
gallery = result1[0]
print(gallery)

print("++++++++++++++++++++++++++++")

collection = db.probe
result1 = collection.find()
probe = result1[0]
print(probe)

distribution_same_arr = []
distribution_diff_arr = []

CMC_predict_arrList = []
CMC_test_arrList = []

for i in range(90004, 90063, 2):
    CMC_predict_arr = []
    CMC_test_arr = []
    probe_face_token = probe[str(i)]
    print(str(i)+"::::::"+probe_face_token)
    for j in range(90004, 90063, 2):
        gallery_face_token = gallery[str(j)]
        print(str(j)+"***"+gallery_face_token)
        compare_res = api.compare(face_token1=probe_face_token, face_token2=gallery_face_token)
        confidence = compare_res['confidence']
        print(confidence)
        if i == j:
            distribution_same_arr.append(confidence)
            CMC_test_arr.append(1)
            CMC_predict_arr.append(confidence)
        else:
            distribution_diff_arr.append(confidence)
            CMC_test_arr.append(0)
            CMC_predict_arr.append(confidence)
    print(CMC_test_arr)
    print(CMC_predict_arr)
    CMC_test_arrList.append(CMC_test_arr)
    CMC_predict_arrList.append(CMC_predict_arr)

print("CMC_test_arrList", CMC_test_arrList)
print("CMC_predict_arrList", CMC_predict_arrList)
print("distribution_same_arr", distribution_same_arr)
print("distribution_diff_arr", distribution_diff_arr)

distribution_same_dict = {"distribution_same_arr": distribution_same_arr}
print(distribution_same_dict)

distribution_diff_dict = {"distribution_diff_arr": distribution_diff_arr}
print(distribution_diff_dict)

collection_same = db.distribution_same
result = collection_same.insert_one(distribution_same_dict)

collection_diff = db.distribution_diff
result = collection_diff.insert_one(distribution_diff_dict)


CMC_test_dict = {"CMC_test_arrList": CMC_test_arrList}
print("CMC_test_dict", CMC_test_dict)

CMC_predict_dict = {"CMC_predict_arrList": CMC_predict_arrList}
print("CMC_predict_dict", CMC_predict_dict)

collection_test = db.CMC_test
result = collection_test.insert_one(CMC_test_dict)

collection_predict = db.CMC_predict
result = collection_predict.insert_one(CMC_predict_dict)



