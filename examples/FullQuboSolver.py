# This example shows using FullQuboSolver on small vrp tests.

import sys
sys.path.insert(1, '../src')

from vrp_solvers import FullQuboSolver
import DWaveSolvers
from input import *

if __name__ == '__main__':

    graph_path = '../graphs/small.csv'

    # Parameters for solve function.
    only_one_const = 10000000.
    order_const = 1.

    for t in ['small_graph1', 'small_graph2']:
        print("Test : ", t)

        # Reading problem from file.
        path = '../tests/vrp/' + t + '.test'
        problem = read_full_test(path, graph_path ,capacity = False)

        # Solving problem on FullQuboSolver.
        solver = FullQuboSolver(problem)
        solution = solver.solve(only_one_const, order_const, solver_type = 'cpu')

        # Checking if solution is correct.
        if solution == None or solution.check() == False:
            print("Solver hasn't find solution.\n")
            continue

        print("Solution : ", solution.solution) 
        print("Total cost : ", solution.total_cost())
        print("\n")
