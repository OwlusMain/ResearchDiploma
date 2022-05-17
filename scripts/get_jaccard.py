import json
import tqdm

data = json.loads(open("subr_stats2.json", "r").read())

proposed_subrs = []
user_sets = dict()

print("getting data")
for subr, users in data.items() :
    user_sets[subr] = set()
    for user, cnt in users.items() :
        if int(cnt) > 10 :
            user_sets[subr].add(user)
    
    if len(user_sets[subr]) == 0 :
        user_sets.pop(subr)

cnts = [len(x) for x in list(user_sets.values())]
cnts = sorted(cnts)[::-1]
for subr, users in user_sets.items() :
    if len(comments) >=  5000:
        proposed_subrs.append(subr)

with open("proposed_subrs.json", "w") as f :
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

with open("subr_matr.json", "w") as f :
    json.dump(subrMatr, f)