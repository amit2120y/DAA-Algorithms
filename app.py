from flask import Flask, render_template, request, jsonify
import time
import traceback

# Import all algorithms
from algorithms.divide_conquer import merge_sort, quick_sort, binary_search, heap_sort, strassen_multiply
from algorithms.greedy import fractional_knapsack, kruskal_algorithm, prim_algorithm, optimal_merge_pattern
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
                # Parse input - handle both space and comma separated values
                if ',' in input_data:
                    arr = list(map(int, input_data.split(',')))
                else:
                    arr = list(map(int, input_data.split()))
                result = merge_sort(arr)
                complexity = "O(n log n)"
                operations = len(arr) * (1 + len(bin(len(arr))) - 2)
                explanation = "Divide and conquer approach: divide array in half, sort recursively, then merge"
                
            elif algorithm == 'quick_sort':
                # Parse input - handle both space and comma separated values
                if ',' in input_data:
                    arr = list(map(int, input_data.split(',')))
                else:
                    arr = list(map(int, input_data.split()))
                result = quick_sort(arr)
                complexity = "O(n log n) average, O(n²) worst"
                operations = len(arr) * (1 + len(bin(len(arr))) - 2)
                explanation = "Partition-based sorting: select pivot, partition array, recursively sort subarrays"
                
            elif algorithm == 'binary_search':
                # Parse input: array,target format (array is auto-sorted for binary search)
                # Example: "1,2,3,5,8,3" means search for 3 in array [1,2,3,5,8]
                input_str = input_data.strip()
                
                # Find the last comma to separate array from target
                last_comma = input_str.rfind(',')
                if last_comma == -1:
                    raise ValueError("Binary search requires format: array_values,target (e.g., '1,3,5,7,3')")
                
                array_part = input_str[:last_comma]
                target = int(input_str[last_comma+1:])
                
                # Parse array - handle both space and comma separated
                arr = list(map(int, array_part.split(',')))
                arr.sort()  # Binary search requires sorted array
                
                index = binary_search(arr, target)
                if index == -1:
                    result = f"{target} not found in array"
                else:
                    result = f"{target} found at index {index}"
                complexity = "O(log n)"
                operations = len(bin(len(arr))) - 2
                explanation = f"Search for {target} in sorted array {arr} by repeatedly dividing search interval in half"
                
            elif algorithm == 'heap_sort':
                # Parse input - handle both space and comma separated values
                if ',' in input_data:
                    arr = list(map(int, input_data.split(',')))
                else:
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
                # Handle both newline-separated and semicolon-separated input
                if '\n' in input_data:
                    lines = input_data.strip().split('\n')
                else:
                    lines = input_data.strip().split(';')
                
                # Parse values - handle both space and comma separated
                values_str = lines[0]
                values = list(map(int, values_str.split(',') if ',' in values_str else values_str.split()))
                
                # Parse weights - handle both space and comma separated
                weights_str = lines[1]
                weights = list(map(int, weights_str.split(',') if ',' in weights_str else weights_str.split()))
                
                # Parse capacity
                capacity = int(lines[2])
                result = fractional_knapsack(values, weights, capacity)
                complexity = "O(n log n)"
                operations = len(values) * (1 + len(bin(len(values))) - 2)
                explanation = "Greedy approach: sort items by value/weight ratio, fill knapsack in order"
                
            elif algorithm == 'kruskal':
                lines = input_data.strip().split('\n')
                n = int(lines[0])
                edges = []
                for i in range(1, len(lines)):
                    # Handle both space and comma separated values
                    edge_str = lines[i]
                    parts = edge_str.split(',') if ',' in edge_str else edge_str.split()
                    u, v, w = map(int, parts)
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
                    # Handle both space and comma separated values
                    edge_str = lines[i]
                    parts = edge_str.split(',') if ',' in edge_str else edge_str.split()
                    u, v, w = map(int, parts)
                    edges.append((u, v, w))
                mst, cost = prim_algorithm(n, edges)
                result = {"mst": mst, "cost": cost}
                complexity = "O(E log V)"
                operations = len(edges) * (1 + len(bin(n)) - 2)
                explanation = "Build MST by greedily adding minimum weight edges using priority queue"
                
            elif algorithm == 'optimal_merge':
                # Parse input - handle both space and comma separated values
                if ',' in input_data:
                    file_sizes = list(map(int, input_data.split(',')))
                else:
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
                # Handle both newline-separated and semicolon-separated input
                if '\n' in input_data:
                    lines = input_data.strip().split('\n')
                else:
                    lines = input_data.strip().split(';')
                
                # Parse values - handle both space and comma separated
                values_str = lines[0]
                values = list(map(int, values_str.split(',') if ',' in values_str else values_str.split()))
                
                # Parse weights - handle both space and comma separated
                weights_str = lines[1]
                weights = list(map(int, weights_str.split(',') if ',' in weights_str else weights_str.split()))
                
                # Parse capacity
                W = int(lines[2])
                result = knapsack_dp(values, weights, W)
                complexity = "O(n*W)"
                operations = len(values) * W
                explanation = "Find maximum value items that fit in knapsack using 0/1 DP"
                
            elif algorithm == 'lcs':
                # Handle both newline-separated and semicolon-separated input
                if '\n' in input_data:
                    lines = input_data.strip().split('\n')
                else:
                    lines = input_data.strip().split(';')
                
                X = lines[0].strip()
                Y = lines[1].strip()
                result = lcs(X, Y)
                complexity = "O(n*m)"
                operations = len(X) * len(Y)
                explanation = "Find longest common subsequence using 2D DP table"
                
            elif algorithm == 'matrix_chain':
                # Handle both space and comma separated values
                if ',' in input_data:
                    dimensions = list(map(int, input_data.split(',')))
                else:
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
                    # Handle both space and comma separated values
                    row = line.split(',') if ',' in line else line.split()
                    dist_matrix.append(list(map(int, row)))
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
                # Handle both newline-separated and semicolon-separated input
                if '\n' in input_data:
                    lines = input_data.strip().split('\n')
                else:
                    lines = input_data.strip().split(';')
                
                text = lines[0].strip()
                pattern = lines[1].strip()
                matches = naive_string_matching(text, pattern)
                result = matches
                complexity = "O((n-m+1)*m)"
                operations = (len(text) - len(pattern) + 1) * len(pattern)
                explanation = "Find all pattern occurrences using naive brute force approach"
                
            elif algorithm == 'rabin_karp':
                # Handle both newline-separated and semicolon-separated input
                if '\n' in input_data:
                    lines = input_data.strip().split('\n')
                else:
                    lines = input_data.strip().split(';')
                
                text = lines[0].strip()
                pattern = lines[1].strip()
                matches = rabin_karp(text, pattern)
                result = matches
                complexity = "O(n+m) average"
                operations = len(text) + len(pattern)
                explanation = "Find pattern using rolling polynomial hash for efficient matching"
                
            elif algorithm == 'kmp':
                # Handle both newline-separated and semicolon-separated input
                if '\n' in input_data:
                    lines = input_data.strip().split('\n')
                else:
                    lines = input_data.strip().split(';')
                
                text = lines[0].strip()
                pattern = lines[1].strip()
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
