import re
import pymongo  
from pymongo import MongoClient



client = MongoClient("mongodb+srv://smita:smita@cluster0.ctqok1y.mongodb.net/")

db = client["ats_data"]
col = db["data"]


pattern = re.compile(r'(UTC_Time)=(\d+:\d+);(Speed)=(\d+);(UTC_Timestamp)=(\d+);')


def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

for line in (open("data.txt")):
    for match in re.finditer(pattern, line):
        utcTime, val, speed, val2, timestamp, val3 = match.groups()
        post1=[utcTime,val,speed,val2,timestamp,val3]
        post=Convert(post1)
        # print(post)
        col.insert_one(post)
       


