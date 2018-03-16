#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <numeric>
#include <future>
#include <sstream>

#ifdef _MSC_VER
	#include <intrin.h>
	#include <immintrin.h>
	#pragma intrinsic(_BitScanForward64, _rotr64)
#endif

void Solve(unsigned __int64 number) {
	std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

	unsigned __int64 start = number / 2 - ((number/2) % 96);
	   
	unsigned __int64 sequenceLength = 0;
	unsigned __int64 startingNumber = 0;
	unsigned __int64 sequence;
	//int modulos[16] = {1, 7, 9, 15, 25, 27, 31, 33, 39, 43, 57, 63, 73, 75, 79, 91};
	//int wheel[16] = { 6, 2, 6, 10, 2, 4, 2, 6, 4, 14, 6, 10, 2, 4, 12, 6 };
	unsigned __int64 wheel = 7800981004390409766;
	auto i = start + 1;
	size_t pos = 0;
	while (i <= number) {
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
		//i += wheel[pos];
		//pos = (pos + 1) & 15;
		i += wheel & 15;
		wheel = _rotr64(wheel, 4);
	}
	
	std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
	std::cout << startingNumber << " " << sequenceLength << " ";
	std::cout << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << "us" << std::endl;

}

int main (int argc, char* argv[]) {
	std::istringstream iss(argv[1]);
	unsigned __int64 limit;
	if(!(iss >> limit))
		std::cerr << "Invalid number " << argv[1] << std::endl;
	Solve(limit);
	return 0;
}

