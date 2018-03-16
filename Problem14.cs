using System;
using System.Collections.Generic;
using System.Diagnostics;


namespace euler {
    class Problem14 {

        public static void Main(string[] args) {
            new Problem14().Solve();
            new Problem14().SolveWithCache();
            //new Problem14().SolveWithRecursion();
            new Problem14().SolveWithRecursionArray();
        }

        public void Solve() {
            Stopwatch clock = Stopwatch.StartNew();

            const int number = 10000000;
               
            long sequenceLength = 0;
            long startingNumber = 0;
            long sequence;
            

            for (int i = number / 2 + 1; i <= number; i += 2) {
				if (i % 3 == 2) {
					continue;
				}
				switch (i % 32) {
					case 3:
					case 5:
					case 13:
					case 17:
					case 19:
					case 21:
					case 23:
					case 29:
						continue;
				}
                int length = 1;
                sequence = i;
                while (sequence > 1) {
                    sequence = sequence % 2 == 0 ? sequence >> 1 : sequence * 3 + 1;
                    length++;
                }
               
                //Check if sequence is the best solution
                if (length > sequenceLength) {
                    sequenceLength = length;
                    startingNumber = i;
                }
            }
            
            clock.Stop();
            Console.WriteLine("The starting number {0} produces a sequence of {1}.", startingNumber, sequenceLength);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }


        public void SolveWithCache() {
            Stopwatch clock = Stopwatch.StartNew();

            const int number = 10000000;

            int sequenceLength = 0;
            int startingNumber = 0;
            long sequence;

            int[] cache = new int[number + 1];
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

            clock.Stop();
            Console.WriteLine("The starting number {0} produces a sequence of {1}.", startingNumber, sequenceLength);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);

        }


        private Dictionary<long, int> recCache;

        public void SolveWithRecursion() {
            Stopwatch clock = Stopwatch.StartNew();

            const int number = 1000000;
            int longestSeqIndex = 0;
            int longestSeq = 0;
            int sequenceLength = 0;

            recCache = new Dictionary<long,int>();
                        
            
            recCache.Add(1, 1);

            for (int i = 2; i <= number; i++) {
                sequenceLength = getLength(i);
                              
                //Check if sequence is the best solution
                if (sequenceLength > longestSeq) {
                    longestSeqIndex = i;
                    longestSeq = sequenceLength;
                }
            }

            clock.Stop();
            Console.WriteLine("The starting number {0} produces a sequence of {1}.", longestSeqIndex, longestSeq);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }


        private int getLength(long i) {
            int chainLength = 0;
            if (recCache.TryGetValue(i, out chainLength)) return chainLength;

            if (i % 2 == 0) {
                chainLength = 1 + getLength(i/2);                            
            } else {
                chainLength = 1 + getLength(3*i +1);                
            }

            recCache.Add(i, chainLength);
            return chainLength;
        }


        private int[] recArrayCache;

        public void SolveWithRecursionArray() {
            Stopwatch clock = Stopwatch.StartNew();

            const int number = 10000000;
            int longestSeqIndex = 0;
            int longestSeq = 0;
            int sequenceLength = 0;

            recArrayCache = new int[number+1];
            recArrayCache[1] = 1;

            for (int i = 2; i <= number; i++) {
                sequenceLength = getArrayLength(i);

                //Check if sequence is the best solution
                if (sequenceLength > longestSeq) {
                    longestSeqIndex = i;
                    longestSeq = sequenceLength;
                }
            }

            clock.Stop();
            Console.WriteLine("The starting number {0} produces a sequence of {1}.", longestSeqIndex, longestSeq);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
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
        }


    }
}
