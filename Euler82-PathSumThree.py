#Project Euler problem #82
#Path sum: three ways
#Status: unsolved

def pathFinder(gr)
    workingGrid = [[None] * len(gr[0]) for _ in range(len(gr))]
    workingGrid[:][-1] = gr[:][-1]
    
        
        
