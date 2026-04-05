# 🎯 DAA Algorithms Playground

An interactive web-based simulator for **Design & Analysis of Algorithms**. Features implementations of 16 algorithms across four major paradigms: Divide & Conquer, Greedy, Dynamic Programming, and Backtracking.

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
│   ├── dynamic.py             # Fibonacci, 0/1 Knapsack, LCS, Matrix Chain, TSP
│   └── backtracking.py        # N-Queens, String Matching (Naive, Rabin-Karp, KMP)
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

## 📚 Supported Algorithms (16 Total)

### Divide & Conquer (5 algorithms)
| Algorithm | Time Complexity | Input Example |
|-----------|-----------------|---------------|
| Merge Sort | O(n log n) | `5,3,1,2` |
| Quick Sort | O(n log n) avg | `5,3,1,2` |
| Binary Search | O(log n) | `1,2,3,5,8,3` |
| Heap Sort | O(n log n) | `5,3,1,2` |
| Strassen's Matrix Multiply | O(n^2.807) | `1 2\n3 4\n5 6\n7 8` |

### Greedy (4 algorithms)
| Algorithm | Time Complexity | Input Example |
|-----------|-----------------|---------------|
| Fractional Knapsack | O(n log n) | `60,100;10,20;50` |
| Kruskal's MST | O(E log E) | `4\n0 1 1\n0 2 2\n1 2 3\n2 3 4` |
| Prim's MST | O(E log V) | `4\n0 1 1\n0 2 2\n1 2 3\n2 3 4` |
| Optimal Merge Pattern | O(n log n) | `10,20,30` |

### Dynamic Programming (5 algorithms)
| Algorithm | Time Complexity | Input Example |
|-----------|-----------------|---------------|
| Fibonacci (DP) | O(n) | `10` |
| 0/1 Knapsack | O(n*W) | `60,100;10,20;50` |
| Longest Common Subsequence | O(n*m) | `AGGTAB;GXTXAYB` |
| Matrix Chain Multiply | O(n³) | `10 20 30 40` |
| TSP (Bitmask DP) | O(n²*2^n) | `0 10 15\n10 0 35\n15 35 0` |

### Backtracking (4 algorithms + 3 string matching variants)
| Algorithm | Time Complexity | Input Example |
|-----------|-----------------|---------------|
| N-Queens Problem | O(N!) | `8` |
| Naive String Matching | O((n-m+1)*m) | `ABABDABACD;ABD` |
| Rabin-Karp Matching | O(n+m) avg | `ABABDABACD;ABD` |
| KMP String Matching | O(n+m) | `ABABDABACD;ABD` |

## 💡 Usage Examples

### Example 1: Quick Sort
1. Select **Divide & Conquer** paradigm
2. Select **Quick Sort** algorithm
3. Enter: `5,3,8,1,2`
4. Click **Run Algorithm**
5. Output: `[1, 2, 3, 5, 8]` with O(n log n) complexity

### Example 2: Fibonacci (DP)
1. Select **Dynamic Programming** paradigm
2. Select **Fibonacci (DP)** algorithm
3. Enter: `10`
4. Output: `55` (10th Fibonacci number) with O(n) complexity

### Example 3: Binary Search
1. Select **Divide & Conquer** paradigm
2. Select **Binary Search** algorithm
3. Enter: `1,2,3,5,8,3` (search for 3 in array [1,2,3,5,8])
4. Output: `3 found at index 3` (1-based indexing) with O(log n) complexity

### Example 4: Kruskal's MST
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

- All algorithms implemented in pure Python (no external algorithm libraries)
- Measured execution times are in seconds
- For very small inputs, execution time may be dominated by overhead
- The app uses Flask's built-in server (not recommended for production)
- 1-based indexing used for Binary Search results
- All graph algorithms use adjacency list representation

## 🎓 Learning Resources

This playground is designed to help understand:
- Algorithm efficiency and time complexity analysis
- Different algorithmic paradigms and their characteristics
- Real-world performance vs. theoretical analysis
- Trade-offs between different algorithmic approaches
- Practical applications of advanced algorithms

## 📄 License

This project is open for educational use.
