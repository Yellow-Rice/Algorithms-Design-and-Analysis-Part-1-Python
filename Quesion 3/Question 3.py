import random
import re

MAX = 2 ** 16 - 1
NUM_OF_NODES = 200
NUM_OF_REPEAT = 1000#NUM_OF_NODES * NUM_OF_NODES * 8
TOTAL_NUM_OF_EDGES = 0
NUM_OF_EDGES = [0] * NUM_OF_NODES
ADJACENCY_MATRIX = [[0 for column in range(NUM_OF_NODES)] for row in range(NUM_OF_NODES)]

input_file = open("kargerMinCut.txt")
for each_line in input_file:
    array = re.split('[ \t\n\r]', each_line.strip())
    vertex1 = int(array[0]) - 1
    for i in range(1, len(array)):
        vertex2 = int(array[i]) - 1
        ADJACENCY_MATRIX[vertex1][vertex2] += 1
        NUM_OF_EDGES[vertex1] += 1
    if ADJACENCY_MATRIX[vertex1][vertex1] > 0:
        NUM_OF_EDGES -= ADJACENCY_MATRIX[vertex1][vertex1]
        ADJACENCY_MATRIX[vertex1][vertex1] = 0
    TOTAL_NUM_OF_EDGES += NUM_OF_EDGES[vertex1]
input_file.close()
TOTAL_NUM_OF_EDGES //= 2;


def karger_minimum_cut():
    if NUM_OF_NODES < 2:
        return 0
    current_minimum = MAX
    #counter = 1
    for i in range(NUM_OF_REPEAT):
        current_cut = randomized_contraction()
        if current_cut < current_minimum:
            current_minimum = current_cut
            #counter = 1
            #print("iteration:", i, "current_minimum:", current_minimum, "counter:", counter, sep = '\t')
        #elif current_cut == current_minimum:
            #counter += 1
            #print("iteration:", i, "current_minimum:", current_minimum, "counter:", counter, sep = '\t')
    return current_minimum


def randomized_contraction():
    total_num_of_edges = TOTAL_NUM_OF_EDGES
    num_of_edges = NUM_OF_EDGES[:]
    adjacency_matrix = [ADJACENCY_MATRIX[i][:] for i in range(NUM_OF_NODES)]
    
    for num_of_nodes in range(NUM_OF_NODES, 2, -1):
        edge = random.randint(1, total_num_of_edges)
        vertex1 = vertex2 = 0
        while edge > num_of_edges[vertex1]:
            edge -= num_of_edges[vertex1]
            vertex1 += 1;
        while edge > adjacency_matrix[vertex1][vertex2]:
            edge -= adjacency_matrix[vertex1][vertex2]
            vertex2 += 1
        total_num_of_edges -= adjacency_matrix[vertex1][vertex2]
        num_of_edges[vertex1] += num_of_edges[vertex2] - 2 * adjacency_matrix[vertex1][vertex2]
        adjacency_matrix[vertex1][vertex2] =adjacency_matrix[vertex2][vertex1] = 0
        num_of_edges[vertex2] = 0
        for i in range(0, NUM_OF_NODES):
            if adjacency_matrix[vertex2][i] > 0:
                adjacency_matrix[vertex1][i] += adjacency_matrix[vertex2][i]
                adjacency_matrix[i][vertex1] = adjacency_matrix[vertex1][i]
                adjacency_matrix[vertex2][i] = adjacency_matrix[i][vertex2] = 0
    return total_num_of_edges


print(karger_minimum_cut())