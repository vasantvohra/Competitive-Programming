# Competitve Programming
# Water retension -first Solution updated on github
<p align="center">
    <img src="https://github.com/vasantvohra/Competitive-Programming/blob/master/Water%20retention/problem%20statement.png?raw=true" alt="Questions"/>
</p>
<h1>How to execute </h1>

You can simply run "test cases.py" .,
it will execute the "waterplatform.py" output against the testcases given as text file "test0.txt".

You may run by making your own test case file file as format in one of the test case
or you can directly run  "waterplatform.py".

The approach used in solving this problem is given "approach.txt"

<h1>Min-Heap</h1>

I have used min Heap to solve this problem,
Priority queues & BFS , Depth first search (to find the lowest) could also be used but they would lead to more time consumption.
All the necessary working has been mentioned for easy understanding of function
<h1>
Approach</h1>

1. Initially the heap contains all cells on the perimeter of the map.

2. The first cell popped is the lowest point on the outer wall.

3. Checking the 4 neighbours, ignoring any already explored (in the heap or have already been popped off the heap) or outside the map.

4. If a newly discovered neighbour is lower than the current cell then water can be added on top of it.

5. We know the water cannot flow out anywhere because the current cell is the lowest.

6. Add the water to this neighbouring cell (zero if neighbour is higher than cell) and push neighbour  with its new height onto the heap.

7. We are effectively continually raising the water level, filling in any "holes" as we go.

<h2>Time complexity</h2>
<li>Every cell is pushed and popped from the heap, which is O(mn log(mn))

<h1>References</h1>
[1] <a href=https://leetcode.com/problems/trapping-rain-water/solution/> Leet Code </a> <br>
[2] <a href=https://www.spoj.com/problems/WATER/> SPOJ </a> <br>
[3] <b>Geeks for geeks:</b><i> Rain water trapping </i><br>




