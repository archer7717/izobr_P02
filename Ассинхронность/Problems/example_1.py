# синхронный код в один поток 
from threading  import Thread
import time

def print1():
    print(1)



def print2():
    time.sleep(10)
    print(2)
    
def new_procces():
    th = Thread(target=print2)
    th.start()

def print3():
    print(3)




def print4():
    print(4)


def print5():
    print(5)


def main():
    print1()
    new_procces()
    print3()




if __name__ =='__main__':
    main()
