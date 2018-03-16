#include <iostream>
#include <chrono>
#include <map>

#ifdef _MSC_VER
	#include <intrin.h>
#endif

void Solve() {
	std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

	unsigned __int64 number = 10000000000;
	unsigned __int64 start = number / 2 - ((number/2) % 96);
	   
	unsigned __int64 sequenceLength = 0;
	unsigned __int64 startingNumber = 0;
	unsigned __int64 sequence;
	int modulos[16] = {1, 7, 9, 15, 25, 27, 31, 33, 39, 43, 57, 63, 73, 75, 79, 91};
	
	for (size_t j = 0; j < 16; j++) {
		for (unsigned __int64 n = start; n <= number; n += 96) {
			unsigned __int64 i = n + modulos[j];
			unsigned __int64 length = 1;
			sequence = i;
			while (sequence > 1) {
				//std::cout << length << " " << sequence << std::endl;
				/*if (sequence & 1) {
					sequence += (sequence << 1) + 1;
				} else {
					sequence >>= 1;
				}*/
				if (sequence & 1)
					sequence += (sequence << 1) + 1;
				#ifndef _MSC_VER
					auto times = __builtin_ctzll(sequence);
				#else
					unsigned long times;
					_BitScanForward64(&times, sequence);
				#endif
				sequence >>= times;
				length += times;
				length++;
			}
		   
			//Check if sequence is the best solution
			if (length > sequenceLength) {
				sequenceLength = length;
				startingNumber = i;
			}
		}
	}
	
	std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
	std::cout << startingNumber << " " << sequenceLength << " ";
	std::cout << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << "us" << std::endl;

}

int main () {
	Solve();
	return 0;
}

