# Используйте модуль multiprocessing, чтобы создать три отдельных процесса. Заставьте каждый из 
# них подождать случайное количество секунд между нулем и единицей, 
# вывести текущее время, а затем завершить работу.

#print('exersice_1\n')
import time 
import multiprocessing
import psutil
import random
#now = time.time()
#now = time.localtime()
#print(psutil.cpu_percent(True))

def time_now ():
    time.sleep(random.uniform(0,10))
    print(time.localtime())
if __name__ == "__main__":
    for n in range(3):
        p = multiprocessing.Process(target=time_now)
        p.start()
    p.join()
    print(psutil.cpu_times_percent(True))     
   