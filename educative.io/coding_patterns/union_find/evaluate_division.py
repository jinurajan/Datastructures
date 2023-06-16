"""
You are given an array of variable pairs equations and an array of real numbers, values, where the equations[i] = [A[i], B[i]] and values[i] represent the equation values[i] = A[i] / B[i]

Each A[i] or B[i] is a string that represents a single variable.

You are also given some queries, where queries[j] = [C[j], D[j]] represents the jth query where you must find the answer for C[j] / D[j].

Return the answers to all queries. If any single answer cannot be determined, return -1.0

"""

class UnionFind:
    # Constructor
    def __init__(self):
        self.parent = {}

    # Function to find which subset a particular element belongs.
    def find(self, i):
        if i not in self.parent:
            self.parent[i] = (i, 1)
        group_id, weight = self.parent[i]

        if group_id != i:
            new_group_id, group_weight = self.find(group_id)
            self.parent[i] = (new_group_id, weight*group_weight)
        return self.parent[i]

    # Function to join two subsets into a single subset.
    def union(self, dividend, divisor, value):
        dividend_root, dividend_wt = self.find(dividend)
        divisor_root, divisor_wt = self.find(divisor)
        if dividend_root != divisor_root:
            self.parent[dividend_root] = (divisor_root, divisor_wt*value / dividend_wt)

def evaluate_equations(equations, values, queries):
    union_find = UnionFind()

    for (dividend, divisor),value in zip(equations, values):
        union_find.union(dividend, divisor, value)
    
    results = []
    for (dividend, divisor) in queries:
        if dividend not in union_find.parent or divisor not in union_find.parent:
            results.append(-1.0)
        else:
            dividend_root, dividend_wt = union_find.find(dividend)
            divisor_root, divisor_wt = union_find.find(divisor)
            if dividend_root != divisor_root:
                results.append(-1.0)
            else:
                results.append(dividend_wt/divisor_wt)
    return results
