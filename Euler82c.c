/*
* Project Euler problem #82
* Path sum: three ways
* Jon McMahon, April 2016
* Unsolved
*/

#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>

#define MAX_LINE 512
#define GRID_HEIGHT 5
#define GRID_WIDTH 5
#define DELIM ","

const char *FILENAME = "p82_test.txt";

void giveUp(const char *msg){
    fprintf(stderr, "Giving up: %s\n", msg);
    abort();
}

int minPathSum(int field[GRID_HEIGHT][GRID_WIDTH], int sRow, int sCol, int cutoff, int startingSum, int lastRow, int lastCol){
    int rval, ret;
    int runningMin = INT_MAX;
    if(sCol == (GRID_WIDTH - 1)){
        return field[sRow][sCol] + startingSum;
    }
    if(startingSum > cutoff){
        return -1;
    }
    //printf("checkpoint 1\n");
    if(sRow != 0 && lastRow != (sRow - 1)){
        rval = minPathSum(field, sRow - 1, sCol, cutoff, startingSum + field[sRow][sCol], sRow, sCol);
        if(rval != -1 && rval < runningMin){
            runningMin = rval;
        }
    }
    //printf("checkpoint 2\n");
    if(sRow != (GRID_HEIGHT - 1) && lastRow != (sRow + 1)){
        rval = minPathSum(field, sRow + 1, sCol, runningMin, startingSum + field[sRow][sCol], sRow, sCol);
        if(rval != -1 && rval < runningMin){
            runningMin = rval;
        }
    }
    //printf("checkpoint 3\n");
    if(sCol + 1 != lastCol){
        rval = minPathSum(field, sRow, sCol + 1, runningMin, startingSum + field[sRow][sCol], sRow, sCol);
        if(rval != -1 && rval < runningMin){
            runningMin = rval;
        }
    }
    ret = startingSum + field[sRow][sCol] + runningMin;
    return ret;
}

int main(void){
    char tmp[MAX_LINE];
    int grid[GRID_HEIGHT][GRID_WIDTH];
    int r, c, p, cutoffSum, minval;
    char *s;
    FILE *matrixFile = fopen(FILENAME, "r");
    if(!matrixFile){
        giveUp("could not open file");
    }
    for(r = 0; r < GRID_HEIGHT; r++){
        fgets(tmp, MAX_LINE, matrixFile);
        if(feof(matrixFile)){
            giveUp("grid not tall enough");
        }
        strtok(tmp, "\n");
        s = strtok(tmp, DELIM);
        for(c = 0; c < GRID_WIDTH; c++){
            if(!s){
                giveUp("grid rows not wide enough");
            }
            grid[r][c] = atoi(s);
            s = strtok(NULL, DELIM);
        }
    }
    fclose(matrixFile);
    cutoffSum = 0;
    for(c = 0; c < GRID_WIDTH; c++){
        cutoffSum += grid[0][c];
    }
    printf("cutoff = %d\n", cutoffSum);
    minval = cutoffSum;
    for(r = 0; r < GRID_HEIGHT; r++){
        p = minPathSum(grid, r, 0, minval, 0, -1, -1);
        if(p < minval){
            minval = p;
        }
    }
    printf("Answer: %d\n", minval);
    printf("done");
    return 0;
}
