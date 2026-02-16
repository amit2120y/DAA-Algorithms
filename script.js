function log2(n) {
    return Math.log(n) / Math.log(2);
}

function runAlgorithm() {
    let algo = document.getElementById("algorithm").value;
    let arr = document.getElementById("input").value.split(',').map(Number);
    let key = Number(document.getElementById("key").value);
    let result = "";
    let complexity = "";

    if (algo === "binary") {
        arr.sort((a, b) => a - b);
        let searchResult = binarySearch(arr, key, 0, arr.length - 1);
        result = "Sorted Array: [" + arr.join(", ") + "]<br>" + searchResult;
        let n = arr.length;
        let ops = Math.round(log2(n));
        complexity = `O(log n), Operations ≈ ${ops}`;

    }

    else if (algo === "merge") {
        result = mergeSort(arr);
        let n = arr.length;
        let ops = Math.round(n * log2(n));
        complexity = `O(n log n), Operations ≈ ${ops}`;
    }

    else if (algo === "quick") {
        result = quickSort(arr);
        let n = arr.length;
        let ops = Math.round(n * log2(n));
        complexity = `O(n log n), Operations ≈ ${ops}`;

    }

    else if (algo === "heap") {
        result = heapSort(arr);
        let n = arr.length;
        let ops = Math.round(n * log2(n));
        complexity = `O(n log n), Operations ≈ ${ops}`;
    }

    else if (algo === "strassen") {
        let parsed = parseMatricesForStrassen(arr);
        if (parsed.error) {
            result = parsed.error;
            complexity = "N/A";
        } else {
            let { n, A, B } = parsed;
            
            let m = nextPowerOfTwo(n);
            let A2 = padMatrix(A, n, m);
            let B2 = padMatrix(B, n, m);
            let Cpad = strassenMultiply(A2, B2);
            let C = unpadMatrix(Cpad, n);
            
            result = C.map(r => '[' + r.join(', ') + ']').join('<br>');
            let ops = Math.round(Math.pow(n, log2(7)));
            complexity = `O(n^2.807), Operations ≈ ${ops}`;
        }
    }

    else if (algo === "maxmin") {
        let res = maxMin(arr, 0, arr.length - 1);
        result = "Max: " + res.max + ", Min: " + res.min;
        let n = arr.length;
        complexity = `O(n), Operations ≈ ${n}`;

    }

    else if (algo === "power") {
        result = power(arr[0], arr[1]);
        let n = arr[1];   // exponent
        let ops = Math.round(log2(n));
        complexity = `O(log n), Operations ≈ ${ops}`;

    }

    else if (algo === "sum") {
        result = sumArray(arr, 0, arr.length - 1);
        let n = arr.length;
        complexity = `O(n), Operations ≈ ${n}`;

    }

    else if (algo === "peak") {
        result = findPeak(arr, 0, arr.length - 1);
        let n = arr.length;
        let ops = Math.round(log2(n));
        complexity = `O(log n), Operations ≈ ${ops}`;

    }

    else if (algo === "inversion") {
        result = countInversions(arr);
        let n = arr.length;
        let ops = Math.round(n * log2(n));
        complexity = `O(n log n), Operations ≈ ${ops}`;

    }

    document.getElementById("output").innerHTML =
        "<b>Result:</b> " + result + "<br><br/><b>Time Complexity:</b> " + complexity +
        "<br><small>(Calculated using input size n = " + arr.length + ")</small>";
}

document.getElementById("algorithm").addEventListener("change", function () {
    let algo = this.value;
    let keyInput = document.getElementById("key");

    if (algo === "binary") {
        keyInput.style.display = "inline-block";
    } else {
        keyInput.style.display = "none";
        keyInput.value = "";
    }
});




function binarySearch(arr, key, low, high) {
    if (low > high) return "Not Found";
    let mid = Math.floor((low + high) / 2);
    if (arr[mid] === key) return "Found at index " + mid;
    if (key < arr[mid]) return binarySearch(arr, key, low, mid - 1);
    return binarySearch(arr, key, mid + 1, high);
}

function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    let mid = Math.floor(arr.length / 2);
    let left = mergeSort(arr.slice(0, mid));
    let right = mergeSort(arr.slice(mid));
    return merge(left, right);
}

function merge(left, right) {
    let res = [];
    while (left.length && right.length)
        res.push(left[0] < right[0] ? left.shift() : right.shift());
    return res.concat(left, right);
}

function quickSort(arr) {
    if (arr.length <= 1) return arr;
    let pivot = arr[0];
    let left = arr.slice(1).filter(x => x < pivot);
    let right = arr.slice(1).filter(x => x >= pivot);
    return [...quickSort(left), pivot, ...quickSort(right)];
}

function heapSort(arr) {
    let n = arr.length;
    let sorted = [...arr]; 

   
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--)
        heapify(sorted, n, i);

    
    for (let i = n - 1; i > 0; i--) {
        [sorted[0], sorted[i]] = [sorted[i], sorted[0]];
        heapify(sorted, i, 0);
    }

    return sorted;
}

function heapify(arr, n, i) {
    let largest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest !== i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]];
        heapify(arr, n, largest);
    }
}

function maxMin(arr, low, high) {
    if (low === high) return { max: arr[low], min: arr[low] };
    let mid = Math.floor((low + high) / 2);
    let left = maxMin(arr, low, mid);
    let right = maxMin(arr, mid + 1, high);
    return {
        max: Math.max(left.max, right.max),
        min: Math.min(left.min, right.min)
    };
}

