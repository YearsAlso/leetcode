#include <stdio.h>

int hammingWeight(uint32_t n) {
    if(n==0) return 0;
    int hm_weigth=0;
    while(n>0){
        if(n&&1){
            hm_weigth+=1;
        }
        n>>1;
    }
    return hm_weigth;
}

int main(void){
    int w = hammingWeight(1);
    printf("%d\n",w);
    return 0;
}

