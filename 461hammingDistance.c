#include <stdio.h>

int hammingDistance(int x, int y) {
	int n = x;
	n ^= y;
	int sum = 0;
	while (n > 0) {
		if (n % 2 == 1) {
			sum++;
		}
		printf("n==>%d\n", n);
		n = n >> 1;
	}
	return sum;
}

int main(void) {
	int n = hammingDistance(1, 4);
	printf("%d\n", n);
	return 0;
}