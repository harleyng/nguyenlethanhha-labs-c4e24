import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()

customers_collection = db["customers"]

event = customers_collection.count_documents({"ref": "events"})
wom = customers_collection.count_documents({"ref": "wom"})
ads = customers_collection.count_documents({"ref": "ads"})

customers_refs_counts = [event, wom, ads]
customers_refs_types = ["Events", "Wom", "Ads"]

pyplot.pie(customers_refs_counts, labels=customers_refs_types, autopct="%.1f%%", explode=[0, 0.1, 0])
pyplot.title("REFERENCES")
pyplot.axis("equal")

pyplot.show()


    

