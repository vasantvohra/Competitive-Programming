import heapq
from numpy import *
class Solution:
    def Waterstoredinplatform(self, heightMap):
        if not heightMap or not heightMap[0]:
          return 0
        #initialize
        rows, cols = len(heightMap), len(heightMap[0])
        #print(len(heightMap))
        visited = set()
        stack = [] #heap
        #push border blocks into heap
        for i in range(rows):
          for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
              heapq.heappush(stack, (heightMap[i][j], i, j))
              visited.add((i, j))
           
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)] #directions
        result=[] 
        res = 0 #result
        print(len(heightMap))
        while stack:
            
        #taking the minimum i.e. lowest checking 4 neighbors and pushing back to heap
          h, i, j = heapq.heappop(stack) #h= height

          for d in dirs:
            _i, _j = i + d[0], j + d[1]
            if not -1 < _i < rows or not -1 < _j < cols or (_i, _j) in visited:
            #if 0<=_i<rows and 0<=_j<cols and not visited :
              continue
            h1=heightMap[_i][_j]
            res += max(0, h - h1) #difference
            heapq.heappush(stack, (max(h, heightMap[_i][_j]), _i, _j))
            visited.add((_i, _j)) #update visited block
            result.append(res)
            #print(result)
        
        return result
#def matrix():
    #n,m=input().split()
    #loop row n col
    # for i in range(row):
        #for j in range(col):
            #l[i][j]=input()

def run():
    f=[]
    #t=int(input("testcase"))
    n=int(input()) #enter number of rows
    l=[]
    while n:
        f=list(map(int,input().split(" ")))
        l.append(f)
        p=array(mat(l))
        n-=1
        c=Solution()
        volume=c.Waterstoredinplatform(l)
    print("Matrix:")
    print(p)
    return(volume)
if __name__=='__main__':
    volume=run()
    print("Water retention:",volume[-1],"units")

    '''
    example for input
    rows: 3
    then, Enter matrix as
    2 2 2
    2 1 2
    2 2 2

    '''

