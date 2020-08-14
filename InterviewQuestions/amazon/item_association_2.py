"""
given a list of associations find out the largest association group

eg: [[1,2], [3,4], [4,5]]

largest association group would be [3,4,5] since all 3 are associated.

"""

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
        if len(item) <= 1:
            continue
        for i in range(len(item)):
            if item[i] not in associations:
                associations[item[i]] = item[i+1:]
            else:
                associations[item[i]].extend(item[i+1:])
    print associations



print largestItemAssociation([])
print largestItemAssociation([[1], [2,3], [2,3,4]])
print largestItemAssociation([['item1','item2'], ['item3','item4']])
print largestItemAssociation([['item1','item2'], ['item3', 'item4'], ['item4','item5']])