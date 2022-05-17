import json
import tqdm

data = open("subr_stats_c++_19_10.txt", "r").readlines()

user_sets1 = dict()

print("getting data 19.10")
for i in tqdm.tqdm(range(len(data))) :
    line = data[i]
    line, cnt = line.rsplit(sep=':', maxsplit=1)
    user, subr = line.rsplit(sep='$', maxsplit=1)
    cnt = int(cnt)
    if cnt > 10 :
        if not (subr in user_sets1) :
            user_sets1[subr] = dict()
        user_sets1[subr][user] = cnt

data = open("subr_stats_c++_19_12.txt", "r").readlines()
user_sets = dict()
cnts = dict()
print("getting data 19.12")
for i in tqdm.tqdm(range(len(data))) :
    line = data[i]
    line, cnt = line.rsplit(sep=':', maxsplit=1)
    user, subr = line.rsplit(sep='$', maxsplit=1)
    cnt = int(cnt)
    if cnt > 10 and (subr in user_sets1) and (user in user_sets1[subr]) :
        if not (subr in user_sets) :
            user_sets[subr] = set()
            cnts[subr] = 0
        user_sets[subr].add(user)
        cnts[subr] += cnt + user_sets1[subr][user]

proposed_subrs = []
for subr in user_sets.keys() :
    if cnts[subr] >= 2000:
        proposed_subrs.append(subr)

print(len(proposed_subrs))

with open("proposed_subrs_2.json", "w") as f :
    json.dump(proposed_subrs, f)




subrMatr = []
pbar = tqdm.tqdm(total=len(proposed_subrs)**2)
for subr1 in proposed_subrs :
    subrMatr.append([])
    for subr2 in proposed_subrs :
        jc_val = float(len(user_sets[subr1] & user_sets[subr2])) / float(len(user_sets[subr1] | user_sets[subr2]))
        subrMatr[-1].append(jc_val)
        pbar.update(1)

pbar.close()

with open("subr_matr_2.json", "w") as f :
    json.dump(subrMatr, f)