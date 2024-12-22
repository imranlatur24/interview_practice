import  multiprocessing
def square(n):
    print(f'squre of {n} = ',n*n)
def fibo(n):
    count,n1,n2=0,0,1
    print(f'fibonacci series of {n} is : ')
    while count<=n:
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        count+=1
def cube(n):
    print(f'cube of {n} = ',n*n*n)

if __name__=="__main__":
    p1 = multiprocessing.Process(target=square,args=(5,))
    p2 = multiprocessing.Process(target=fibo,args=(5,))
    p3 = multiprocessing.Process(target=cube,args=(5,))
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()

    ###########
#     squre of 5 =  25
#   fibonacci series of 5 is : 
#   0
#   1
#   1
#   2
#   3
#   5
#   cube of 5 =  125