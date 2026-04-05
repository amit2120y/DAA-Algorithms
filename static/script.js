// Algorithm metadata for each category
const algorithmMap = {
    divide: [
        { id: 'merge_sort', name: 'Merge Sort' },
        { id: 'quick_sort', name: 'Quick Sort' },
        { id: 'binary_search', name: 'Binary Search' },
        { id: 'heap_sort', name: 'Heap Sort' },
        { id: 'strassen', name: "Strassen's Matrix Multiply" }
    ],
    greedy: [
        { id: 'fractional_knapsack', name: 'Fractional Knapsack' },
        { id: 'kruskal', name: "Kruskal's Algorithm (MST)" },
        { id: 'prim', name: "Prim's Algorithm (MST)" },
        { id: 'optimal_merge', name: 'Optimal Merge Pattern' }
    ],
    dynamic: [
        { id: 'fibonacci', name: 'Fibonacci (DP)' },
        { id: 'knapsack', name: '0/1 Knapsack (DP)' },
        { id: 'lcs', name: 'Longest Common Subsequence (LCS)' },
        { id: 'matrix_chain', name: 'Matrix Chain Multiplication' },
        { id: 'tsp', name: 'TSP (Travelling Salesman Problem)' }
    ],
    backtracking: [
        { id: 'nqueens', name: 'N-Queens Problem' },
        { id: 'naive_string', name: 'Naive String Matching' },
        { id: 'rabin_karp', name: 'Rabin-Karp String Matching' },
        { id: 'kmp', name: 'Knuth-Morris-Pratt Algorithm' }
    ]
};

// Populate algorithm dropdown when category changes
function populateAlgorithms() {
    const category = document.getElementById('category').value;
    const algoSelect = document.getElementById('algorithm');

    algoSelect.innerHTML = '';

    algorithmMap[category].forEach(algo => {
        const option = document.createElement('option');
        option.value = algo.id;
        option.textContent = algo.name;
        algoSelect.appendChild(option);
    });
}

// Run the selected algorithm
async function runAlgo() {
    const category = document.getElementById('category').value;
    const algorithm = document.getElementById('algorithm').value;
    const inputData = document.getElementById('inputData').value.trim();

    if (!inputData) {
        showError('Please enter input data!');
        return;
    }

    const resultBox = document.getElementById('resultBox');
    const metaInfo = document.getElementById('metaInfo');

    resultBox.innerHTML = '<p><em>Running...</em></p>';
    metaInfo.innerHTML = '';

    try {
        const response = await fetch('/run', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ category, algorithm, input: inputData })
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
            showError(data.error);
            return;
        }

        // Format and display output
        resultBox.innerHTML = `
            <div class="result-content">
                <h3>Output:</h3>
                <pre>${formatOutput(data.output)}</pre>
            </div>
        `;

        metaInfo.innerHTML = `
            <div class="meta-details">
                <div class="meta-item">
                    <strong>Time Complexity:</strong> <code>${data.complexity}</code>
                </div>
                <div class="meta-item">
                    <strong>Number of Operations:</strong> <code>${data.operations}</code>
                </div>
                <div class="meta-item" style="grid-column: 1/-1;">
                    <strong>Explanation:</strong> ${data.explanation}
                </div>
            </div>
        `;

    } catch (error) {
        showError('Error: ' + error.message);
    }
}

function showError(msg) {
    document.getElementById('resultBox').innerHTML = `<p class="error"> ${msg}</p>`;
}

function formatOutput(output) {
    if (typeof output === 'string') return output;
    return JSON.stringify(output, null, 2);
}

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    populateAlgorithms();

    document.getElementById('category').addEventListener('change', () => {
        populateAlgorithms();
    });

    document.getElementById('runBtn').addEventListener('click', runAlgo);
});