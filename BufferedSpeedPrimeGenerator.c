#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
#include <string.h>

#define integer int64_t

int main(int argc, char *argv[]){
    integer *primeList, candidate;
    long numPrimes, primesFound, x;
    char *filename;
    FILE *outfile;
    unsigned i;

    if(argc < 3){
        fprintf(stderr, "Usage: %s num file\nGenerates a newline-separated list of the first num primes and saves to file (or stdout if name is '1')\n", argv[0]);
        return 1;
    }
    numPrimes = atol(argv[1]);
    if(numPrimes <= 0){
        fprintf(stderr, "Cannot generate zero or fewer primes. That makes no sense\n");
        return 2;
    }
    filename = argv[2];
    if(!strcmp(filename, "1")){
        outfile = stdout;
    }
    else{
        outfile = fopen(filename, "w");
    }
    if(!outfile){
        fprintf(stderr, "Could not open file for writing\n");
        return 3;
    }

    primeList = malloc(sizeof(*primeList) * numPrimes);

    if(!primeList){
        fprintf(stderr, "Insufficient memory\n");
        return 4;
    }

    primeList[0] = 2;
    
    primesFound = 1;
    candidate = 3;
    while(primesFound < numPrimes){
        for(i = 0; i < primesFound; i++){
            if(primeList[i] * primeList[i] > candidate){
                primeList[primesFound] =  candidate;
                primesFound++;
                break;
            }
            if(!(candidate % primeList[i])){
                break;
            }
        }
        candidate += 2;
    }

    fprintf(outfile, "2\n");
    for(x = 1; x < primesFound; x++){
	fprintf(outfile, "%"PRId64"\n", primeList[x]);
    }

    if(outfile != stdout){
        fclose(outfile);
    }
    free(primeList);
    return 0;
}
