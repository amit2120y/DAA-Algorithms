# 🎯 DAA Algorithms Playground

An interactive web-based simulator for **Design & Analysis of Algorithms**. Features implementations of 18 algorithms across five major paradigms: Divide & Conquer, Greedy, Dynamic Programming, Backtracking, and String Matching.

## 📋 Features

- **Dynamic Algorithm Selection**: Choose paradigm → select specific algorithm
- **Real-Time Execution**: Run algorithms with custom input and see results instantly
- **Time Complexity Analysis**: Theoretical complexity + measured execution time
- **Operation Counting**: See number of operations performed during execution
- **Input Format Guide**: Clear instructions for each algorithm's input format
- **Responsive Design**: Works on desktop and mobile browsers
- **Python Backend**: Server-side Python execution via Flask

## 🏗️ Project Structure

```
.
├── app.py                      # Flask application & API endpoints
├── algorithms/                 # Algorithm implementations
│   ├── divide_conquer.py      # Merge, Quick, Binary Search, Heap Sort, Strassen
│   ├── greedy.py              # Fractional Knapsack, Kruskal, Prim, Optimal Merge
│   ├── dynamic.py             # 0/1 Knapsack, LCS, Matrix Chain Multiply
│   ├── backtracking.py        # N-Queens, TSP (Bitmask DP)
│   └── string_matching.py     # Naive, Rabin-Karp, KMP, Boyer-Moore
├── templates/
│   └── index.html             # Main UI template
├── static/
│   ├── script.js              # Client-side JavaScript logic
│   └── style.css              # Responsive styling
├── README.md                  # This file
└── requirements.txt           # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Flask 2.3.0+

### Installation

1. **Clone/Navigate to project**:
```bash
cd "e:\code\.vscode\Webs\Divide & Conquer"
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the Flask app**:
```bash
python app.py
```

4. **Open in browser**:
Navigate to `http://localhost:5000`
8 Total)

### Divide & Conquer (5 algorithms)
| Algorithm | Time Complexity | Special Cases | Input Example |
|-----------|-----------------|---------------|---------------|
| Merge Sort | O(n log n) | Always O(n log n) | `5,3,1,2` |
| Quick Sort | O(n log n) avg, **O(n²) if sorted** | Detects sorted arrays (increasing/decreasing) and calculates as O(n²) | `5,3,1,2` |
| Binary Search | O(log n) avg, **O(1) if found at mid** | If target found at first mid check, operations = 1 | `1,2,3,5,8,3` |
| Heap Sort | O(n log n) | Always O(n log n) | `5,3,1,2` |
| Strassen's Matrix Multiply | O(n^2.807) | Fast matrix multiplication | `1 2\n3 4\n5 6\n7 8` |

### Greedy (4 algorithms)
| Algorithm | Time Complexity | Input Example |
|-----------|-----------------|---------------|
| Fractional Knapsack | O(n log n) | `60,100;10,20;50` |
| Kruskal's MST | O(E log E) | `4\n0 1 1\n0 2 2\n1 2 3\n2 3 4` |
| Prim's MST | O(E log V) | `4\n0 1 1\n0 2 2\n1 2 3\n2 3 4` |
| Optimal Merge Pattern | O(n log n) | `10,20,30` |

### Dynamic Programming (3 algorithms)
| Algorithm | Time Complexity | Input Example |
|-----------|-----------------|---------------|
| 0/1 Knapsack | O(n*W) | `60,100;10,20;50` |
| Longest Common Subsequence | O(n*m) | `AGGTAB;GXTXAYB` |
| Matrix Chain Multiply | O(n³) | `10 20 30 40` |

### Backtracking (2 algorithms)
| Algorithm | Time Complexity | Input Example |
|-----------|-----------------|---------------|
| N-Queens Problem | O(N!) | `8` |
| TSP (Bitmask DP) | O(n²*2^n) | `0 10 15\n10 0 35\n15 35 0` |

### String Matching (4 algorithms)
| Algorithm | Time Complexity | Description | Input Example |
|-----------|-----------------|-------------|---------------|
| Naive String Matching | O((n-m+1)*m) | Brute force pattern matching | `ABABDABACD;ABD` |
| Rabin-Karp Matching | O(n+m) average | Rolling hash for fast matching | `ABABDABACD;ABD` |
| KMP String Matching | O(n+m) | Uses failure function to skip comparisons | `ABABDABACD;ABD` |
| **Boyer-Moore** (NEW) | O(n/m) best, O(n*m) worst | Right-to-left scan with bad character rule avg | `ABABDABACD;ABD` |
| KMP String Matching | O (Unsorted Array)
1. Select **Divide & Conquer** paradigm
2. Select **Quick Sort** algorithm
3. Enter: `5,3,8,1,2`
4. Click **Run Algorithm**
5. Output: `[1, 2, 3, 5, 8]` with **O(n log n)** complexity and **operations = n * log(n)**

