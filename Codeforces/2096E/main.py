def test():
    n = int(input())
    arrangement = list(input())
    swap_counter = 0
    unsolved = True
    left =0
    right = n
    while unsolved:
        while(arrangement[left:left+3]==['B','B','B']):
            left+=1
        while(arrangement[right-3:right]==['P','P','P']):
            right-=1
        #print(arrangement)
        #Check 2 position jumps PXB
        while unsolved:
            unsolved = False
            while(arrangement[left:left+3]==['B','B','B']):
                left+=1
            while(arrangement[right-3:right]==['P','P','P']):
                right-=1
            for i,_ in enumerate(arrangement[left:right-2]):
                index = i + left
                if (arrangement[index],arrangement[index+2]) == ('P','B'):
                    arrangement[index],arrangement[index+2] = ('B','P')
                    swap_counter+=1
                    unsolved = True
                    #print(index)
        unsolved = False
        #Check for 1 position jumps PBP or BPB
        for i,_ in enumerate(arrangement[left:right-2]):
                index = i + left
            #if sortable
                if (arrangement[index],arrangement[index+1],arrangement[index+2])==('P','B','P') or (arrangement[index],arrangement[index+1],arrangement[index+2])==('B','P','B'): 
                    if(arrangement[index+1]=='P'):
                        arrangement[index+1],arrangement[index+2] =('B','P')
                    else:
                        arrangement[index],arrangement[index+1] = ('B','P')
                    swap_counter+=1
                    unsolved = True
                    #print(index)
                    break
    print(swap_counter)
    return
 
 
tests = int(input())
for i in range(0,tests):
    test()