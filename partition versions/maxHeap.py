import sys, math

class maxheap:

    # create heap of max capacity cap
    def __init__ (self, cap):
        self.cap = cap 
        self.size = 0
        self.heap = []
        
        # initialize heap as a list of size cap
        # h.heap = [0] * (h.cap)
        # h.heap[0] = sys.maxsize # @LIYA also this wtf

    # gets parent of node in h at position p
    def parent (h, p):
        if p != 0:
            return ((p-1) // 2)
        else: return -1


    # gets left child of node in h at position p
    def leftchild (h, p):
        if (2 * p + 1 <= h.size):
            return 2 * p + 1
        else: return -1


    # gets right child of node in h at position p
    def rightchild (h, p):
        if (2 * p + 2 <= h.size):
            return 2 * p + 2
        else: return -1

    # def isLeaf(h, pos):
    #     if pos >= (h.size//2) and pos <= h.size:
    #         return True
    #     return False

    def hasParent(h, p):
        # This function checks if the given node has a parent or not
        return h.parent(p) < len(h.heap)

    # swap two values in heap
    def swap (h, p1, p2):
        (h.heap[p1], h.heap[p2]) = (h.heap[p2], h.heap[p1])


    # turn heap rooted at position p into max heap; each child of p also its own max heap
    def maxheapify (h, p):        
        print("MAXHEAPIFY RUNNING")

        while(h.hasParent(p) and h.heap[p] > h.heap[h.parent(p)]): # Loops until it reaches a leaf node
            h.heap[p], h.heap[h.parent(p)] = h.heap[h.parent(p)], h.heap[p] # Swap the values
            p = h.parent(p)

        # lchild = h.leftchild(p)
        # print("left child: ", lchild)
        # rchild = h.leftchild(p)
        # print("right child: ", lchild)

        # # print("\n\n")
        
        # # finds biggest of node p, its left child, and its right child
        # biggest = p
        # if (lchild != -1) & (h.heap[lchild] > h.heap[biggest]):
        #     biggest = lchild
        # if (rchild != -1) & (h.heap[rchild] > h.heap[biggest]):
        #     biggest = rchild

        # # if node p isn't biggest, swap p with biggest
        # if biggest != p:
        #     h.swap(h.heap[p], h.heap[biggest])
        #     h.maxheapify(biggest)


              
        # if not h.isLeaf(pos):
        #     if (h.heap[pos] < h.heap[h.leftchild(pos)] or
        #         h.heap[pos] < h.heap[h.rightchild(pos)]):
  
        #         # Swap with the left child and heapify
        #         # the left child
        #         if (h.heap[h.leftchild(pos)] > 
        #             h.heap[h.rightchild(pos)]):
        #             h.swap(pos, h.leftchild(pos))
        #             h.maxheapify(h.leftchild(pos))
  
        #         # Swap with the right child and heapify
        #         # the right child
        #         else:
        #             h.swap(pos, h.rightchild(pos))
        #             h.maxheapify(h.rightchild(pos))
        
        
        # print("h.size ", h.size)


    # insert element into heap
    def insert (h, el):
        if h.size >= h.cap:
            return
            
        # h.heap.append(el)
        # h.size += 1
        # h.heapprint()
        # h.maxheapify(h.size - 1)

        # print("el: ", el)
        # print("current heap: ")
        # h.heapprint()

        # print("size preinsert: ", h.size)
        # print("cap: ", h.cap)

        h.size += 1
        h.heap.append(el)

        # print("size postinsert: ", h.size)

        
        # print("inserted item: ", h.heap[h.size])

        curr = h.size - 1
        #h.parent(curr) = h.parent(curr)

        # print("\npreswap: ")
        # h.heapprint()
        # @LIYA MAKE SURE NO ISSUES W ASSIGNMENT HERE
        while (curr != 0) & (h.heap[curr] > h.heap[h.parent(curr)]):
            # print("\nIS SWAP RUNNING?")
            
            # print("curr: ", curr)
            # print("      h.heap[curr]: ", h.heap[curr])
            # print("parent(curr): ", h.parent(curr))
            # print("      h.heap[h.parent(curr)]: ", h.heap[h.parent(curr)])

            h.swap(curr, h.parent(curr))
            curr = h.parent(curr)

        # print("postswap: ")
        # h.heapprint()

        # print("\n\n----------")


    # returns current max node and reheapifies heap
    def pop (h):
        max = h.heap[0]

        # assign last node to root, then reheapify
        h.heap[0] = h.heap[h.size-1]
        h.size -= 1
        h.maxheapify(0)

        return max

    # prints the heap in readable format
    def heapprint (h):
        for j in range(h.size):
            print(h.heap[j])
        print("\n")
    


def main():
    # initialize and define variables
    me, fname = sys.argv
    
    # store input file into single array
    f = open(fname, "r")
    input = []
    for line in f:
        input.append(int(line))

    h = maxheap(len(input))
    for i in range(len(input)):
        h.insert(input[i])

    print(h.pop())

if __name__ == "__main__":
    main()