"""
In a Retail Inventory Management Alice went to buy products from an inventory in a retail mart. Each inventory has various products, all with varying weights. Alice decides to use a scooter that can pick up three products at a time. The products in each inventory are lined up in a single row, and Alice indexes them from 0 to n−1, starting from the first product to the n th product in the row. In each selection, Alice picks the lightest remaining product in the inventory with weight w and uses the scooper to pick up that product along with the two other products adjacent to it. Alice repeats this process until there are no more products left in the inventory. Alice wants to find the sum of the weights of the lightest products which can be chosen in every selection. Note: If there are two products with the lightest weight at different indexes, Alice chooses the product at the smallest index. If the product only has one other product adjacent to it, then the product itself and the single adjacent product will be removed. Example Let there be n=4 products in the inventory with weights represented by weights =[4,3,2,1]. First, choose the minimum weight (i.e., 1) and add that weight up to the total. The products with weights 2 and 1 are removed. The array of products is now [4,3]. - Then, choose the minimum weight from the remaining products (i.e., 3) and add that weight up to the total. The products with weights 3 and 4 are removed, and now there are no more products in the inventory. Hence, the total is 1+3=4. Function Description Complete the function findTotalWeight in the editor below. findTotalWeight has the following parameter: products: the array of integers denoting the weights of the products in the inventory Returns int: an integer denoting the sum of minimum weighted products at each selection. Constraints - 3≤w≤2000 - 3≤ length of products ≤2000 - 1≤ products [i]≤10

Another example would be [6,4,9,10,34,56,54] and output is 68. to explain it in a bit more detail 4 is the smallest weight, so we add 4 to thhe sum and remove it's adjacent numbers 6 and 9 from the list, in the next iteration we look at numbers 10, 34 and 10 is thhe smallest so we add 10 to the sum and remove 34 and next iteration we look at 56 and 54 and 54 is the smaller number so we add 54 to the sum and remove 56 so the total sum = 68



"""

import collections
def cartWeight(weights):
    items = [(val, idx) for idx, val in enumerate(weights)]
    items.sort()
    result = 0
    for val, idx in items:
        if weights[idx] == 0:
            continue
        result +=val
        if idx-1 >= 0 and weights[idx-1]:
            weights[idx-1] = 0
        if idx +1 < len(weights) and weights[idx+1]:
            weights[idx+1] = 0
    return result

print (cartWeight([4,3,2,1]))
print (cartWeight([6,4,9,10,34,56,54]))