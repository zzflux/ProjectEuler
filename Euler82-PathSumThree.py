#Project Euler problem #82
#Path sum: three ways
#Status: unsolved

FILENAME_REAL = 'p082_matrix.txt'
FILENAME_TEST = 'p82_test.txt'
FILENAME = FILENAME_TEST

def minPathSum(gr, startpoint, lastpoint, cache):
    #if not cache:
    #    print('Cache started empty')
    try:
        return cache[startpoint]
    except KeyError:
        try:
            x = gr[startpoint[0]][startpoint[1]]
        except IndexError:
            cache[startpoint] = float('inf')
            return float('inf')
        if not cache:
            for r in range(len(gr)):
                cache[(r, len(gr[0]) - 1)] = gr[r][len(gr[0]) -1]
        #print('Cache is', len(cache))
        ans = min(minPathSum(gr, (startpoint[0] + delta[0], startpoint[1] + delta[1]), startpoint, cache) for delta in ((-1, 0), (1, 0), (0, 1)) if (startpoint[0] + delta[0], startpoint[1] + delta[1]) != lastpoint)
        cache[startpoint] = ans + x
        return ans + x
    


if __name__ == '__main__':
    cache = dict()
    with open(FILENAME) as file:
        grid = [[int(x) for x in line.split(',')] for line in file]

    #print('len cache before:', len(cache))
    #minPathSum(grid, (0,0), (-1,-1), cache)
    #print('len cache after:', len(cache))
    
    print('Answer:', min(minPathSum(grid, (r, 0), (-1, -1), cache) for r in range(len(grid))))
    
        
        
