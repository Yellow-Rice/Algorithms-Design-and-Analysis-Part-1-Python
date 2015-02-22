import re
import sys

MAX = 875714
sys.setrecursionlimit(MAX)
adjacent_list = [[] for i in range(MAX)]
reversed_adjacent_list = [[] for i in range(MAX)]
finish_time = [-1 for i in range(MAX)]
current_source = -1
current_time = 0
counter = 0
leaders = [-1 for i in range(MAX)]
max_scc = [0] * 5

def dfs_loop_1():
    global current_source
    for each_vertex in range(MAX):
        if leaders[each_vertex] < 0:
            current_source = each_vertex
            dfs_1(each_vertex)

def dfs_1(vertex):
    global current_time
    leaders[vertex] = current_source
    for each_vertex in reversed_adjacent_list[vertex]:
        if leaders[each_vertex] < 0:
            dfs_1(each_vertex)
    finish_time[current_time] = vertex;
    current_time += 1;

def dfs_loop_2():
    global current_source
    global counter
    finish_time.reverse()
    for each_vertex in finish_time:
        if leaders[each_vertex] < 0:
            current_source = each_vertex
            counter = 0
            dfs_2(each_vertex)
            if counter > max_scc[4]:
                max_scc[4] = counter
                max_scc.sort(reverse = True)

def dfs_2(vertex):
    global counter
    leaders[vertex] = current_source
    counter += 1
    for each_vertex in adjacent_list[vertex]:
        if leaders[each_vertex] < 0:
            dfs_2(each_vertex)

input_file = open("SCC.txt")
for each_line in input_file:
    vertex1, vertex2 = re.split('[ \t\n\r]', each_line.strip())
    vertex1 = int(vertex1) - 1
    vertex2 = int(vertex2) - 1
    reversed_adjacent_list[vertex2].append(vertex1)
input_file.close()
dfs_loop_1()
del reversed_adjacent_list
input_file = open("SCC.txt")
for each_line in input_file:
    vertex1, vertex2 = re.split('[ \t\n\r]', each_line.strip())
    vertex1 = int(vertex1) - 1
    vertex2 = int(vertex2) - 1
    adjacent_list[vertex1].append(vertex2)
input_file.close()
leaders = [-1 for i in range(MAX)]
dfs_loop_2()
print(max_scc)