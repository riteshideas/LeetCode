#include <stdio.h>

int main() {
	int f = 2;
	int infoList[10] = {1,2,3,4,5,6,7,8,9,10};
	int splitPoint = f;
	int firstHalf[f+1];
	int secondHalf[10 - f - 1];
	int z = 0;

	for (int i = 0; i < 10; i++) {
		printf("%d  ", infoList[i]);
		if (i <= splitPoint) {
			firstHalf[i] = infoList[i];
		} else {
			secondHalf[z] = infoList[i];
			z ++;
		}
	}
	printf("\n");

	for (int a = 0; a < 3; a++) {
		printf("%d  ", firstHalf[a]);
	}
	printf("\n");

	for (int a = 0; a < 7; a++) {
		printf("%d  ", secondHalf[a]);
	}
	printf("\n");

	return 0;
}