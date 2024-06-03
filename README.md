# for i in rang(0, N)
    # Loops from 0 to N-1


# add negative sign to a positive number
    # negative = 0 - positive

# add positive sign to a negative number
    # positive = abs(negative)

# reverse a string
    # str_rever = given_str[::-1]

# add last digit of a number to another number
    # result = result*10 + n%10
    # n = int(n / 10)

# Slicing in Python

a = "abcdef"
index = 0
number_of_elemenets = 4

print(a[index:number_of_elements])

Gives output: abcd

# Slicing in JS

```js
const a = "abcdef";

// abcd
console.log(a.slice(0,4))
```

# deleting ith element from array JS | replacing n elements

```js
const months = ['Jan', 'March', 'April', 'June'];

// add element (feb) at index 1 after deleting 0 elements
months.splice(1, 0, 'Feb');

// delete element at index 1
months.splice(1, 1);

console.log(months)
```

# pop first element from array | delete first element from array 

```js
var arr = [1, 2, 3, 4]; 
var theRemovedElement = arr.shift(); // theRemovedElement == 1
console.log(arr); // [2, 3, 4]
```

# push elements to start of array JS

```js
const array1 = [1, 2, 3];

console.log(array1.unshift(4, 5));
// Expected output: 5

console.log(array1);
// Expected output: Array [4, 5, 1, 2, 3]
```

# push and pop at the end of array js

```js
let fruits = ["apple", "banana", "kiwi"];
console.log(fruits); // ["apple", "banana", "kiwi"]

fruits.push("orange");
console.log(fruits); // ["apple", "banana", "kiwi", "orange"]

fruits.pop();
console.log(fruits); // ["apple", "banana", "kiwi"]
```

# Problems

## Two Sum

```js
var twoSum = function (nums, target) {
  const diff_obj = {};
  let diff = undefined;
  let result;
  nums.every((value, index) => {
    diff = target - value;
    if (diff in diff_obj) {
      result = [diff_obj[diff], index];
      return false;
    } else {
        diff_obj[value] = index;
    }
    return true
  });

  return result;
};
```


## Reverse Integer

```py
def ans(n):
    sign = 0
    if n < 0:
        n = abs(n)
        sign = 1
    result = 0
    while n:
        result = result*10 + n%10
        n = int(n / 10)
    
    if sign:
        result = 0 - result
    if result < a or result > b:
        return 0
    else:
        return result
```

## Roman to Integer (upto 1000)

```js
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  let max_index = s.length - 1
  if (max_index < 0) {
    return -1
  }
  let dict = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 }

  let cur = 0
  let next = 1
  let sum = 0
  while (next <= max_index) {
    if (dict[s[next]] <= dict[s[cur]]) {
      sum += dict[s[cur]]
      cur++
      next++
      continue
    }
    sum = sum + (dict[s[next]] - dict[s[cur]])
    cur += 2
    next += 2
  }
  if (cur <= max_index) {
    sum += dict[s[cur]]
  }
  return sum
}
```

## Longest Common Prefix

```js
var longestCommonPrefix = function(strs) {
    let pref = strs[0];
    let prefLen = pref.length;

    for (let i = 1; i < strs.length; i++) {
        let s = strs[i];
        while (pref !== s.substring(0, prefLen)) {
            prefLen--;
            if (prefLen === 0) {
                return "";
            }
            pref = pref.substring(0, prefLen);
        }
    }

    return pref;    
};
```


## Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

```js
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let len = s.length
  if (s <= 0 || len > 10000) {
    return false
  }
  let stack = []
  let char2int = { '(': 1, ')': 2, '{': 10, '}': 11, '[': 20, ']': 21 }
  for (let i = 0; i < len; i++) {
    if (char2int[s[i]] != (stack.slice(-1))[0]+1) {
      stack.push(char2int[s[i]])
      continue
    }
    stack.pop()

  }
  if (stack.length) {
    return false
  }
  return true
}
```

## Remove Duplicate from Sorted Array

>  remove the duplicates in-place 
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let max = nums[nums.length - 1]

  //  pointer to first unique value 
  let ptr_a = 0

  //  pointer to search second unique value 
  let i = 1
  while (nums[ptr_a] < max) {

    // if second value is a unique value then it must be a greater value
    // since you have found second unique value
    //      move it next to first unique value and increase both pointers
    if (nums[i] > nums[ptr_a]) {
      nums[ptr_a + 1] = nums[i]
      ptr_a++
      i++
    }

    // if if second value is same as the first value
    // increase this pointer to search for a unique value
    else {
      i++
    }
  }

  return ptr_a+1
}

