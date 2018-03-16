#include <iostream>
#include <chrono>
#include <map>

void Solve() {
	std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

	const int number = 100000000;
	const int start = number / 2 - ((number/2) % 96);
	   
	int sequenceLength = 0;
	int startingNumber = 0;
	unsigned long long sequence;
	int modulos[16] = {1, 7, 9, 15, 25, 27, 31, 33, 39, 43, 57, 63, 73, 75, 79, 91};
	
	for (int j = 0; j < 16; j++) {
		for (int n = start; n <= number; n += 96) {
			int i = n + modulos[j];
			int length = 1;
			sequence = i;
			while (sequence > 1) {
				//std::cout << length << " " << sequence << std::endl;
				if (sequence % 2) {
					sequence += (sequence << 1) + 1;
				} else {
					sequence >>= 1;
				}
				length++;
			}
		   
			//Check if sequence is the best solution
			if (length > sequenceLength) {
				sequenceLength = length;
				startingNumber = i;
			}
		}
	}
	
	std::chrono::steady_clock::time_point end= std::chrono::steady_clock::now();
	std::cout << startingNumber << " " << sequenceLength << " ";
	std::cout << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << std::endl;

}

/*
void SolveWithCache() {

	const int number = 10000000;

	int sequenceLength = 0;
	int startingNumber = 0;
	long sequence;

	int cache[number + 1];
	//Initialise cache
	for (int i = 0; i <= number; i++) {
		cache[i] = -1;
	}
	cache[1] = 1;

	for (int i = number / 2 + 1; i <= number; i += 2) {
		sequence = i;
		int k = 0;
		while (sequence != 1 && sequence >= i) {
			k++;
			sequence = sequence % 2 == 0 ? sequence >> 1 : sequence * 3 + 1;
		}
		//Store result in cache
		cache[i] = k + cache[sequence];

		//Check if sequence is the best solution
		if ((cache[i] > -1) && (cache[i] > sequenceLength)) {
			sequenceLength = cache[i];
			startingNumber = i;
		}
	}

	std::cout << "The starting number " << startingNumber << " produces a sequence of " << sequenceLength << std::endl;
	std::cout << "Solution took " << std::endl;

}


public std::map<long, int> recCache;
void SolveWithRecursion() {

	const int number = 1000000;
	int longestSeqIndex = 0;
	int longestSeq = 0;
	int sequenceLength = 0;

	
	recCache[1] = 1;

	for (int i = 2; i <= number; i++) {
		sequenceLength = getLength(i);
					  
		//Check if sequence is the best solution
		if (sequenceLength > longestSeq) {
			longestSeqIndex = i;
			longestSeq = sequenceLength;
		}
	}

	std::cout << "The starting number " << longestSeqIndex << " produces a sequence of " << longestSeq << std::endl;
	std::cout << "Solution took " << std::endl;
}


private int getLength(long i) {
	int chainLength = 0;
	if (recCache.count(i)) return recCache[i];

	if (i % 2 == 0) {
		chainLength = 1 + getLength(i/2);                            
	} else {
		chainLength = 1 + getLength(3*i +1);                
	}

	recCache[i] = chainLength;
	return chainLength;
}


private int recArrayCache;

void SolveWithRecursionArray() {

	const int number = 10000000;
	int longestSeqIndex = 0;
	int longestSeq = 0;
	int sequenceLength = 0;

	recArrayCache = int[number+1];
	recArrayCache[1] = 1;

	for (int i = 2; i <= number; i++) {
		sequenceLength = getArrayLength(i);

		//Check if sequence is the best solution
		if (sequenceLength > longestSeq) {
			longestSeqIndex = i;
			longestSeq = sequenceLength;
		}
	}

	std::cout << "The starting number " << longestSeqIndex << " produces a sequence of " << longestSeq << std::endl;
	std::cout << "Solution took " << std::endl;
}


private int getArrayLength(long i) {
	int chainLength = 0;
	if (i < recArrayCache.Length && recArrayCache[i] != 0) return recArrayCache[i];

	if (i % 2 == 0) {
		chainLength = 1 + getArrayLength(i / 2);
	} else {
		chainLength = 1 + getArrayLength(3 * i + 1);
	}

	if (i < recArrayCache.Length) recArrayCache[i] = chainLength;
	return chainLength;
}*/

int main () {
	Solve();
	//new Problem14().SolveWithCache();
	//new Problem14().SolveWithRecursion();
	//new Problem14().SolveWithRecursionArray();
	return 0;
}

