# Topic Thread

## Application Development Strategies

- Synchronous: A synchronous process is one that runs sequentially, waiting for each operation to finish before starting the next. That is, if you had two tasks in your program, “process 1” and “process 2.” Process 2 would wait for process 1 to finish, and then start immediately.

- Concurrency: Concurrency refers to the ability of a system to execute multiple tasks that overlap in time. That is, they concur in time (hence the name). By definition, two tasks are concurrent if one of them starts between the start and finish of the other.

- Asynchronous: Normally, we tend to call a process “asynchronous” when we have a process that involves a very long wait or blocking. For example, waiting for a user to press a key, for a file to be read, or for a communication to be received. In order for these processes not to block the main program flow, they are launched with a concurrency mechanism so that they are not blocking. Then it is usually said that they have been launched asynchronously.

- Sequential: Sequential structure or sequential programming is understood as a methodology that bases its operation on having actions or instructions that follow others in a sequential manner. In this mechanism, multiple operations can be presented from start to finish, as well as assignment or calculation operations, among other

- Parallel: Now we come to parallelism and semi-parallelism. Here we are talking about a specific way of achieving concurrency, by executing multiple processes simultaneously. The first thing to remember is that, in general, a single-core processor can only execute a single process simultaneously. That is how they are built and that is how they work. In the case that our processor has multiple cores, we can achieve parallelism. This means that each core can be responsible for executing one of the processes. 
    
    - Process: It refers to the simultaneous execution of several computational processes. This means that several physical means of execution are required: several processors (or a processor with several cores) or several computers (distributed systems) and enough memory to maintain them.
    
    - Thread: Thread parallelism is a hardware mechanism that enables parallel computing by assigning independent flow of control to threads.


## Types

- **Functional:**

    ```py
    import threading
    t1 = threading.Thread(name="thread1", target=fn_agent_first, args=("agent_first",))
    ```

- **OOP:**



## Run & Configure
-  python thread_as_fn.py

## References 
- [Python 3 Tutorial - 15 Hilos](https://www.youtube.com/watch?v=3Rlh6uUuQqA&list=PLvimn1Ins-43WtzBU5281m6UwbNROArTB&index=15)
- [threading: Paralelismo basado en hilos](https://docs.python.org/es/3.8/library/threading.html)
- [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)
- [Asincronía, concurrencia y paralelismo](https://www.luisllamas.es/asincronia-concurrencia-paralelismo/)
- [¿Qué es la estructura secuencial en programación?](https://keepcoding.io/blog/que-es-estructura-secuencial-programacion/)

## Related Projects 
