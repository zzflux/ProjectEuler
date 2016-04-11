//Project Euler problem #34
//Digit factorials
//Jon McMahon March 2016
#include <stdio.h>

#define ABSOLUTE_MAX 10000000

const int DIGIT_FACTORIALS[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};

int sumDigitFactorials(int x){
    int sum = 0;
    do{
        sum += DIGIT_FACTORIALS[x % 10];
        x /= 10;
    }while(x > 0);
    return sum;
}

int main(void){
    int current;
    long int runningSum = 0;
    for(current = 3; current < ABSOLUTE_MAX; current++){
                if(current == sumDigitFactorials(current)){
                            runningSum += current;
                }
    }
    printf("Answer: %ld", runningSum);
    return 0;
}


        
    
    
