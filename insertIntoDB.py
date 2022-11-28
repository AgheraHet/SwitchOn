import pymongo
import os
import time
import numpy as np
import datetime

random_no = np.random.randint(1,101,size=10)
print(random_no)

client = pymongo.MongoClient()
DB = client["SwitchOn"]
Collection = DB["Stock_Status"]



diractory = "pics"
img_list = sorted(os.listdir(diractory), key=lambda x: int(x.split('.')[0]))
for i in img_list:
    unit_id = i[:-4]
    ct = datetime.datetime.now()
    ts = ct.timestamp()
    sku_id = "Unit_"+str(i[:-4])+"_"+str(ts)[:-3]
    status = "Good"
    if (int(i[:-4]) in random_no):
        status = "Bad"
    query = {"SKU_id": sku_id,"Unit_id": unit_id,"Status":status}
    Collection.insert_one(query)
    time.sleep(0.3)
