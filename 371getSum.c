#include <stdio.h>

int getSum(int a, int b) {
	int sum = 0;
	int c = 0;
	int d = 0;
	while (a & b) {
		c = a ^ b;
		d = (a & b) << 1;
		a = c;
		b = d;
	}
	sum = a ^ b;
	return sum;
}

int main(void) {
	printf("%d\n", getSum(4, 5));
	return 0;
}