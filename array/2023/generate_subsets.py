from typing import List



def generate_subsets(array: List):
    result = []
    subset = []

    def search(n):
        print(f"called search with {n}")
        if n == len(array):
            result.append(subset[:])
            print(".........")
            return
        subset.append(array[n])
        search(n+1)
        print(f"returned value {n}")
        subset.pop()
        search(n+1)
    search(0)
    return result


array = [1,2,3]
print(generate_subsets(array))