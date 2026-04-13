from flask import Flask, render_template, request, jsonify
import time
import traceback
import math

# Import all algorithms
from algorithms.divide_conquer import merge_sort, quick_sort, binary_search, heap_sort, strassen_multiply
from algorithms.greedy import fractional_knapsack, kruskal_algorithm, prim_algorithm, optimal_merge_pattern
from algorithms.dynamic import knapsack_dp, lcs, matrix_chain_multiply
from algorithms.backtracking import n_queens, tsp_dp
from algorithms.string_matching import naive_string_matching, rabin_karp, knuth_morris_pratt, boyer_moore

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
        steps = []
        
        # Divide & Conquer Algorithms
        if category == 'divide':
            if algorithm == 'merge_sort':
                # Parse input - handle both space and comma separated values
                if ',' in input_data:
                    arr = list(map(int, input_data.split(',')))
                else:
                    arr = list(map(int, input_data.split()))
                
                # Track steps
                original_arr = arr.copy()
                result = merge_sort(arr)
                complexity = "O(n log n)"
                n = len(arr)
                operations = int(n * math.log2(n)) if n > 1 else n
                explanation = "Divide and conquer approach: divide array in half, sort recursively, then merge"
                
                # Generate steps for merge sort
                steps = [
                    {"description": "Input array", "detail": str(original_arr)},
                    {"description": "Divide: Split array into halves recursively", "detail": "Array is divided into single elements"},
                    {"description": "Conquer: Merge subarrays in sorted order", "detail": "Compare elements and merge"},
                    {"description": "Sorted Output", "detail": str(result)}
                ]
                
            elif algorithm == 'quick_sort':
                # Parse input - handle both space and comma separated values
                if ',' in input_data:
                    arr = list(map(int, input_data.split(',')))
                else:
                    arr = list(map(int, input_data.split()))
                
                original_arr = arr.copy()
                result, was_sorted = quick_sort(arr)
                
                # Calculate operations based on whether array is sorted
                n = len(arr)
                if was_sorted:
                    # Already sorted (increasing or decreasing): worst case O(n²)
                    operations = n * n
                    complexity = "O(n²) - Input already sorted!"
                    explanation = "Partition-based sorting: array is already sorted (increasing or decreasing), leading to worst-case O(n²) complexity"
                else:
                    # Unsorted: average case O(n log n)
                    operations = int(n * math.log2(n)) if n > 1 else n
                    complexity = "O(n log n) average, O(n²) worst"
                    explanation = "Partition-based sorting: select pivot, partition array, recursively sort subarrays"
                
                # Generate steps for quick sort
                steps = [
                    {"description": "Input array", "detail": str(original_arr)},
                    {"description": f"Array status: {'SORTED' if was_sorted else 'UNSORTED'}", "detail": f"Array is {'already sorted (increasing or decreasing)' if was_sorted else 'not sorted'}"},
                    {"description": "Select pivot element", "detail": f"Pivot: {original_arr[0] if original_arr else 'N/A'}"},
                    {"description": "Partition array into left and right", "detail": "Elements < pivot go left, > pivot go right"},
                    {"description": "Recursively sort subarrays", "detail": "Apply same process to left and right partitions"},
                    {"description": "Sorted Output", "detail": str(result)}
                ]
                
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
                
                index, found_at_first = binary_search(arr, target)
                if index == -1:
                    result = f"{target} not found in array"
                    complexity = "O(log n)"
                    operations = len(bin(len(arr))) - 2
                else:
                    result = f"{target} found at index {index}"
                    if found_at_first:
                        # Found at first mid check
                        operations = 1
                        complexity = "O(1) - Found at first check!"
                    else:
                        complexity = "O(log n)"
                        operations = len(bin(len(arr))) - 2
                
                explanation = f"Search for {target} in sorted array {arr} by repeatedly dividing search interval in half"
                
                # Generate steps
                steps = [
                    {"description": "Sorted array", "detail": str(arr)},
                    {"description": f"Searching for target: {target}", "detail": f"Start with full array range [0, {len(arr)-1}]"},
                    {"description": "Check middle element", "detail": f"Compare {target} with middle values"},
                    {"description": "Narrow search space", "detail": "Keep dividing the range in half based on comparison"},
                    {"description": "Final Result", "detail": result}
                ]
                
            elif algorithm == 'heap_sort':
                # Parse input - handle both space and comma separated values
                if ',' in input_data:
                    arr = list(map(int, input_data.split(',')))
                else:
                    arr = list(map(int, input_data.split()))
                
                original_arr = arr.copy()
                result = heap_sort(arr)
                complexity = "O(n log n)"
                n = len(arr)
                operations = int(n * math.log2(n)) if n > 1 else n
                explanation = "Build max heap, extract elements in order to sort array"
                
                steps = [
                    {"description": "Input array", "detail": str(original_arr)},
                    {"description": "Build max heap", "detail": "Organize array into heap structure"},
                    {"description": "Extract root (max) repeatedly", "detail": "Remove max element and heapify"},
                    {"description": "Sorted Output", "detail": str(result)}
                ]
                
            elif algorithm == 'strassen':
                lines = input_data.strip().split('\n')
                # Filter out empty lines
                lines = [line for line in lines if line.strip()]
                
                # Determine matrix size (n x n for n rows = n^2 elements)
                n = len(lines) // 2  # Divide total lines by 2 to get n for n x n matrices
                
                # Parse matrix A (first n lines) and matrix B (last n lines)
                A = [list(map(int, line.split())) for line in lines[:n]]
                B = [list(map(int, line.split())) for line in lines[n:]]
                
                # Verify matrices are square
                if len(A) != len(A[0]) or len(B) != len(B[0]):
                    raise ValueError(f"Matrices must be square. Got A: {len(A)}x{len(A[0])}, B: {len(B)}x{len(B[0])}")
                
                # Note: Strassen requires matrix dimensions to be powers of 2
                result = strassen_multiply(A, B)
                # Convert NumPy array to list for JSON serialization
                result = result.tolist()
                complexity = "O(n^2.807)"
                matrix_size = len(A)
                operations = int(7 ** math.log2(matrix_size)) if matrix_size > 1 else 7
                explanation = f"Recursive matrix multiplication using 7 multiplications instead of 8 for {matrix_size}x{matrix_size} matrices"
                
                steps = [
                    {"description": f"Matrix A ({matrix_size}x{matrix_size})", "detail": str(A)},
                    {"description": f"Matrix B ({matrix_size}x{matrix_size})", "detail": str(B)},
                    {"description": "Strassen Algorithm", "detail": "Divide matrices into submatrices, compute 7 products instead of 8 multiplications"},
                    {"description": f"Result Matrix ({matrix_size}x{matrix_size})", "detail": str(result)}
                ]
        
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
                result = fractional_knapsack(weights, values, capacity)
                complexity = "O(n log n)"
                n = len(values)
                operations = int(n * math.log2(n)) if n > 1 else n
                explanation = "Greedy approach: sort items by value/weight ratio, fill knapsack in order"
                
                # Generate steps
                steps = [
                    {"description": "Items with values and weights", "detail": f"Values: {values}, Weights: {weights}"},
                    {"description": f"Knapsack capacity: {capacity}", "detail": f"Can carry up to {capacity} units of weight"},
                    {"description": "Calculate value-to-weight ratio", "detail": "Ratio = Value / Weight for each item"},
                    {"description": "Sort by ratio (greedy choice)", "detail": "Pick items with highest ratio first"},
                    {"description": f"Total value achieved: {result}", "detail": "Fill knapsack greedily"}
                ]
                
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
                e = len(edges)
                operations = int(e * math.log2(e)) if e > 1 else e
                explanation = "Kruskal's Algorithm: Sort edges by weight, use Union-Find to detect cycles, greedily add edges that don't create cycles"
                
                steps = [
                    {"description": f"Graph structure", "detail": f"{n} vertices, {len(edges)} edges"},
                    {"description": "Step 1: Initialize Union-Find", "detail": f"Create data structure to track connected components"},
                    {"description": "Step 2: Sort all edges by weight", "detail": f"Process edges from smallest to largest weight"},
                    {"description": "Step 3: Process edges greedily", "detail": "For each edge, check if both vertices are in different components"},
                    {"description": "Step 4: Detect cycles with Union-Find", "detail": "Only add edges that don't create cycles (different components)"},
                    {"description": f"Result: MST with {len(mst)} edges", "detail": f"Total weight: {cost}"}
                ]
                
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
                operations = int(len(edges) * math.log2(n)) if n > 1 else len(edges)
                explanation = "Build MST by greedily adding minimum weight edges using priority queue"
                
                steps = [
                    {"description": f"Start with vertex 0", "detail": f"Initialize visited set with vertex 0"},
                    {"description": "Use priority queue to track minimum edges", "detail": f"Total vertices: {n}"},
                    {"description": "Greedily select minimum weight edge", "detail": "Always pick edge with smallest weight"},
                    {"description": "Add new vertex to MST", "detail": "Expand MST by connecting new vertices"},
                    {"description": f"Minimum Spanning Tree Cost: {cost}", "detail": f"Edges in MST: {mst}"}
                ]
                
            elif algorithm == 'optimal_merge':
                # Parse input - handle both space and comma separated values
                if ',' in input_data:
                    file_sizes = list(map(int, input_data.split(',')))
                else:
                    file_sizes = list(map(int, input_data.split()))
                cost, merges = optimal_merge_pattern(file_sizes)
                result = {"cost": cost, "merges": merges}
                complexity = "O(n log n)"
                n = len(file_sizes)
                operations = int(n * math.log2(n)) if n > 1 else n
                explanation = "Determine optimal order to merge files to minimize total operations"
                
                steps = [
                    {"description": "File sizes to merge", "detail": str(file_sizes)},
                    {"description": "Use greedy approach with priority queue", "detail": "Always merge two smallest files first"},
                    {"description": "Calculate merge costs", "detail": f"Cost of merging two files = sum of their sizes"},
                    {"description": "Repeat until all files merged", "detail": f"Total merge operations: {len(merges)}"},
                    {"description": f"Optimal total cost: {cost}", "detail": f"Merge sequence: {merges}"}
                ]
        
        # Dynamic Programming Algorithms
        elif category == 'dynamic':
            if algorithm == 'knapsack':
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
                
                steps = [
                    {"description": "Items with values and weights", "detail": f"Values: {values}, Weights: {weights}"},
                    {"description": f"Knapsack capacity: {W}", "detail": f"Maximum weight: {W} units"},
                    {"description": f"Number of items: {len(values)}", "detail": "Create DP table of size (n+1) x (W+1)"},
                    {"description": "Fill DP table bottom-up", "detail": "For each item, decide to include or exclude"},
                    {"description": f"Maximum value: {result}", "detail": "Traceback to find items selected"}
                ]
                
            elif algorithm == 'lcs':
                if '\n' in input_data:
                    lines = input_data.strip().split('\n')
                else:
                    lines = input_data.strip().split(';')
                
                X = lines[0].strip()
                Y = lines[1].strip()
                length, sequence = lcs(X, Y)
                complexity = "O(n*m)"
                operations = len(X) * len(Y)
                explanation = "Find longest common subsequence using DP table with backtracking"
                
                steps = [
                    {"description": "First string (X)", "detail": f"'{X}'"},
                    {"description": "Second string (Y)", "detail": f"'{Y}'"},
                    {"description": f"Create DP table: ({len(X)+1}) x ({len(Y)+1})", "detail": "Initialize first row and column to 0"},
                    {"description": "Fill DP table", "detail": f"If X[i]==Y[j]: dp[i][j]=dp[i-1][j-1]+1, else: max(dp[i-1][j], dp[i][j-1])"},
                    {"description": "Backtrack to find sequence", "detail": "Trace from end to start to reconstruct LCS"},
                    {"description": f"Length: {length}", "detail": f"Sequence: '{sequence}'"}
                ]
                result = f"Length: {length} | Sequence: '{sequence}'"
                
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
                
                steps = [
                    {"description": f"Matrices: {len(dimensions)-1}", "detail": f"Dimensions: {dimensions}"},
                    {"description": "Matrix sizes", "detail": f"M1: {dimensions[0]}x{dimensions[1]}, M2: {dimensions[1]}x{dimensions[2]}, ..."},
                    {"description": "Create DP table (cost)", "detail": f"Size: ({len(dimensions)-1}) x ({len(dimensions)-1})"},
                    {"description": "Fill table for all possible ways", "detail": "Try all parenthesizations"},
                    {"description": f"Minimum scalar multiplications: {result}", "detail": "Optimal parenthesization found"}
                ]
        
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
                
                steps = [
                    {"description": f"Problem: Place {n} queens on {n}x{n} board", "detail": "No two queens can attack each other"},
                    {"description": "Backtracking approach", "detail": "Place queen in each row, check column and diagonal conflicts"},
                    {"description": "Recursively solve", "detail": f"Try each column in current row, backtrack if no valid placement"},
                    {"description": "Check constraints", "detail": "Ensure no queen threatens another (row, column, diagonal)"},
                    {"description": f"Total solutions: {len(solutions)}", "detail": f"Found all valid board configurations"}
                ]
            
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
                explanation = "Find shortest Hamiltonian cycle using bitmask DP with backtracking"
                
                steps = [
                    {"description": f"Number of cities: {len(dist_matrix)}", "detail": "Distance matrix provided"},
                    {"description": "Use bitmask DP approach", "detail": "dp[mask][i] = min cost to visit cities in mask ending at city i"},
                    {"description": f"Total states: {1 << len(dist_matrix)}", "detail": f"2^{len(dist_matrix)} possible subsets"},
                    {"description": "Fill DP table bottom-up", "detail": "Compute shortest path for all subsets"},
                    {"description": f"Shortest tour cost: {cost}", "detail": f"Optimal path: {' -> '.join(map(str, path))}"}
                ]
                
            else:
                raise ValueError(f"Unknown backtracking algorithm: {algorithm}")
        
        # String Matching Algorithms
        elif category == 'string_matching':
            if algorithm == 'naive_string':
                if ';' in input_data:
                    text, pattern = input_data.split(';')
                else:
                    parts = input_data.split()
                    text, pattern = parts[0], parts[1]
                
                positions = naive_string_matching(text.strip(), pattern.strip())
                result = f"Pattern found at positions: {positions}"
                complexity = "O(n*m)"
                operations = len(text) * len(pattern)
                explanation = "Find all occurrences of pattern in text using naive approach"
                
                steps = [
                    {"description": "Text to search", "detail": f"'{text.strip()}'"},
                    {"description": "Pattern to find", "detail": f"'{pattern.strip()}'"},
                    {"description": "Naive sliding window", "detail": "Compare pattern with each position in text"},
                    {"description": f"Comparisons needed: {len(text)} * {len(pattern)}", "detail": f"Worst case: {operations} character comparisons"},
                    {"description": f"Pattern locations: {positions}", "detail": f"Found at {len(positions)} position(s)"}
                ]
                
            elif algorithm == 'rabin_karp':
                if ';' in input_data:
                    text, pattern = input_data.split(';')
                else:
                    parts = input_data.split()
                    text, pattern = parts[0], parts[1]
                
                positions = rabin_karp(text.strip(), pattern.strip())
                result = f"Pattern found at positions: {positions}"
                complexity = "O(n+m) average"
                operations = len(text) + len(pattern)
                explanation = "Find pattern using rolling hash for efficient comparison"
                
                steps = [
                    {"description": "Text to search", "detail": f"'{text.strip()}'"},
                    {"description": "Pattern to find", "detail": f"'{pattern.strip()}'"},
                    {"description": "Calculate pattern hash", "detail": f"Hash of pattern: {hash(pattern.strip())}"},
                    {"description": "Rolling hash approach", "detail": "Slide window and update hash incrementally"},
                    {"description": f"Pattern locations: {positions}", "detail": f"Found at {len(positions)} position(s)"}
                ]
                
            elif algorithm == 'kmp':
                if ';' in input_data:
                    text, pattern = input_data.split(';')
                else:
                    parts = input_data.split()
                    text, pattern = parts[0], parts[1]
                
                positions = knuth_morris_pratt(text.strip(), pattern.strip())
                result = f"Pattern found at positions: {positions}"
                complexity = "O(n+m)"
                operations = len(text) + len(pattern)
                explanation = "Find pattern using KMP failure function to avoid redundant comparisons"
                
                steps = [
                    {"description": "Text to search", "detail": f"'{text.strip()}'"},
                    {"description": "Pattern to find", "detail": f"'{pattern.strip()}'"},
                    {"description": "Build KMP failure function", "detail": f"Analyze pattern structure for '{pattern.strip()}'"},
                    {"description": "Single pass matching", "detail": "Use failure function to skip redundant comparisons"},
                    {"description": f"Pattern locations: {positions}", "detail": f"Found at {len(positions)} position(s)"}
                ]
            
            elif algorithm == 'boyer_moore':
                if ';' in input_data:
                    text, pattern = input_data.split(';')
                else:
                    parts = input_data.split()
                    text, pattern = parts[0], parts[1]
                
                positions = boyer_moore(text.strip(), pattern.strip())
                result = f"Pattern found at positions: {positions}"
                complexity = "O(n/m) best, O(n*m) worst"
                operations = len(text) + len(pattern)
                explanation = "Find pattern using Boyer-Moore algorithm with bad character rule"
                
                steps = [
                    {"description": "Text to search", "detail": f"'{text.strip()}'"},
                    {"description": "Pattern to find", "detail": f"'{pattern.strip()}'"},
                    {"description": "Build bad character table", "detail": f"Analyze character positions in pattern"},
                    {"description": "Scan from right to left", "detail": "Skip mismatches using bad character rule"},
                    {"description": f"Pattern locations: {positions}", "detail": f"Found at {len(positions)} position(s)"}
                ]
            
            else:
                raise ValueError(f"Unknown string matching algorithm: {algorithm}")
        
        end_time = time.time()
        
        return jsonify({
            'output': str(result),
            'complexity': complexity,
            'operations': operations,
            'time': round(end_time - start_time, 6),
            'explanation': explanation,
            'steps': steps,
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
