from random import *
import sys, random, gc, math

# random.seed()
MAX_ITER = 100

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


def ismaxheap(input):
    n = len(input)
    for i in range(n):
        m = i * 2
        num = input[i]
        if m + 1 < n:
            if num < input[m + 1]:
                return False
        if m + 2 < n:
            if num < input[m + 2]:
                return False
    return True

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

    # general HEURISTIC solution function
    def repeatrand (self, input, n):
        # rsol = self.randsol(n)

        # print("repeatrand neighbor: ")
        # rsol.printsol()

        for i in range(MAX_ITER):
            rsol = self.randsol(n)
            if rsol.residue(input, n) < self.residue(input, n):
                print("UPGRADED")
                self = rsol

        return self

    # general HEURISTIC solution function @LIYA COULD OPTIMIZE FOR STANDARD SOLUTION
    def hillclimb (self, input, n):
        for i in range(MAX_ITER):
            rneigh = self.randneighbor(n)
            print("rsneigh res: ", rneigh.residue(input, n))
            print("curr res: ", self.residue(input, n))
            if rneigh.residue(input, n) < self.residue(input, n):
                print("UPGRADED res from ", self.residue(input, n), "to ", rneigh.residue(input, n))
                self = rneigh

        return self
            

    def simanneal (self, input, n):
        spprime = self

        for i in range(MAX_ITER):
            sprime = self.randneighbor(n)

            res_sp = sprime.residue(input, n)
            res_self = self.residue(input, n)

            if res_sp < res_self:
                self = sprime
            elif (random.uniform(0, 1) <= math.exp(-(res_sp - res_self) / T(i))):
                self = sprime
            if res_sp < spprime.residue(input,n):
                spprime = self
                    
        return spprime


    # print solutions visibly
    def printsol (self):
        for i in range(len(self.ls)):
            print(self.ls[i])
        print("\n")
    

class Standard (Solution):
    # def __init__ (self):
    #     ()

    # standard sequence function for generating random solutions
    def randsol (self, n):
        rsol = Standard(n)

        for i in range(n):
            if (randint(0,1) == 1):
                rsol.ls[i] = 1
                # rsol.ls[i] = 1
            else: rsol.ls[i] = -1 # rsol.ls[i] = -1
        
        return rsol
        # for i in range(n):
        #     if (randint(0,1) == 1):
        #         self.ls[i] = 1
        #         # rsol.ls[i] = 1
        #     else: self.ls[i] = -1 # rsol.ls[i] = -1
        
        # return self

    # standard sequence function for generating random neighbor of solution sol of size n
    def randneighbor (self, n):
        # duplicate neighbor
        nbor = Standard(n)
        nbor.ls = self.ls[:]
        # for i in range(n):
        #     nbor.ls[i] = sol[i]

        # change first index
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
        random.seed()

        rsol = Prepart(n)
        for i in range(n):
            rsol.ls[i] = randint(1, n)

        return rsol

    # prepartitioning function for generating random neighbor of solution sol of size n
    def randneighbor (self, n):
        random.seed()

        nbor = Prepart(n)
        nbor.ls = self.ls[:]

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

        # print("A': ", newinput)

        res = kk(newinput)
        del newinput
        gc.collect()

        return abs(res)






def main():
    me, fname = sys.argv

    f = open(fname, "r")
    input = []
    
    for line in f:
        input.append(int(line))

    # print(ismaxheap(input))

    # rrStan = Standard(n).repeatrand(input, n)

    n = len(input)
    print("\ninput! ", input)


    rsol = Prepart(n).randsol(n)
    rsol.printsol()
    rr_sol = rsol.simanneal(input, n)
    print("hc solution: ")
    rr_sol.printsol()

    print("hc residue: ", rr_sol.residue(input, n))
    
    
    # res = rsol.residue(input, n)
    # rsol.printsol()
    # print("res: ", res)
    
    # rsol = Prepart(n).randsol(n)
    # print("\nrandom solution: ")
    # rsol.printsol()
    # res = rsol.residue(input, n)
    # print("\nres w random solution: ", res)

    # rneigh = rsol.randneighbor(n)
    # print("\nrneighbor: ")
    # rneigh.printsol()
    # resneigh = rneigh.residue(input, n)
    # [print("\nrneighbor residue: ", resneigh)]

if __name__ == "__main__":
    main()
