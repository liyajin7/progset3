# from maxHeap import maxheap
import sys, gc, math, random, time
from random import *
from xml.dom.pulldom import END_ELEMENT

MAX_ITER = 25000

def T(iter):
    return (10**10*0.8**(iter/300))

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
        lchild = h.leftchild(p)
        rchild = h.rightchild(p)
        
        biggest = p
        rchild = h.rightchild(p)

        if (lchild != -1) & (h.heap[lchild] > h.heap[biggest]):
            biggest = lchild
        if (rchild != -1) & (h.heap[rchild] > h.heap[biggest]):
            biggest = rchild

        if biggest != p:
            h.swap(p, biggest)
            h.maxheapify(biggest)


    # insert element into heap
    def insert (h, el):
        if h.size >= h.cap:
            return
        
        h.size += 1
        h.heap[h.size-1] = el
     
        curr = h.size - 1

        while (curr != 0) & (h.heap[curr] > h.heap[h.parent(curr)]):
            h.swap(curr, h.parent(curr))
            curr = h.parent(curr)

    # returns current max node and reheapifies heap
    def pop (h):
        
        max = h.heap[0]
        h.heap[0] = h.heap[h.size-1]
        h.size -= 1
        
        h.maxheapify(0)
   
        return max

    # prints the heap in readable format
    def heapprint (h):
        for j in range(h.size):
            print(h.heap[j])
        print("\n")
    

class Solution:
    # initialize a solution set of size n
    def __init__ (self, n):
        self.ls = [0] * n # @LIYA MAKE THIS ANY DIFF?

    # to-be-overriden function for generating random solutions
    def randsol (self, n): ()

    # to-be-overriden function for generating random neighbor of solution sol of size n
    def randneighbor (self, n): ()

    # to-be-overriden function for generating residue
    def residue (self, input, n): ()

    # general HEURISTIC repeated random solution
    def repeatrand (self, input, n):
        for i in range(MAX_ITER):
            rsol = self.randsol(n)
            if rsol.residue(input, n) < self.residue(input, n):
                self = rsol

        return self.residue(input, n)

    # general HEURISTIC repeated hill climbing solution
    def hillclimb (self, input, n):
        for i in range(MAX_ITER):
            rneigh = self.randneighbor(n)
            if rneigh.residue(input, n) < self.residue(input, n):
                self = rneigh

        return self.residue(input, n)
            
    # general HEURISTIC repeated simulated annealing solution
    def simanneal (self, input, n):
        import random
        spprime = self

        for i in range(MAX_ITER):
            sprime = self.randneighbor(n)

            res_sp = sprime.residue(input, n)
            res_self = self.residue(input, n)
            res_spp = spprime.residue(input,n)

            if res_sp < res_self:
                self = sprime
            elif (random.uniform(0, 1) <= math.exp(-(res_sp - res_self) / T(i))):
                self = sprime
            if res_sp < res_spp:
                spprime = self
            
            # del res_sp, res_self, res_spp
            # gc.collect()
                    
        return spprime.residue(input, n)#, res_spp

    # print solutions visibly
    def printsol (self):
        for i in range(len(self.ls)):
            print(self.ls[i])
        print("\n")
    

class Standard (Solution):
    # standard sequence function for generating random solutions
    def randsol (self, n):
        rsol = Standard(n)

        for i in range(n):
            if (randint(0,1) == 1):
                rsol.ls[i] = 1
                # rsol.ls[i] = 1
            else: rsol.ls[i] = -1 # rsol.ls[i] = -1
        
        return rsol
        
    # standard sequence function for generating random neighbor of solution sol of size n
    def randneighbor (self, n):
        import random
        # duplicate neighbor
        nbor = Standard(n)
        nbor.ls = self.ls[:]
        
        random.seed()
        i = randint(0, n-1)
        nbor.ls[i] = -nbor.ls[i]
        
        # change second index with probability 1/2
        if (random.uniform(0, 1) > 0.5):
            j = i

            # ensure j ≠ i
            while (j == i):
                j = randint(0, n-1)
            
            nbor.ls[j] = -nbor.ls[j]

        return nbor;

    # standard sequence function for generating residue
    def residue (self, input, n):
        res = 0
        for i in range(n):
            res += self.ls[i] * input[i]
        
        return abs(res)


