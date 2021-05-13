"""
Analyze User Website Visit Pattern

We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.


Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation:
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.


Note:

3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.
It is guaranteed that there is at least one user who visited at least 3 websites.
No user visits two websites at the same time.
"""


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = [x for x in zip(username, timestamp, website)]
        data.sort(key=lambda x: (x[0], x[1]))
        hashmap = defaultdict(list)
        for x, y, z in data: hashmap[x].append(z)
        triplets, count, res = defaultdict(int), 0, None
        for x in hashmap:
            keys = set(combinations(hashmap[x], 3))
            print(keys)
            for y in keys:
                triplets[y] += 1
                if triplets[y] == count:
                    if not res or res > y:
                        res = y
                elif triplets[y] > count:
                    count = triplets[y]
                    res = y
            print(triplets)

        return res


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        pairs = sorted(zip(timestamp, website, username), key=lambda pair: pair[0])
        print(pairs)
        print("*********")
        um = collections.defaultdict(list)

        for i in range(len(pairs)):
            um[pairs[i][2]].append(pairs[i][1])
        print(um)
        fm = collections.defaultdict(int)

        freq = collections.defaultdict(int)

        max_seq = 0
        max_ans = ("zzzzzzzzzz", "zzzzzzzzzz", "zzzzzzzzzz")
        for user, sites in um.items():
            if len(sites) < 3:
                continue

            seen = set()

            for i in range(len(sites) - 2):
                for j in range(i + 1, len(sites) - 1):
                    for k in range(j + 1, len(sites)):
                        key = (sites[i], sites[j], sites[k])

                        if key not in seen:
                            seen.add(key)
                            freq[key] += 1

                            if freq[key] >= max_seq:
                                max_seq = freq[key]

        for k, v in freq.items():
            if v == max_seq:
                max_ans = min(max_ans, k)
        print("*********")
        print(freq)
        return max_ans