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