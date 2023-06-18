"""
Reward Top K Students

You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.

Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.

You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student is unique.

Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.

"""
from typing import List
from heapq import *


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        max_heap = []
        for id, review in zip(student_id, report):
            score = 0
            for r in review.split(" "):
                if r in positive:
                    score += 3
                if r in negative:
                    score -= 1
            heappush(max_heap, (-score, id))

        result = []
        while k > 0:
            result.append(heappop(max_heap)[1])
            k -= 1
        return result    

positive_feedback = ["smart","brilliant","studious"]
negative_feedback = ["not"]
report = ["this student is studious","the student is smart"]
student_id = [1,2]
k = 2
print(Solution().topStudents(positive_feedback=positive_feedback, negative_feedback=negative_feedback, report=report, student_id=student_id, k=k))
positive_feedback = ["smart","brilliant","studious"]
negative_feedback = ["not"]
report = ["this student is not studious","the student is smart"]
student_id = [1,2]
k = 2
print(Solution().topStudents(positive_feedback=positive_feedback, negative_feedback=negative_feedback, report=report, student_id=student_id, k=k))


