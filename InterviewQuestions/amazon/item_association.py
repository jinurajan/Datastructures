# RETURN AN EMPTY LIST IF NO ITEM ASSOCIATION IS GIVEN

def largestItemAssociation(itemAssociation):
    # WRITE YOUR CODE HERE
    if not itemAssociation:
        return []
    associations = {}
    largest_association = []
    max_key = None
    no_association = 1
    for item in itemAssociation:
        if len(item) < 2:
            continue
        item1, item2 = item[0], item[1]
        if max_key is None:
            max_key = item1
        if item1 not in associations:
            associations[item1] = [item2]
        else:
            associations[item1].append(item2)
        if item2 not in associations:
            associations[item2] = [item1]
        else:
            associations[item2].append(item1)
        # print associations
        if len(associations[item1]) > no_association:
            max_key = item1
            no_association = len(associations[item1])
        elif len(associations[item1]) > no_association:
            max_key = item2
            no_association = len(associations[item1])
    largest_association = associations[max_key]
    largest_association.append(max_key)
    return sorted(largest_association)




print largestItemAssociation([])
print largestItemAssociation([[1], [2,3]])
print largestItemAssociation([['item1','item2'], ['item3','item4']])
print largestItemAssociation([['item1','item2'], ['item3', 'item4'], ['item4','item5']])