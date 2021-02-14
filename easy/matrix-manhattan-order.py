# https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        coords = [[r, c] for r in range(R) for c in range(C)]
        coords.sort(key=lambda k: abs(k[0]-r0) + abs(k[1]-c0))
        return coords