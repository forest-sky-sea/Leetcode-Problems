class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        for move in moves:
            if move == 'L':
                pos[0] -= 1
            elif move == 'R':
                pos[0] += 1
            elif move == 'U':
                pos[1] += 1
            elif move == 'D':
                pos[1] -= 1
        if pos == [0, 0]:
            return True
        else:
            return False


print(Solution().judgeCircle("UD"))
