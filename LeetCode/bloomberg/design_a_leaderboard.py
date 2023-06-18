"""
Design A Leaderboard

Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.
"""

from collections import defaultdict
from copy import deepcopy
from heapq import *


from heapq import *


class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score
        

    def top(self, K: int) -> int:
        min_heap = []
        for score in self.scores.values():
            heappush(min_heap, score)
            if len(min_heap) > K:
                heappop(min_heap)
        result = 0
        while K:
            result += heappop(min_heap)
            K-= 1
        return result

        

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)



class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)
        self.max_heap = []

    def addScore(self, playerId: int, score: int) -> None:
        curr_score = self.scores[playerId]
        self.scores[playerId] = curr_score+score
        self._delete_from_max_heap(playerId)
        heappush(self.max_heap, (-(curr_score+score), playerId))
        

    def top(self, K: int) -> int:
        max_heap_copy = deepcopy(self.max_heap)
        score = 0
        while K:
            curr_score, player = heappop(max_heap_copy)
            score += -curr_score
            K -= 1
        return score
    
    def _delete_from_max_heap(self, playerId):
        for idx, value in enumerate(self.max_heap):
            if value[1] == playerId:
                self.max_heap.pop(idx)
        heapify(self.max_heap)
        
    
    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        self._delete_from_max_heap(playerId)
        