### Example 2: Quick Sort (Sorted Array - Worst Case)
1. Select **Divide & Conquer** paradigm
2. Select **Quick Sort** algorithm
3. Enter: `1,2,3,4,5` (already sorted!)
4. Click **Run Algorithm**
5. Output: `[1, 2, 3, 4, 5]` with **O(n²)** complexity and **operations = n²** (worst case detected)

### Example 3: Binary Search (Found at First Check)
1. Select **Divide & Conquer** paradigm
2. Select **Binary Search** algorithm
3. Enter: `1,2,3,4,5,3` (searching for 3, which is at mid position)
4. Output: `3 found at index 3` with **O(1)** complexity and **operations = 1**

### Example 4: Binary Search (Multiple Iterations)
1. Select **Divide & Conquer** paradigm
2. Select **Binary Search** algorithm
3. Enter: `1,2,3,4,5,8,5` (searching for 8, requires iterations)
4. Output: `8 found at index 5` with **O(log n)** complexity

### Example 5: String Matching With Boyer-Moore
1. Select **String Matching** paradigm
2. Select **Boyer-Moore Algorithm**
3. Enter: `ABABDABACD;ABD`
4. Output: Pattern positions with efficient right-to-left scanning

### Example 6: N-Queens Problem
1. Select **Backtracking** paradigm
2. Select **N-Queens Problem**
3. Enter: `8`
4. Output: Number of solutions found for 8-queens with O(N!) complexity

### Example 7: TSP Using Bitmask DP
1. Select **Backtracking** paradigm
2. Select **TSP (Travelling Salesman Problem)**
3. Enter: `0 10 15\n10 0 35\n15 35 0`
4. Output: Shortest tour cost and path with O(n²*2^n) complexity
1. Select **Greedy** paradigm
2. Select **Kruskal's Algorithm (MST)**
3. Enter: `4\n0 1 1\n0 2 2\n1 2 3\n2 3 4`
4. Output: MST edges and total cost

## 🎨 Interface Highlights

- **Category Dropdown**: Filter algorithms by paradigm
- **Algorithm Dropdown**: Dynamically populated based on category
- **Input Textarea**: Format guide with clear examples
- **Run Button**: Executes the selected algorithm
- **Results Panel**: Shows output, complexity, operations, execution time, and explanation

## 📊 Output Information

Each result displays:
- **Output**: The actual result of the algorithm
- **Time Complexity**: Theoretical complexity analysis
- **Number of Operations**: Estimated operation count
- **Execution Time**: Measured runtime in seconds
- **Explanation**: Detailed description of the algorithm

## 🔧 Configuration

To run on a different port, modify `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8000)
```

## 📝 Notes

### Algorithm Optimizations
- **Quick Sort**: Automatically detects if input array is sorted (increasing or decreasing) and calculates worst-case O(n²) operations instead of average O(n log n)
- **Binary Search**: Optimized to detect if target is found at the first mid check, resulting in O(1) operations (best case)

### General Notes
- All algorithms implemented in pure Python (no external algorithm libraries)
- Measured execution times are in seconds
- For very small inputs, execution time may be dominated by overhead
- The app uses Flask's built-in server (not recommended for production)
- 1-based indexing used for Binary Search results
- All graph algorithms use adjacency list representation
- String Matching algorithms accept text and pattern separated by semicolon (e.g., `text;pattern`)
- TSP uses bitmask dynamic programming for exact solution

## 🎓 Learning Resources

This playground is designed to help understand:
- Algorithm efficiency and time complexity analysis
- Different algorithmic paradigms and their characteristics
  - **Divide & Conquer**: Breaking problems into subproblems (with smart case detection)
  - **Greedy**: Making locally optimal choices
  - **Dynamic Programming**: Solving overlapping subproblems optimally
  - **Backtracking**: Exploring solution space with constraint satisfaction
  - **String Matching**: Pattern finding in text with various optimization techniques
- Real-world performance vs. theoretical analysis
- Trade-offs between different algorithmic approaches
- Practical applications of advanced algorithms
- How data characteristics (sorted vs unsorted) affect algorithm performance
- Smart optimizations and best-case scenario handling

## 📄 License

This project is open for educational use.