function power(x, n) {
    if (n === 0) return 1;
    let temp = power(x, Math.floor(n / 2));
    return n % 2 === 0 ? temp * temp : x * temp * temp;
}

function sumArray(arr, low, high) {
    if (low === high) return arr[low];
    let mid = Math.floor((low + high) / 2);
    return sumArray(arr, low, mid) + sumArray(arr, mid + 1, high);
}

function findPeak(arr, low, high) {
    let mid = Math.floor((low + high) / 2);
    if ((mid === 0 || arr[mid] >= arr[mid - 1]) &&
        (mid === arr.length - 1 || arr[mid] >= arr[mid + 1]))
        return arr[mid];
    if (mid > 0 && arr[mid - 1] > arr[mid])
        return findPeak(arr, low, mid - 1);
    return findPeak(arr, mid + 1, high);
}

function countInversions(arr) {
    let count = 0;
    for (let i = 0; i < arr.length; i++)
        for (let j = i + 1; j < arr.length; j++)
            if (arr[i] > arr[j]) count++;
    return count;
}


function parseMatricesForStrassen(values) {
    
    let nums = values.map(Number).filter(x => !isNaN(x));
    if (nums.length === 0) return { error: 'No numeric input provided' };


    if (Number.isInteger(nums[0]) && nums[0] > 0) {
        let n = nums[0];
        if (nums.length === 1 + 2 * n * n) {
            let Aflat = nums.slice(1, 1 + n * n);
            let Bflat = nums.slice(1 + n * n);
            return { n, A: toMatrix(Aflat, n), B: toMatrix(Bflat, n) };
        }
        
    }


    let possible = nums.length / 2;
    let n = Math.floor(Math.sqrt(possible));
    if (n * n * 2 === nums.length) {
        let Aflat = nums.slice(0, n * n);
        let Bflat = nums.slice(n * n);
        return { n, A: toMatrix(Aflat, n), B: toMatrix(Bflat, n) };
    }

    return { error: 'Input format not recognized. Use: n, A-elements..., B-elements... or provide exactly 2*n*n numbers.' };
}

function toMatrix(flat, n) {
    let M = [];
    for (let i = 0; i < n; i++) M.push(flat.slice(i * n, (i + 1) * n));
    return M;
}

function nextPowerOfTwo(n) {
    let p = 1;
    while (p < n) p <<= 1;
    return p;
}

function padMatrix(A, n, m) {
    let M = Array.from({ length: m }, (_, i) => Array.from({ length: m }, (_, j) => (i < n && j < n) ? A[i][j] : 0));
    return M;
}

function unpadMatrix(A, n) {
    return A.slice(0, n).map(r => r.slice(0, n));
}

function addMatrix(A, B) {
    let n = A.length;
    let C = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++)
        for (let j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
    return C;
}

function subMatrix(A, B) {
    let n = A.length;
    let C = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++)
        for (let j = 0; j < n; j++)
            C[i][j] = A[i][j] - B[i][j];
    return C;
}

function splitMatrix(A) {
    let n = A.length;
    let k = n / 2;
    let A11 = Array.from({ length: k }, () => Array(k).fill(0));
    let A12 = Array.from({ length: k }, () => Array(k).fill(0));
    let A21 = Array.from({ length: k }, () => Array(k).fill(0));
    let A22 = Array.from({ length: k }, () => Array(k).fill(0));
    for (let i = 0; i < k; i++)
        for (let j = 0; j < k; j++) {
            A11[i][j] = A[i][j];
            A12[i][j] = A[i][j + k];
            A21[i][j] = A[i + k][j];
            A22[i][j] = A[i + k][j + k];
        }
    return { A11, A12, A21, A22 };
}

function combineMatrix(C11, C12, C21, C22) {
    let k = C11.length;
    let n = k * 2;
    let C = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < k; i++)
        for (let j = 0; j < k; j++) {
            C[i][j] = C11[i][j];
            C[i][j + k] = C12[i][j];
            C[i + k][j] = C21[i][j];
            C[i + k][j + k] = C22[i][j];
        }
    return C;
}

function strassenMultiply(A, B) {
    let n = A.length;
    if (n === 1) return [[A[0][0] * B[0][0]]];
    if (n % 2 !== 0) throw new Error('Matrix size must be power of two after padding');

    let { A11, A12, A21, A22 } = splitMatrix(A);
    let { A11: B11, A12: B12, A21: B21, A22: B22 } = splitMatrix(B);

    let M1 = strassenMultiply(addMatrix(A11, A22), addMatrix(B11, B22));
    let M2 = strassenMultiply(addMatrix(A21, A22), B11);
    let M3 = strassenMultiply(A11, subMatrix(B12, B22));
    let M4 = strassenMultiply(A22, subMatrix(B21, B11));
    let M5 = strassenMultiply(addMatrix(A11, A12), B22);
    let M6 = strassenMultiply(subMatrix(A21, A11), addMatrix(B11, B12));
    let M7 = strassenMultiply(subMatrix(A12, A22), addMatrix(B21, B22));

    let C11 = addMatrix(subMatrix(addMatrix(M1, M4), M5), M7);
    let C12 = addMatrix(M3, M5);
    let C21 = addMatrix(M2, M4);
    let C22 = addMatrix(subMatrix(addMatrix(M1, M3), M2), M6);

    return combineMatrix(C11, C12, C21, C22);
}

