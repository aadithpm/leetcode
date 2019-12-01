class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = {}
        for id, score in items:
            if id not in students:
                students[id] = [score]
            else:
                students[id].append(score)
        return [[student, sum(sorted(scores, reverse = True)[:5]) // 5] for student, scores in students.items()]
