from pprint import pformat
# import PythonSDK
from PythonSDK.facepp import API,File
import PythonSDK.ImagePro

def print_result(hit, result):
    print(hit)
    print('\n'.join("  " + i for i in pformat(result, width=75).split('\n')))

def printFuctionTitle(title):
    return "\n"+"-"*60+title+"-"*60;

api = API()
res = api.detect(image_url=detech_img_url, return_attributes="gender,age,smiling,headpose,facequality,"
                                                       "blur,eyestatus,emotion,ethnicity,beauty,"
                                                       "mouthstatus,skinstatus")
print_result(printFuctionTitle("face detection"), res)
compare_res = api.compare(image_file1=File(face_search_img), image_file2=File(face_search_img))
print_result("compare", compare_res)

# api.faceset.delete(outer_id='faceplusplus', check_empty=0)
# # 1.make a faceSet
ret = api.faceset.create(outer_id='faceplusplus')

faceResStr=""
res = api.detect(image_file=File(faceSet_img))
faceList = res["faces"]
for index in range(len(faceList)):
    if(index==0):
         faceResStr = faceResStr + faceList[index]["face_token"]
    else:
         faceResStr = faceResStr + ","+faceList[index]["face_token"]

api.faceset.addface(outer_id='faceplusplus', face_tokens=faceResStr)

search_result = api.search(image_file=File(face_search_img), outer_id='faceplusplus')
print_result('search', search_result)


