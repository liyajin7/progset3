
def main():
    A_input = [10,8,7,6,5]

    P_self = [1,2,3,2,3]
    
    n = len(A_input)

    Aprime_newinput = [0,0,0,0,0]
    
    for i in range(1, n+1):
            for j in range (1, n+1):
                if (P_self[j-1] == i):
                    Aprime_newinput[i-1] += A_input[j-1] 
    
    print(Aprime_newinput)


if __name__ == "__main__":
    main()