class Prepart (Solution):
    
    # prepartitioning function for generating random solutions
    def randsol (self, n):
        import random
        random.seed()

        rsol = Prepart(n)
        for i in range(n):
            rsol.ls[i] = randint(1, n)

        return rsol

    # prepartitioning function for generating random neighbor of solution sol of size n
    def randneighbor (self, n):
        import random
        random.seed()

        nbor = self #Prepart(n)
        #nbor.ls = self.ls[:]

        # generate index j to be changed, ensuring it's different than i
        i = randint(0, n-1)
        j = nbor.ls[i]
        while (j == nbor.ls[i]):
            j = randint(0, n-1)

        nbor.ls[i] = j

        return nbor

    # prepartitioning function for generating residue
    def residue (self, input, n):
        newinput = [0] * n

        for i in range(1, n+1):
            for j in range (1, n+1):
                if (self.ls[j-1] == i):
                    newinput[i-1] += input[j-1] 

        res = kk(newinput)
        del newinput
        gc.collect()

        return abs(res)



# runs the karmarker karp algorithm
def kk(input):
    # create max heap from given input
    h = maxheap(len(input))
    for i in range(len(input)):
        h.insert(input[i])
    
    # run kk algorithm
    while (h.size > 1):
        x, y = h.pop(), h.pop()
        h.insert(x-y)    
    
    # calculate final element, deallocate memory used by heap
    residue = h.pop()
    del h
    gc.collect()

    return residue


def runTest():
    for i in range(10):
        input = [0] * 100
        for i in range(100):
            input[i] = randint(1, 10**12)


        stan = Standard(100).randsol(100)
        prep = Prepart(100).randsol(100)
        
        n = 100
        # print("KK residue: ", kk(input))
        # print("\ninitial residue, standard sequence:", stan.residue(input, n))
        # print("\nRR standard sequence:", stan.repeatrand(input, n))
        # print("\nHC standard sequence:", stan.hillclimb(input, n))
        # print("\nSA standard sequence:", stan.simanneal(input, n))
        # print("\ninitial residue, standard sequence:", prep.residue(input, n))
        # print("\nRR prepartition:", prep.repeatrand(input, n))
        # print("\nHC prepartition:", prep.hillclimb(input, n))
        # print("\nSA prepartition:", prep.simanneal(input, n))

        print(kk(input), "\t", stan.residue(input, n), "\t", stan.repeatrand(input, n), "\t", stan.hillclimb(input, n), "\t", stan.simanneal(input, n), "\t", prep.residue(input, n), "\t", prep.repeatrand(input, n), "\t", prep.hillclimb(input, n), "\t", prep.simanneal(input, n))


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

    n = len(input)

    # run respective algorithm to calculate residue
    stan = Standard(n).randsol(n)
    prep = Prepart(n).randsol(n)
    
    residue = 0
    if (flag == 0): # kk
        residue = kk(input)
    elif (flag == 1): # standard repeated rand
        residue = stan.repeatrand(input, n)
    elif (flag == 2): # standard hillclimb
        residue = stan.hillclimb(input, n)
    elif (flag == 3): # standard simulated anneal
        residue = stan.simanneal(input, n)
    elif (flag == 11): # prepart repeated rand
        residue = prep.repeatrand(input, n)
    elif (flag == 12): # prepart hillclimb
        residue = prep.hillclimb(input, n)
    elif (flag == 13): # prepart simanneal
        residue = prep.simanneal(input, n)
    
    print(residue)

if __name__ == "__main__":
    main()