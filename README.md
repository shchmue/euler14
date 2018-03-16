## Project Euler problem 14 solutions

### About
A collection of solution optimizations for [Project Euler problem 14](https://projecteuler.net/problem=14) regarding delay records for testing the [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture) in Python, C++ and x64 Assembly. I originally solved the problem in 2010 but recently used it to practice different optimization techniques and languages.

### Background
The procedure is very straightforward. Starting with some number `n`, follow a simple iterative procedure:
* if even, divide by 2
* if odd, multiply by 3 and add 1
* if 1, finish

These programs try all starting numbers below a specified limit and find the longest chain. There's no way to predict the length of a chain given the starting value. You can cache results, but that requires `O(n)` space. Chain length grows very slowly&mdash;the longest chain below `10^10` has `1133` steps&mdash;but that's still almost 19 gigabytes with lengths stored as 16-bit ints!

Simply, there is no practical early termination condition.<sup>1</sup>

Therefore I focused first on shrinking search space and second on using faster languages and libraries. Note that unsigned 64-bit ints can handle the intermediate values in chains for any limit up to `10^10`.

<sup>1</sup> Of course there's finishing when you reach a power of 2, but the savings there are minimal, especially when using bit shifts and [count trailing zeros](https://en.wikipedia.org/wiki/Find_first_set).

### Examples of improvements
* naive solution
* search space narrowing: `n mod 96` must be in `[1, 7, 9, 15, 25, 27, 31, 33, 39, 43, 57, 63, 73, 75, 79, 91]` - only checking `16/96` or `1/6` of the numbers<sup>2</sup>
* Python [Numba](http://numba.pydata.org/) library JIT compiler
* Python [Multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.dummy) package
* efficient wheel implementation of search space scan
* bit packing the wheel
* compiler intrinsics (specifically [bit scan forward/count trailing zeros](https://en.wikipedia.org/wiki/Find_first_set))
* pure x64 assembly implementation

   <sup>2</sup> there are several known records produced by numbers that fall outside this set (including even numbers, eg. `6, 18, 54, 31466382`). However, most with limit `10^N` fall inside it. See http://www.ericr.nl/wondrous/delrecs.html for a list of known records.

Benchmark results are included in `eul14 benchmarks.txt` and all ran on my over-the-hill `Core i7-920 @ 2.67 GHz`

### Code usage
* Each source file is self-contained and should run in the interpreter or compile as appropriate
* C++ files require C++11 for timing via `<chrono>`
* Preprocessor uses either [GCC](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html) or [MSVC++](https://docs.microsoft.com/en-us/cpp/intrinsics/x64-amd64-intrinsics-list) intrinsics
* Assembly code uses MASM syntax and was tested with [ML64](https://docs.microsoft.com/en-us/cpp/assembler/masm/masm-for-x64-ml64-exe) packaged with Visual Studio 2017

### Future plans
* C++ multithreading!
* GPU would be nice but this problem may not be a good candidate due to extreme variability and unpredictability of chain lengths

Special thanks to [Eric Roosendaal's 3x + 1 Problem compendium](http://www.ericr.nl/wondrous/) for ideas on narrowing search space
