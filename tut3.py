from pymongo import MongoClient

db = MongoClient('mongodb://143.215.138.132:27017')['big_data']

limit = {'$limit': 10000}

match = {'$match': {'author_name': '511 New York'}}

pipeline = [limit]

author_dict = {}
for tweet in db.tweet_subset.aggregate(pipeline):
    author = tweet['author_name']
    if author in author_dict:
        author_dict[author] += 1
    else:
        author_dict[author] = 1

print sorted(author_dict, key=lambda x:author_dict[x], reverse=True)[0]