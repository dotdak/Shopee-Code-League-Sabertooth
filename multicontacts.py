import json
from collections import defaultdict
import time
import uuid

# Load data
with open('contacts.json') as f:
    data = json.load(f)

start_time = time.time()

# Prepare
email_refs = []
phone_refs = []
order_refs = []

for idx, val in enumerate(data):
    if (val['Email'] != ''):
        email_refs.append((val['Email'], idx))

    if (val['Phone'] != ''):
        phone_refs.append((val['Phone'], idx))

    if (val['OrderId'] != ''):
        order_refs.append((val['OrderId'], idx))

email_refs.sort(key=lambda tup: tup[0])
phone_refs.sort(key=lambda tup: tup[0])
order_refs.sort(key=lambda tup: tup[0])

# Process
union_sets = {}

def joinSet(data, union_sets, set1_id, set2_id):
    set1 = union_sets[set1_id]
    set2 = union_sets[set2_id]
    
    newSet = set1.union(set2)
    newSetId = str(uuid.uuid4())
    union_sets[newSetId] = newSet

    for idx in newSet:
        data[idx]['set_id'] = newSetId

    del union_sets[set1_id]
    del union_sets[set2_id]


def loopCheck(data, refs):
    for idx, current in enumerate(refs):
        if (idx > 0):
            prev = refs[idx - 1]
            if (current[0] == prev[0]):
                current_src = data[current[1]]
                prev_src = data[prev[1]]
                if (not ('set_id' in current_src)):
                    current_src['set_id'] = prev_src['set_id']
                    union_sets[current_src['set_id']].add(current[1])
                else:
                    # Join set
                    prev_old_set_id = prev_src['set_id']
                    joinSet(data, union_sets, current_src['set_id'], prev_src['set_id'])

                continue
        if (not ('set_id' in data[current[1]])):
            # Init new set
            set_id = str(uuid.uuid4())
            union_sets[set_id] = set([current[1]])
            data[current[1]]['set_id'] = set_id

loopCheck(data, email_refs)
loopCheck(data, phone_refs)
loopCheck(data, order_refs)
print(union_sets.values())

print("--- %s seconds ---" % (time.time() - start_time))