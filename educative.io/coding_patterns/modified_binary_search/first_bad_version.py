"""
The latest version of a software product fails the quality check. Since each version is developed upon the previous one, all the versions created after a bad version are also considered bad.

Suppose you have  n  versions with the IDs [1,2,3,.....n] and you have access to an API function that returns TRUE if the argument is the ID of a bad version.

Your task is to find the first bad version, which is causing all the later ones to be bad. You have to implement a solution with the minimum number of API calls.
"""


from api import *

version_api = api(0)

def is_bad_version(v):
    return version_api.is_bad(v)

def first_bad_version(n):
# -- DO NOT CHANGE THIS SECTION
    version_api.n = n
# -- 
    low = 1
    high = n
    first_bad_version = n
    call_count = 0
    while low < high:
        mid = (low + high) // 2
        call_count += 1
        if is_bad_version(mid):
            first_bad_version = min(first_bad_version, mid)
            high = mid
        else:
            low = mid+1

    return first_bad_version, call_count    


# Driver code
def main():
    global v
    test_case_versions = [38, 13, 29, 40, 23]
    first_bad_versions = [28, 10, 10, 28, 19]

    for i in range(len(test_case_versions)):
        v = first_bad_versions[i]
        if i > 0:
            print()
        print(i + 1,  ".\tNumber of versions: ", test_case_versions[i], sep="")
        result = first_bad_version(test_case_versions[i])
        print("\n\tFirst bad version: ",
              result[0], ". Found in ", result[1], " API calls.", sep="")
        print("-"*100)


if __name__ == '__main__':
    main()
