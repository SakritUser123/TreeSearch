
 
BranchA = [0,1,2,3,4,5,6,7,8,9]
BranchB = [10,11,12,13,14,15,16,17,18,19,20]
LeafC = [0,1,2,3,4]
LeafD = [5,6,7,8,9,10]
LeafE = [10,11,12,13,14,15]
LeafF = [15,16,17,18,19,20]


def traverse():
    num = int(input('Search For a Number: '))
    if num > 20:
        print('Not Found In Tree...')
    if num < 0:
         print('Not Found In Tree...')
    else:
        print('Found in Tree')
    if num in BranchA:
        print('In BranchA...')
        
        if num in LeafC:
            print('In Left Leaf ...')
            
        elif num in LeafD:
            print('In Right Leaf...')
    elif num in BranchB:
        print('In Right Branch...')
        if num in LeafE:
            print('In Left Leaf')
        elif num in LeafF:
            print('In RIght Leaf')
            
traverse()
