#include <chrono>
#include <iostream>
#include <sstream>

extern "C" unsigned __int64 Collatz(unsigned __int64 limit);

int main(int argc, char* argv[])
{
	std::istringstream iss(argv[1]);
	unsigned __int64 limit;
	if (!(iss >> limit))
		std::cerr << "Invalid number " << argv[1] << std::endl;

	std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
	auto result = Collatz(limit);
	std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();

	std::cout << result << " ";
	std::cout << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() << "us" << std::endl;
}