```


## Remove Element from Array

```js
var removeElement = function (nums, val) {

  //  pointer to the element to be removed inplacely 
  let ptr_val

  //   count of total occurances of the item to be removed
  let k = 0

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == val) {
      ptr_val = i
      break
    }
  }


  for (let i = ptr_val; i < nums.length; i++) {

    // if current item is not the one to be removed then
    // the move it left to the place of the item which should be removed
    if (nums[i] != val) {
      nums[ptr_val] = nums[i]
      ptr_val++
    }

    // if the current number is the one to be removed then increase count
    else{
        k++
    }
  }
  return nums.length-k
}
```

## Find the Index of the First Occurrence in a String

```js
var strStr = function (haystack, needle) {
  if (needle == '') {
    return 0
  }
  if (needle.length > 50000 || haystack.length > 50000) {
    return -1
  }
  if (needle.length > haystack.length) {
    return -1
  }
  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] == needle[0]) {
      if (haystack.substring(i, i + needle.length) == needle) {
        return i
      }
    }
  }
  return -1
}
```

## Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

```js
var searchInsert = function (nums, target) {
  let end = nums.length - 1
  if (end == -1) {
    return 0
  }
  if (target < -10000 || target > 10000) {
    return -1
  }
  let start = 0
  let mid = Math.ceil((start + end) / 2)
  while (true) {
    if (nums[mid] > target) {
      if (mid == start) {
        return mid
      }
      end = mid - 1
      mid = Math.floor((start + end) / 2)
      continue
    }
    if (nums[mid] < target) {
      if (mid == end) {
        return mid + 1
      }
      start = mid + 1
      mid = Math.floor((start + end) / 2)
      continue
    }
    if (nums[mid] == target) {
      return mid
    }
  }
}
```

## Pow || Binary Exponentiation

```js
// For a much better version view 2.js
// This Code doesn't handle negative exponents
// This Code doesn't handle fractional exponents


/*
        EXPLANATION

params: base, exponent : (base^e).residual

while exponent greater than 1
    if exponent even
        then half it and take square of base
    else
        subtract 1 from exponent, multiply residual by base to make equation balanced,
        and half exponent and take square of base

    return residual*base

then handle edge cases
*/


const binary_expo = (base, exponent) => {
  res = 1

  if(base == 0 && exponent==0){
    throw Error("Math Error")
  }

  if (exponent==0 || base==1){
    return 1
  }
  if(base == -1 ){
    if(exponent & 1){
      return -1
    }
    return 1
  }

  while (exponent>1) {
    if (!(exponent & 1)) {
      // u cab further optimize by recognizing the fact that 
      // below two lines are also in else case
      exponent = exponent >> 1
      base = base * base
    } else {
      exponent = exponent >> 1

      // update res first then update base
      // note that negative base will be handles here automatically
      res = res * base
      base = base * base

    }
  }
  return res*base
}

console.log(binary_expo(2.5, 2))
```

## Climbing Stairs | Fibonacci

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

```js
const fib = (n) => {
    let f1 = 0
    let f2 = 1
    n = n - 1
    while (n--) {
      ;[f1, f2] = [f2, f1 + f2]
    }
    return f2
  }
```

```js
var climbStairs = function (n) {
  let one = 1
  let two = 2
let t
  for (let i = 2; i <= n; i++) {
      t = one
      one = two
      two = t+two
  }
  return one
}
```

```js
const fn = (n)=>{
    if(n==0){
        return 0
    }
    if(n==1){
        return 1
    }
    else{
        return fn(n-1)+fn(n-2)
    }
}
```

## Merge Sorted arrays

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

```js
 var merge = function (nums1, m, nums2, n) {
    let len = n + m - 1
    m--
    n--
    while (n >= 0) {
      if (nums1[m] > nums2[n]) {
        nums1[len--] = nums1[m--]
        continue
      }
      nums1[len--] = nums2[n--]
    }
  }
