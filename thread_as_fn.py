import threading
import time
import datetime
import logging

time_in = datetime.datetime.now()
print("INN >>>>>> agent_MAIN")


def fn_agent_first(param):
    local_in = datetime.datetime.now()
    print("INN >>>>>> " + param)
    time.sleep(5)
    print(
        "END >>>>>> "
        + param
        + " : "
        + str(datetime.datetime.now().second - local_in.second)
    )


def fn_agent_second(param):
    local_in = datetime.datetime.now()
    print("INN >>>>>> " + param)
    time.sleep(2)
    print(
        "END >>>>>> "
        + param
        + " : "
        + str(datetime.datetime.now().second - local_in.second)
    )


t1 = threading.Thread(name="thread1", target=fn_agent_first, args=("agent_first",))
t2 = threading.Thread(name="thread2", target=fn_agent_second, args=("agent_second",))

t1.start()
t2.start()

t1.join()
t2.join()

# fn_agent_first("agent_first")
# fn_agent_second("agent_second")

print(
    "END >>>>>> agent_MAIN "
    + " : "
    + str(datetime.datetime.now().second - time_in.second)
)
