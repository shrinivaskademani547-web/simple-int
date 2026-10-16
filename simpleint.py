import sys

def simpleInt(pr, intr, time):
    return(pr*intr*time/100)

if __name__=="__main__":
    p = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])

    print("simple Intrest:",simpleInt(p,i,t))
