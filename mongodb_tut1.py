from pymongo import MongoClient

db = MongoClient('mongodb://143.215.138.132:27017')['big_data']

sample = {'$sample': {'size': 3}}

pipeline = [sample]

query_result = db.tweet.aggregate(pipeline)

for tweet in query_result:
    print tweet['text']
