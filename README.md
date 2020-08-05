# Leetcode-Problems

### 1. Two Sum
一次遍历  
使用dict记录遍历过的元素num，并判断target-num是否在dict中

### 2. Add Two Numbers
同时遍历双链表  
注意：1. 可以使用dummyHead；2. 最终的进位非0要加一位

### 3. Longest Substring Without Repeating Characters
记录头尾指针head-tail，遍历str的同时，在[head, tail)中找tail是否存在  
> 可以使用dict查找，但是发现不如find函数快

### 4. Median of Two Sorted Arrays
核心思想：最均衡的情况下，其中一个数组的median//2位置刚好是median，另一个数组的median//2位置是median-1。  
否则，当其中一个数组>median的数更多就会导致另一个数组<median的数更多，这样median//2较小的部分也一定是<median的。
因此每次二分都可以直接去除median//2较小的部分。