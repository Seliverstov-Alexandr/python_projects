import multiprocessing
import os
def whoiam(what):
    print("Process %s says: %s" %(os.getpid(), what))
if __name__ == '__main__':
    whoiam("I am a main program")
    for n in range(4):
        p = multiprocessing.Process(target = whoiam, args= ('I am a function %s' % n,))
        p.start()    