```


## Pascals Triangle
Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

```js
var generate = function (numRows) {
  var arr = []
  for (var i = 0; i < numRows; i++) {
    arr[i] = []
    arr[i][0] = 1
    for (var j = 1; j < i; j++) {
      arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    }
    arr[i][i] = 1
  }
  return arr
}
```

## Best Time to Buy and Sell Stock | Max Subarray sum


/*
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
*/


/*
Algo: 
Can be optimized to great extent, written like this for easier understanding
and for similarity with Kadane to be evident

Two for loop algo is trivial. Using Kadane Algo here
make a relative_prices array (prices[i]-prices[i-1])
set first element of relative prices to be 0 
find max subarray sum of relative_pricess and return it.
*/


/*
Runtime: 148 ms, faster than 11.04% of JavaScript online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 52.3 MB, less than 5.50% of JavaScript online submissions for Best Time to Buy and Sell Stock.
*/

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProfit = function (nums) {
  var max = (moving_sum = Number.NEGATIVE_INFINITY)
  var relative_prices = nums.map((e, i) => nums[i] - nums[i - 1])
  relative_prices[0] = 0
  for (var i = 0; i < relative_prices.length; i++) {
    moving_sum =
      moving_sum + relative_prices[i] > relative_prices[i]
        ? moving_sum + relative_prices[i]
        : relative_prices[i]
    if (moving_sum > max) {
      max = moving_sum
    }
  }
  return max
}

console.log(maxSubArray([7, 1, 5, 3, 6, 4]))
```

## Valid Palindrome

```js
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  var parsed_str = s.toLowerCase().replace(/[^A-Za-z0-9]/g, '')
  var tail = parsed_str.length - 1
  var head = 0
  for (var i = 0; head <= tail; i++) {
    if (parsed_str[head++] != parsed_str[tail--]) {
      return false
    }
  }
  return true
}
```

## Find single non duplicate element, all else are repeated twice

Algo: XOR between all elements of array.

```js
var singleNumber = function(nums) {
    let res = nums[0]
    for(var i=1; i<nums.length; i++){
        res ^= nums[i]
    }
    return res
};

console.log(1^4)
```

## Plus One

/*
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
*/

/*
Algo:

last_index = length of array-1

while last_index element is 9 and last_index!=0:
    update last_index element to 0
    last_index = last_index-1

if element at last index is 9 and last index is 0:
        update last_index element to 0
        unshift array with 1
        return
return arr[last_index] = arr[last_index]+1
*/


/*
Runtime: 100 ms, faster than 7.96% of JavaScript online submissions for Plus One.
Memory Usage: 38.3 MB, less than 96.93% of JavaScript online submissions for Plus One.
*/

```js
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  let index2incr = digits.length - 1
  while (digits[index2incr] == 9 && index2incr) {
    digits[index2incr] = 0
    index2incr--
  }
  if (index2incr == 0 && digits[index2incr] == 9) {
    digits[index2incr] = 0
    digits.unshift(1)
    return digits
  }
  digits[index2incr]++
  return digits
}

// test
let digits = [9]
console.log(plusOne(digits))
```

## Add Binary

```js
const addBinary = (a, b) => {
  let obj = { a: a, b: b }
  let max_len = a.length > b.length ? a.length : b.length
  let small_str = a.length < b.length ? 'a' : 'b'
  let carry = '0'
  let sum = ''
  let l = max_len - obj[small_str].length

  for (let i = 0; i < l; i++) {
    obj[small_str] = '0' + obj[small_str]
  }

  console.log(obj['a'], obj['b'])
  for (let i = max_len - 1; i >= 0; i--) {
    if (obj['a'][i] == '1' && obj['b'][i] == '1') {
      sum = carry + sum
      carry = '1'
      continue
    }
    if (obj['a'][i] == '0' && obj['b'][i] == '0') {
      sum = carry + sum
      carry = '0'

      continue
    }
    if (carry == '1') {
      sum = '0' + sum
    } else {
      sum = '1' + sum
    }
  }
  if (carry == '1') sum = '1' + sum
  return sum
}

```

## Square root

```js
var mySqrt = function (x) {
    
    let s = 0
    while (s * s <= x) {
      s++
    }
  
    return s-1
  }
console.log(mySqrt(1024))
```


## Majority Element in array
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

```
Input: nums = [3,2,3]
Output: 3
```


```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  var dict = {}
  var n = parseInt(nums.length / 2)
  for (var i = 0; i < nums.length; i++) {
    if (dict.hasOwnProperty(nums[i])) {
      dict[nums[i]] = dict[nums[i]] + 1
      if (dict[nums[i]] > n) {
        return nums[i]
      }
      continue
    }

    dict[nums[i]] = 1
  }
  return nums[0]
}
```


## reverse bits

```js
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int ans = 0;
        for( int i= 0; i < 32 ;i++){
            ans = (ans << 1) | (n&1);
            n = n >> 1;
        }
        return ans;
    }
}
```

## Number of 1 Bits

```js
/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (num) {
  var count = 0
  while (num) {
    if (num & 1) {
      count++
    }
    num >>>= 1
  }
  return count
}
```

## Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



```js
* @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
  return f2(n, {})
}

var f2 = function (n, dict) {
  // this if must be prior to next one
  if (n == 1) {
    return true
  }

  if (n == 0 || dict.hasOwnProperty(n)) {
    return false
  }
  dict[n] = 1

  var sqrs_sum = 0
  var num = 0
  while (n) {
    num = n % 10
    sqrs_sum += num * num
    n = Math.floor(n / 10)
  }
  return f2(sqrs_sum, dict)
}
```

## Count Primes | Seive

```js
var countPrimes = function (n) {
    let arr = new Uint8Array(n)
  
    let count = 0
  
    for (let i = 2; i < n; i++) {
      if (arr[i]) {
        continue
      }
      count++
  
      for (let j = i * i; j < n; j = j + i) {
        arr[j] = 1
      }
    }
  
    return count
  }
```

## Isomorphic

```js
var isIsomorphic = function (s, t) {
  var len = s.length
  if (len != t.length) {
    false
  }
  var map1 = {}
  var map2 = {}

  for (var i = 0; i < len; i++) {
    if (map1.hasOwnProperty(s[i]) || map2.hasOwnProperty(t[i])) {
      if (map1[s[i]] != map2[t[i]]) {
        return false
      }
      continue
    }
    map1[s[i]] = i
    map2[t[i]] = i
  }
  return true
}
```

# DSA Tree

## Binary Tree Inorder Traversal

```js
var inorderTraversal = function (root) {
  var stack = []
  var result = []
  while (root || stack.length) {
    if (root) {
      stack.push(root)
      root = root.left
      continue
    }
    root = stack.pop()
    result.push(root.val)
    root = root.right
  }

  return result
}
```


```js
var inorderTraversal = function(root) {
    var arr = [0,]
    traverse(root, arr)
    return arr.splice(1,arr.length)
};

const traverse = (root,arr)=>{
    if(!root){
        return null
    }
    traverse(root.left,arr)
        arr.push(root.val)
    traverse(root.right,arr)
}
```


## Same Tree

```js
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
    return inorderTraversal(p, q)
}

var inorderTraversal = function (root1, root2) {
    var stack1 = []
  var stack2 = []

  while (root1 || stack1.length) {
      if (root1 || root2) {
          if (!(root1!=undefined && root2!=undefined)) {
              return false
      }
      if (root1.val != root2.val) {
          return false
      }
      stack1.push(root1)
      root1 = root1.left
      stack2.push(root2)
      root2 = root2.left
      continue
    }
    root1 = stack1.pop()
    root1 = root1.right
    root2 = stack2.pop()
    root2 = root2.right
  }

  // if p and q are [] and [0] then stakcs will be empty at the end, hence don't compare stacks
  // both roots must be null,equal, at the end  
  return root1==root2
}
```

## Maximum Depth of Binary Tree

```
bottom up approach:
    last subtree's left/right child have height 0, so return 0 in terminating condition of recursion
    last tress's root height is 1, so when it's child's return 0 then add 1
```

```js
var maxDepth = function (root) {
  if (!root) {
    return 0
  }
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right))
}
```

## BFS | Level Order traversal | Number of Levels | height | depth

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    // Check if the root is null
  if (!root) return [];

  const result = []; // Array to store level order traversal
  const queue = [root]; // Queue to perform BFS

  while (queue.length > 0) {
    const levelSize = queue.length; // Number of nodes at current level
    const currentLevel = [];

    // Process all nodes at current level
    for (let i = 0; i < levelSize; i++) {
      const currentNode = queue.shift(); // Dequeue node from front of queue
      currentLevel.push(currentNode.val); // Add node value to current level array

      // Enqueue left and right children (if exists) for next level traversal
      if (currentNode.left) queue.push(currentNode.left);
      if (currentNode.right) queue.push(currentNode.right);
    }

    result.push(currentLevel); // Add current level to result array
  }

  return result;
};
```

## Convert Sorted Array to Binary Search Tree


## Symmetric Tree
## preorder traversal 
## postorder traversal 
## Balanced Binary Tree
## Minimum Depth of Binary Tree
## Path Sum

# DSA Linked List
## Cycle
## Intersection of Linked Lists
## Remove Linked List Elements
## Reverse Linked List

# DSA Stack
## Design a Stack
## Implement Stack with Queues

## Contains Duplicate 1
## Contains Duplicate 2
## Excel sheet columns number
## Excel sheet columns title

## Pascal's Triangle II

## Merge Two Sorted Linked Lists


## Remove Duplicates from Sorted List

