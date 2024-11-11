class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 'L':
                return
            
            grid[r][c] = 'V'
            
            dfs(r + 1, c)  
            dfs(r - 1, c)  
            dfs(r, c + 1)  
            dfs(r, c - 1)  

        
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == 'L':
                    dfs(i, j)  
                    island_count += 1  

        return island_count


solution = Solution()

# Dispatch 1
map1 = [
    ["L", "L", "L", "L", "W"],
    ["L", "L", "W", "L", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"]
]
print(solution.getTotalIsles(map1))  # Expected Output: 1

# Dispatch 2
map2 = [
    ["L", "L", "W", "W", "W"],
    ["L", "L", "W", "W", "W"],
    ["W", "W", "L", "W", "W"],
    ["W", "W", "W", "L", "L"]
]
print(solution.getTotalIsles(map2))  # Expected Output: 3
