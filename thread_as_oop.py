import threading
import time
import datetime
import logging

time_in = datetime.datetime.now()
print("INN >>>>>> agent_MAIN")

class thread_1(threading.Thread):
    def __init__(self, name_thread, id ,data):
        self.name_thread = name_thread
        self.id = id
        self.data = data
        threading.Thread.__init__(self, name=self.name_thread, target=thread_1.run)
    
    def run(self):
        self.method_1(self.id)

    def method_1(self, id):
        local_in = datetime.datetime.now()
        print("INN >>>>>> agent_1")
        time.sleep(5)
        print("END >>>>>> agent_1 " + str(datetime.datetime.now().second - local_in.second))
        return None

class thread_2(threading.Thread):
    def __init__(self, name_thread, id ,data):
        self.name_thread = name_thread
        self.id = id
        self.data = data
        threading.Thread.__init__(self, name=self.name_thread, target=thread_1.run)
    
    def run(self):
        self.method_2(self.id)

    def method_2(self, id):
        local_in = datetime.datetime.now()
        print("INN >>>>>> agent_2")
        time.sleep(2)
        print("END >>>>>> agent_2 " + str(datetime.datetime.now().second - local_in.second))
        return None

t1 = thread_1("first thread", 12, "data")
t2 = thread_2("second thread", 34, "data")

t1.start()
t2.start()

t1.join()
t2.join()

print("END >>>>>> agent_MAIN " + " : " + str(datetime.datetime.now().second - time_in.second))

