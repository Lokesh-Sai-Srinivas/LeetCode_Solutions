"""
Problem: 1733 - Minimum Number of People to Teach  
Description: You are given an integer n representing the number of languages, a 2D array languages where languages[i] is the list of languages the i-th person knows, and a 2D array friendships where friendships[j] = [u, v] denotes a friendship between person u and person v. Two people can communicate if they share at least one common language. You may choose one language and teach it to some people so that all friends can communicate with each other. Return the minimum number of people you need to teach.  
Date: 2025-09-10  
"""

class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        lang_sets = [set(l) for l in languages]

        need_teach_users = set()
        for u, v in friendships:
            if lang_sets[u - 1].isdisjoint(lang_sets[v - 1]):
                need_teach_users.add(u)
                need_teach_users.add(v)

        min_teach = float("inf")
        for lang in range(1, n + 1):
            count = sum(1 for user in need_teach_users if lang not in lang_sets[user - 1])
            min_teach = min(min_teach, count)

        return min_teach
