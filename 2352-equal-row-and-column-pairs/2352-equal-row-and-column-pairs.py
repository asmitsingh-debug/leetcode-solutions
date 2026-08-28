class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic={}
        rows=len(grid)
        cols=len(grid[0])
        for row in grid:
            row=tuple(row)
            dic[row]= dic.get(row, 0) + 1
        count=0
        for i in range(rows):
            col = tuple(grid[j][i] for j in range(len(grid)))
            if col in dic:
                count+=dic[col]
        return count