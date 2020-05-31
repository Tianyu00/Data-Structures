# Data-Structures

These problems here come from coursera course 'Data Structures'.

They are about [basic data structures](#week-1-basic-data-structures), [priority queues and disjoint sets](#week-2-priority-queues-and-disjoint-sets), [hash tables](#week-3-hash-tables) and [binary search trees](#week-4-binary-search-trees).

## week 1 basic data structures
[detailed problem description](week1_basic_data_structures/week1_basic_data_structures.pdf)

#### 1 [Check brackets in the code](week1_basic_data_structures/1_brackets_in_code/check_brackets.py)

**Task** If the code in S uses brackets correctly, output “Success" (without the quotes). Otherwise, output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket. Code can contain any brackets from the set []{}(), where the opening brackets are [,{, and ( and the closing brackets corresponding to them are ],}, and ). Apart from the brackets, code can contain big and small latin letters, digits and punctuation marks.

Example:\
Input:
`foo(bar);`
Output:
`Success`

Input:
`foo([bar);`
Output:
`10`\
) doesn’t match [, so ) is the first unmatched closing bracket, so we output its position, which is 10.

#### 2 [Compute tree height](week1_basic_data_structures/2_tree_height/tree-height.py)

**Task** You are given a description of a rooted tree. Your task is to compute and output its height. Recall that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.

Example:\
Input:
```
5
4 -1 4 1 1
```
Output:
```
3
```

#### 3 [Network packet processing simulation](week1_basic_data_structures/3_network_simulation/process_packages.py)

**Task** In this problem you will implement a program to simulate the processing of network packets.

Input Format: The first line of the input contains the size 𝑆 of the buffer and the number 𝑛 of incoming network packets. Each of the next 𝑛 lines contains two numbers. 𝑖-th line contains the time of arrival 𝐴𝑖 and the processing time 𝑃𝑖 (both in milliseconds) of the 𝑖-th packet. It is guaranteed that the sequence of arrival times is non-decreasing (however, it can contain the exact same times of arrival in milliseconds — in this case the packet which is earlier in the input is considered to have arrived earlier).

Output Format. For each packet output either the moment of time (in milliseconds) when the processor began processing it or −1 if the packet was dropped (output the answers for the packets in the same order as the packets are given in the input).

Example:\
Input:
```
1 2
0 1
0 1
```
Output:
```
0
-1
```

#### 4 [Extending stack interface](week1_basic_data_structures/4_stack_with_max/stack_with_max_naive.py)

**Task** Stack is an abstract data type supporting the operations `Push()` and `Pop()`. It is not difficult to implement it in a way that both these operations work in constant time. In this problem, you goal will be to implement a stack that also supports finding the maximum value and to ensure that all operations still work in constant time. Implement a stack supporting the operations `Push()`, `Pop()`, and `Max()`.

#### 5 [Maximum in Sliding Window](week1_basic_data_structures/5_max_sliding_window/max_sliding_window.py)

**Task** Given a sequence 𝑎1, . . . , 𝑎𝑛 of integers and an integer 𝑚 ≤ 𝑛, find the maximum among {𝑎𝑖, . . . , 𝑎𝑖+𝑚−1} for every 1 ≤ 𝑖 ≤ 𝑛 − 𝑚 + 1. A naive 𝑂(𝑛𝑚) algorithm for solving this problem scans each window separately. Your goal is to design an 𝑂(𝑛) algorithm.


## week 2 priority queues and disjoint sets
[detailed problem description](week2_priority_queues_and_disjoint_sets/week2_priority_queues_and_disjoint_sets.pdf)

#### 1 [Convert array into heap](week2_priority_queues_and_disjoint_sets/1_make_heap/build_heap.py)

**Task** In this problem you will convert an array of integers into a heap. This is the crucial step of the sorting algorithm called HeapSort. It has guaranteed worst-case running time of 𝑂(𝑛 log 𝑛) as opposed to QuickSort’s average running time of 𝑂(𝑛 log 𝑛). QuickSort is usually used in practice, because typically it is faster, but HeapSort is used for external sort when you need to sort huge files that don’t fit into memory of your computer.

Your task is to implement this first step and convert a given array of integers into a heap. You will do that by applying a certain number of swaps to the array. Swap is an operation which exchanges elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖 and 𝑗. You will need to convert the array into a heap using only 𝑂(𝑛) swaps.

Example:\
Input:
```
5
5 4 3 2 1
```
Output:
```
3
1 4
0 1
1 3
```

#### 2 [Parallel processing](week2_priority_queues_and_disjoint_sets/2_job_queue/job_queue.py)

**Task** Task. You have a program which is parallelized and uses 𝑛 independent threads to process the given list of 𝑚 jobs. Threads take jobs in the order they are given in the input. If there is a free thread, it immediately takes the next job from the list. If a thread has started processing a job, it doesn’t interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list simultaneously, the thread with smaller index takes the job. For each job you know exactly how long will it take any thread to process this job, and this time is the same for all the threads. You need to determine for each job which thread will process it and when will it start processing.

Example:\
Input:
```
2 5
1 2 3 4 5
```
Output:
```
0 0
1 0
0 1
1 2
0 4
```

#### 3 [Merging tables](week2_priority_queues_and_disjoint_sets/3_merging_tables/merging_tables.py)

In this problem, your goal is to simulate a sequence of merge operations with tables in a database. (This is an application of disjoint sets data structure. Pls see the detail description file for more about problem description.)

Example:\
Input:
```
5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3
```
Output:
```
2
2
3
5
5
```


### week 3 hash tables
[detailed problem description]()

### week 4 binary search trees
[detailed problem description]()
