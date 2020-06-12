# Logic - A ghost can always catch pacman if it is closer to or equidistant from the target position. We don't have to worry about chasing, only distance.

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        targetDist = abs(target[0]) + abs(target[1])
        for pos in ghosts:
            if abs(pos[0]-target[0]) + abs(pos[1]-target[1]) <= targetDist:
                return False
        return True