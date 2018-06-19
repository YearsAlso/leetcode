#include <stdio.h>
#include <stdbool.h>
bool canWinNim(int n) {
	// if ((n > 0) && (n <= 3)) {
	// 	return true;
	// }

	// if ((canWinNim(n - 1)) || (canWinNim(n - 3)) || (canWinNim(n - 2))) {
	// 	return true;
	// } else {
	// 	return false;
	// }
	int fr = n % 4;
	int fr_t = n / 4;
	int fv = n % 5;
	int fv_t = n / 5;
	int sx = n % 6;
	int sx_t = n / 6;

	if (n <= 3) {
		return true;
	}
	if ((fr <= 3) || (fv <= 3) || (sx <= 3)) {
		if ((fr && fr_t) || (fv && fv_t) || (sx && sx_t)) {
			return true;
		}
	}
	return false;
}



int main(char *argc, char **argv[]) {
	int n = 0;
	scanf("%d", &n);
	printf("%d\n", (int)canWinNim(n));
	return 0;
}