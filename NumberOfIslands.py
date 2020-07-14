'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

class Solution(object):
    def islandCount(self, grid, i, j):
        if(i<0 or i>= len(grid) or j < 0 or j>= len(grid[i]) or grid[i][j] == '0'):
            return 0
        
        grid[i][j] = '0'
        
        self.islandCount(grid, i+1, j)
        self.islandCount(grid, i-1, j)
        self.islandCount(grid, i, j+1)
        self.islandCount(grid, i, j-1)
        
        return 1
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        
        noOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    noOfIslands = noOfIslands + self.islandCount(grid, i, j)
        return noOfIslands
        
    
