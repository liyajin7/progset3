# from maxHeap import maxheap
import sys, gc, random


class maxheap:

    # create heap of max capacity cap
    def __init__ (self, cap):
        self.cap = cap
        self.size = 0
        self.heap = [0] * self.cap
        
    # gets parent of node in h at position p
    def parent (h, p):
        if p != 0:
            return ((p-1) // 2)
        else: return -1

    # gets left child of node in h at position p
    def leftchild (h, p):
        if (2 * p + 1 <= h.size-1):
            return 2 * p + 1
        else: return -1

    # gets right child of node in h at position p
    def rightchild (h, p):
        if (2 * p + 2 <= h.size-1):
            return 2 * p + 2
        else: return -1

    # checks if the position p node has a parent or not
    def hasParent(h, p):
        return h.parent(p) < len(h.heap)

    # swap two values in heap
    def swap (h, p1, p2):
        (h.heap[p1], h.heap[p2]) = (h.heap[p2], h.heap[p1])

    # turn heap rooted at position p into max heap; each child of p also its own max heap
    def maxheapify (h, p):        
        print("\n\n———running MAXHEAPIFY———")
        # print("h.cap: ", h.cap)
        # while(h.hasParent(p) and h.heap[p] > h.heap[h.parent(p)]): # Loops until it reaches a leaf node
        #     h.heap[p], h.heap[h.parent(p)] = h.heap[h.parent(p)], h.heap[p] # Swap the values
        #     p = h.parent(p)

        # print("h.size: ", h.size)
        # print("CURRENT HEAP: ")
        # h.heapprint()


        lchild = h.leftchild(p)
        print("p: ", p)
        print("left child: ", lchild)
        rchild = h.rightchild(p)
        print("right child: ", rchild)

        # print("\n\n")
        
        # finds biggest of node p, its left child, and its right child
        
        biggest = p
        # print("@ p: ", h.heap[biggest])
        # print("@ left child: ", h.heap[lchild])
        rchild = h.rightchild(p)
        # print("@ right child: ", h.heap[rchild])

        if (lchild != -1) & (h.heap[lchild] > h.heap[biggest]):
            biggest = lchild
        if (rchild != -1) & (h.heap[rchild] > h.heap[biggest]):
            biggest = rchild

        # print("biggest: ", biggest)

        # if node p isn't biggest, swap p with biggest
        if biggest != p:
            h.swap(p, biggest)
            h.maxheapify(biggest)


    # insert element into heap
    def insert (h, el):
        if h.size >= h.cap:
            return

        # print("——RUNNING INSERT!!——")
        # print("el: ", el)
        # h.heap.append(el)
        
        h.size += 1
        print("INSERT——— h.size: ", h.size)
        print("INSERT——— curr heap:")
        h.heapprint()
        h.heap[h.size-1] = el
        # print("NOW newly inserted")
        # h.heapprint()

        curr = h.size - 1

        while (curr != 0) & (h.heap[curr] > h.heap[h.parent(curr)]):
            h.swap(curr, h.parent(curr))
            curr = h.parent(curr)

    # returns current max node and reheapifies heap
    def pop (h):
        print("——RUNNING POP——")
        
        h.heapprint()

        max = h.heap[0]
        h.heap[0] = h.heap[h.size-1]
        # del h.heap[h.size-1]
        
        # print("max: ", max)
        # print("new h.heap[0]: ", h.heap[0])
        # print("NEW FUCKIN THING: ")
        h.size -= 1
        # h.heapprint()

        # assign last node to root, then reheapify
        

        # print("new size????", h.size)


        # print("after head's gone: ")
        # h.heapprint()
        
        
        
        h.maxheapify(0)
        # print("post pop heapify: ")
        # h.heapprint()

        return max

    # prints the heap in readable format
    def heapprint (h):
        for j in range(h.size):
            print(h.heap[j])
        print("\n")
    

class Solution:
    def __init__ (self):
        ()


# runs the karmarker karp algorithm
def kk(input):
    # create max heap from given input
    h = maxheap(len(input))
    for i in range(len(input)):
        print("input[i]:", input[i])
        h.insert(input[i])
    
    
    print("origheap heap: ")
    h.heapprint()

    # run kk algorithm
    while (h.size > 1):
        print("------\nnew KK run")
        print("prepop heap: ")
        h.heapprint()
        x = h.pop()
        y = h.pop()
        z = [x-y]
        print("x,y,z: ", x, "-", y,"=",z)
        
        print("preinsert heap: ")
        h.heapprint()
        
        # print("x-y: ", x-y)
        h.insert(z[0])
        
        print("current heap size: ", h.size)

        print("postpop, postinsert heap: ")
        h.heapprint()

    
    
    # calculate final element, deallocate memory used by heap
    residue = h.pop()
    del h
    gc.collect()

    return residue


def main():
    # initialize and define variables
    me, flag, alg, fname = sys.argv
    alg = int(alg)
    flag = int(flag)

    # store input file into single array
    f = open(fname, "r")
    input = []
    for line in f:
        input.append(int(line))

    # run respective algorithm to calculate residue
    residue = 0
    if (flag == 0):
        residue = kk(input)
    
    print("------------\nRESIDUE: ", residue)

if __name__ == "__main__":
    main()