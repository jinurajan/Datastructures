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
    largest_associations = []
    no_association = 1
    for item in itemAssociation:
        if len(item) == 0:
            continue
        if len(item) == 1:
            item1 = item[0]
            if item1 not in associations:
                associations[item1] = [item1]
            if len(associations[item1]) > no_association:
                no_association = len(associations[item1])
        else:
            item1, item2 = item[0], item[1]
            if item1 not in associations:
                associations[item1] = [item2]
            else:
                associations[item1].append(item2)
            if item2 not in associations:
                associations[item2] = [item1]
            else:
                associations[item2].append(item1)
            if len(associations[item1]) > no_association:
                no_association = len(associations[item1])
            elif len(associations[item1]) > no_association:
                no_association = len(associations[item1])
    for key, value in associations.items():
        if len(value) == no_association:
            largest_associations.append(sorted([key] + value))
    print largest_associations
    largest_associations = sorted(largest_associations, key=lambda x: x[0])
    return largest_associations[0]




# print largestItemAssociation([])
# print largestItemAssociation([[1], [2,3]])
print largestItemAssociation([['item1','item2'], ['item3','item4']])
# print largestItemAssociation([['item1','item2'], ['item3', 'item4'], ['item4','item5']])
print largestItemAssociation([['I1', 'I2'], ['I5', 'I6'], ['I3', 'I4'], ['I7', 'I8'], ['I4', 'I5'], ['I2', 'I10']])