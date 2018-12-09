from pymongo import MongoClient

uri = "mongodb://admin1:pipjyr-gEsrix-sogdo4@ds215633.mlab.com:15633/c4e24-lab1"
client = MongoClient(uri)

db = client.get_database()

account_collection = db["accounts"]
for account in account_collection.find():
    print(account)

# new_document = {
#     "username": "Thanh",
#     "email": "hihihi@gmail.com",
#     "phone": "238945335",
#     "password": "ijfsdkf34s",
#     "yob": "1995"
# }

# post_collection.insert_one(new_document)


# Use list[dict] 
    # for i in range (len(new_document)):
    #     account_collection.insert_one(new_document[i])

    # for acc in new_document:
    #     print(acc)

client.close()