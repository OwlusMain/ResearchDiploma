import pandas as pd
from tqdm import tqdm

gen = iter(pd.read_json("/Users/owlus/Downloads/RC_2019-10.json", orient='records', lines=True, chunksize=1000000))

reddit_info = None
reddit_ids = set(list(json.loads(open("/Users/owlus/Desktop/RedditDumps/proposed_subrs.json", "r").read())))


for i in tqdm(range(1)) :
    data = next(gen)
    if type(reddit_info) == type(None) :
        reddit_info = data[["author_fullname", "id", "parent_id", "subreddit_id", "body"]]
    else :
        reddit_info = pd.concat([reddit_info, data[["author_fullname", "id", "parent_id", "subreddit_id", "body"]]], ignore_index=True)
reddit_info.to_csv("/Users/owlus/Desktop/reddit_dump_tiny.csv")

for i in range(3) :
    for j in tqdm(range(2 ** i)) :
        data = next(gen)
        reddit_info = pd.concat([reddit_info, data[["author_fullname", "id", "parent_id", "subreddit_id", "body"]]], ignore_index=True)
    
    reddit_info.to_csv("/Users/owlus/Desktop/reddit_dump_sz_" + str(i) + ".csv")