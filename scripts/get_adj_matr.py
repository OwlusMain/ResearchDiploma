import pandas as pd
import json
import tqdm

dirs = ["19_09", "19_10", "19_11", "19_12", "20_01", "20_02", "20_03", "20_04"]

#getting users

counts = dict()
i = 0
pbar = tqdm.tqdm(total=8)
for curDir in dirs :
    data = pd.read_csv(curDir + "/reddit_dump_large.csv").groupby("subreddit_id")
    subrs = list(data.groups.keys())
    for subr in subrs :
        if not (subr in counts) :
            counts[subr] = dict()
        curCounts = data.get_group(subr).groupby("author_fullname").size().to_dict()
        for author, sz in curCounts.items() :
            if not (author in counts[subr]) :
                counts[subr][author] = dict()
            if not (curDir in counts[subr][author]) :
                counts[subr][author][curDir] = 0
            counts[subr][author][curDir] += sz
    i+=1
    pbar.update(1)
        
with open("subr_stats3.json", "w") as f :
    json.dump(counts, f)


