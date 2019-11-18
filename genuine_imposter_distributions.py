import pymongo
import seaborn as sns

client = pymongo.MongoClient(host='localhost', port=26025)
db = client.biometrics

collection_same = db.distribution_same
collection_diff = db.distribution_diff

result1 = collection_same.find()
distribution_same_dict1 = result1[0]
distribution_same_arr = distribution_same_dict1['distribution_same_arr']
print(distribution_same_arr)

result1 = collection_diff.find()
distribution_diff_dict1 = result1[0]
distribution_diff_arr = distribution_diff_dict1['distribution_diff_arr']
print(distribution_diff_arr)

sns.set(color_codes=True)

sns.distplot(distribution_same_arr, bins=5, hist=True, rug=True)
sns.distplot(distribution_diff_arr, bins=5, hist=True, rug=True)


