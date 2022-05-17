import pandas as pd
from tqdm import tqdm

gen = iter(pd.read_json("/Users/owlus/Downloads/RC_2019-10.json", orient='records', lines=True, chunksize=1000000))

reddit_info = None
counts = dict()
for i in tqdm(range(145)) :
    data = next(gen)
    data = data[["author_fullname", "subreddit_id"]].groupby("subreddit_id")
    subrs = list(data.groups.keys())
    for subr in subrs :
        if not (subr in counts) :
            counts[subr] = dict()
        curCounts = data.get_group(subr).groupby("author_fullname").size().to_dict()
        for author, sz in curCounts.items() :
            if not (author in counts[subr]) :
                counts[subr][author] = 0
            counts[subr][author] += sz

with open("subr_stats_19_10.json", "w") as f :
    json.dump(counts, f)
