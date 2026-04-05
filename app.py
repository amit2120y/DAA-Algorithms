from flask import Flask, render_template, request, jsonify
import time
import traceback

# Import all algorithms
from algorithms.divide_conquer import merge_sort, quick_sort, binary_search, heap_sort, strassen_multiply
from algorithms.greedy import fractional_knapsack, activity_selection, kruskal_algorithm, prim_algorithm, optimal_merge_pattern
from algorithms.dynamic import fibonacci, knapsack_dp, lcs, matrix_chain_multiply, tsp_dp
from algorithms.backtracking import n_queens, naive_string_matching, rabin_karp, knuth_morris_pratt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_algorithm():
    try:
        data = request.json
        category = data.get('category')
        algorithm = data.get('algorithm')
        input_data = data.get('input')
        
        operations = 0
        start_time = time.time()
        result = None
        explanation = ""
        complexity = ""
        
        # Divide & Conquer Algorithms
        if category == 'divide':
            if algorithm == 'merge_sort':
                arr = list(map(int, input_data.split()))
                result = merge_sort(arr)
                complexity = "O(n log n)"
                operations = len(arr) * (1 + len(bin(len(arr))) - 2)
                explanation = "Divide and conquer approach: divide array in half, sort recursively, then merge"
                
            elif algorithm == 'quick_sort':
                arr = list(map(int, input_data.split()))
                result = quick_sort(arr)
                complexity = "O(n log n) average, O(n²) worst"
                operations = len(arr) * (1 + len(bin(len(arr))) - 2)
                explanation = "Partition-based sorting: select pivot, partition array, recursively sort subarrays"
                
            elif algorithm == 'binary_search':
                parts = input_data.split(',')
                arr = list(map(int, parts[0].split()))
                target = int(parts[1])
                result = binary_search(arr, target)
                complexity = "O(log n)"
                operations = len(bin(len(arr))) - 2
                explanation = f"Search for {target} in sorted array by repeatedly dividing search interval in half"
                
            elif algorithm == 'heap_sort':
                arr = list(map(int, input_data.split()))
                result = heap_sort(arr)
                complexity = "O(n log n)"
                operations = len(arr) * (1 + len(bin(len(arr))) - 2)
                explanation = "Build max heap, extract elements in order to sort array"
                
            elif algorithm == 'strassen':
                lines = input_data.strip().split('\n')
                A = [list(map(int, line.split())) for line in lines[:2]]
                B = [list(map(int, line.split())) for line in lines[2:]]
                result = strassen_multiply(A, B)
                complexity = "O(n^2.807)"
                operations = int(7 ** (len(bin(len(A))) - 2))
                explanation = "Recursive matrix multiplication using 7 multiplications instead of 8"
        
        # Greedy Algorithms
        elif category == 'greedy':
            if algorithm == 'fractional_knapsack':
                lines = input_data.strip().split('\n')
                values = list(map(int, lines[0].split()))
                weights = list(map(int, lines[1].split()))
                capacity = int(lines[2])
                result = fractional_knapsack(values, weights, capacity)
                complexity = "O(n log n)"
                operations = len(values) * (1 + len(bin(len(values))) - 2)
                explanation = "Greedy approach: sort items by value/weight ratio, fill knapsack in order"
                
            elif algorithm == 'activity_selection':
                lines = input_data.strip().split('\n')
                start = list(map(int, lines[0].split()))
                finish = list(map(int, lines[1].split()))
                result = activity_selection(start, finish)
                complexity = "O(n log n)"
                operations = len(start) * (1 + len(bin(len(start))) - 2)
                explanation = "Select maximum non-overlapping activities by sorting on finish time"
                
            elif algorithm == 'kruskal':
                lines = input_data.strip().split('\n')
                n = int(lines[0])
                edges = []
                for i in range(1, len(lines)):
                    u, v, w = map(int, lines[i].split())
                    edges.append((u, v, w))
                mst, cost = kruskal_algorithm(n, edges)
                result = {"mst": mst, "cost": cost}
                complexity = "O(E log E)"
                operations = len(edges) * (1 + len(bin(len(edges))) - 2)
                explanation = "Find minimum spanning tree using union-find and greedy edge selection"
                
            elif algorithm == 'prim':
                lines = input_data.strip().split('\n')
                n = int(lines[0])
                edges = []
                for i in range(1, len(lines)):
                    u, v, w = map(int, lines[i].split())
                    edges.append((u, v, w))
                mst, cost = prim_algorithm(n, edges)
                result = {"mst": mst, "cost": cost}
                complexity = "O(E log V)"
                operations = len(edges) * (1 + len(bin(n)) - 2)
                explanation = "Build MST by greedily adding minimum weight edges using priority queue"
                
            elif algorithm == 'optimal_merge':
                file_sizes = list(map(int, input_data.split()))
                cost, merges = optimal_merge_pattern(file_sizes)
                result = {"cost": cost, "merges": merges}
                complexity = "O(n log n)"
                operations = len(file_sizes) * (1 + len(bin(len(file_sizes))) - 2)
                explanation = "Determine optimal order to merge files to minimize total operations"
        
        # Dynamic Programming Algorithms
        elif category == 'dynamic':
            if algorithm == 'fibonacci':
                n = int(input_data)
                result = fibonacci(n)
                complexity = "O(n)"
                operations = n
                explanation = "Compute nth Fibonacci number using bottom-up dynamic programming"
                
            elif algorithm == 'knapsack':
                lines = input_data.strip().split('\n')
                values = list(map(int, lines[0].split()))
                weights = list(map(int, lines[1].split()))
                W = int(lines[2])
                result = knapsack_dp(values, weights, W)
                complexity = "O(n*W)"
                operations = len(values) * W
                explanation = "Find maximum value items that fit in knapsack using 0/1 DP"
                
            elif algorithm == 'lcs':
                lines = input_data.strip().split('\n')
                X = lines[0]
                Y = lines[1]
                result = lcs(X, Y)
                complexity = "O(n*m)"
                operations = len(X) * len(Y)
                explanation = "Find longest common subsequence using 2D DP table"
                
            elif algorithm == 'matrix_chain':
                dimensions = list(map(int, input_data.split()))
                cost, _ = matrix_chain_multiply(dimensions)
                result = cost
                complexity = "O(n³)"
                operations = (len(dimensions) - 1) ** 3
                explanation = "Find optimal parenthesization order to minimize scalar multiplications"
                
            elif algorithm == 'tsp':
                lines = input_data.strip().split('\n')
                dist_matrix = []
                for line in lines:
                    dist_matrix.append(list(map(int, line.split())))
                cost, path = tsp_dp(dist_matrix)
                result = {"cost": cost, "path": path}
                complexity = "O(n² * 2^n)"
                operations = (len(dist_matrix) ** 2) * (1 << len(dist_matrix))
                explanation = "Find shortest Hamiltonian cycle using bitmask DP"
        
        # Backtracking Algorithms
        elif category == 'backtracking':
            if algorithm == 'nqueens':
                n = int(input_data)
                solutions = n_queens(n)
                result = f"{len(solutions)} solutions found"
                complexity = "O(N!)"
                operations = 1
                for i in range(1, n + 1):
                    operations *= i
                explanation = f"Place {n} queens on {n}x{n} board with no attacks using backtracking"
                
            elif algorithm == 'naive_string':
                lines = input_data.strip().split('\n')
                text = lines[0]
                pattern = lines[1]
                matches = naive_string_matching(text, pattern)
                result = matches
                complexity = "O((n-m+1)*m)"
                operations = (len(text) - len(pattern) + 1) * len(pattern)
                explanation = "Find all pattern occurrences using naive brute force approach"
                
            elif algorithm == 'rabin_karp':
                lines = input_data.strip().split('\n')
                text = lines[0]
                pattern = lines[1]
                matches = rabin_karp(text, pattern)
                result = matches
                complexity = "O(n+m) average"
                operations = len(text) + len(pattern)
                explanation = "Find pattern using rolling polynomial hash for efficient matching"
                
            elif algorithm == 'kmp':
                lines = input_data.strip().split('\n')
                text = lines[0]
                pattern = lines[1]
                matches = knuth_morris_pratt(text, pattern)
                result = matches
                complexity = "O(n+m)"
                operations = len(text) + len(pattern)
                explanation = "Find pattern using failure function array for optimal matching"
        
        end_time = time.time()
        
        return jsonify({
            'output': str(result),
            'complexity': complexity,
            'operations': operations,
            'time': round(end_time - start_time, 6),
            'explanation': explanation,
            'success': True
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
