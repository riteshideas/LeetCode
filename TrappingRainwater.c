#include <stdio.h> 
#include <stdbool.h>
#include <stdlib.h>


int trap(int* height, int heightSize);
bool validateForZeroValues(int* height, int heightSize);

int main() {
	int height[132] = {1000,999,998,997,996,995,994,993,992,991,990,989,988,987,986,985,984,983,982,981,980,979,978,977,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966};
	printf("%d\n", trap(height, 132));
	return 0;
}

bool validateForZeroValues(int* height, int heightSize) {
	int desendingRepeat = 0;
	bool returnValue = false;
	for (int i = 0; i < heightSize; i++) {
		if (i != heightSize - 1) {
			if (height[i] >= height[i + 1]) {
				desendingRepeat ++;
			}
		}
	}

	if (desendingRepeat + 1 == heightSize) returnValue = true;


	return returnValue;
}

int trap(int* height, int heightSize) {

	int rainwater = 0;
	int highestElement = 0;

	int a = 0;
    int b = 0;
    int c = 0;
    int d = 0;
    int e = 0;
    int f = 0;
    int g = 0;
    int h = 0;
    int i = 0;
    int j = 0;

    int splitPoint = 0;

    bool firstHalfBool = false;
    bool secondHalfBool = false;
    
    for (i = 0; i < heightSize;i++) {
        if (height[i] > highestElement) highestElement = height[i];
    }

    if (validateForZeroValues(height, heightSize)) {
    	return 0;
    }


    if (highestElement > 1) {
    	
        int infoList[highestElement][heightSize];
        int infoList2[highestElement][heightSize];
    
        
        for (a = 0; a < highestElement; a++) {
            for (b = 0; b < heightSize; b++) {
    
                if (height[b] != 0) {
                    infoList2[a][b] = 1;
                    height[b] = height[b] - 1;
                } else {
                    infoList2[a][b] = 0;
                }
            }
        }
    
        for (c = 0; c < highestElement; c++) {
            for (d = 0; d < heightSize; d++) {
                infoList[c][d] = infoList2[highestElement-(c+1)][d];
            }
        }
    
    
    
        for (e = 0; e < highestElement; e++) {
            for (f = 0; f < heightSize; f++) {
    
                firstHalfBool = false;
                secondHalfBool = false;
    
                if (infoList[e][f] == 0 && f != 0 && f != heightSize - 1) {
    
    
                    splitPoint = f;
                    int firstHalf[f + 1];
                    int secondHalf[heightSize - f - 1];
                    int z = 0;
    
                    for (i = 0; i < heightSize; i++) {
                        if (i <= splitPoint) {
                            firstHalf[i] = infoList[e][i];
                        } else {
                            secondHalf[z] = infoList[e][i];
                            z++;
                        }
                    }

                    if(validateForZeroValues(firstHalf,f)) return 0;
    
    
                    for (g = 0; g < f; g++) {
                        if (firstHalf[g] == 1) {
                            firstHalfBool = true;
                        }
                    }
    
                    for (h = 0; h < (heightSize - f - 1); h++) {
                        if (secondHalf[h] == 1) {
                            secondHalfBool = true;
                        }
                    }
    
                    //printf("First Bool: %d, Second Bool: %d\n", firstHalfBool, secondHalfBool);
                    if (firstHalfBool && secondHalfBool) rainwater ++;
    
                }
                //printf("%d: %d %d   ", infoList[e][f], firstHalfBool, secondHalfBool);
    
            }
            //printf("\n");
        }
	
    }
	//printf("Rainwater : %d\n", rainwater);
    
	return rainwater;
}