from pymongo import MongoClient

#1. Connect to database server
uri = "mongodb://admin1:pipjyr-gEsrix-sogdo4@ds215633.mlab.com:15633/c4e24-lab1"
client = MongoClient(uri)

#2. Select database
db = client.get_database()

#3. Select collection
post_collection = db["posts"]
for post in post_collection.find():
    print(post)
# #4. Create document
# new_document = {
#     "title": "Hôm nay tuyển VN thắng",
#     "post": "Mình vẫn ở nhà ... Láo, tao đi bão",
# }
 

# #5. Add document into collection
# post_collection.insert_one(new_document)

#6. Close connecttion
client.close()