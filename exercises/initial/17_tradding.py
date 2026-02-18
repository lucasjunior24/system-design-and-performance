import threading


def tarefa():
    for _ in range(10_000_000):
        print(_)


t1 = threading.Thread(target=tarefa)
t2 = threading.Thread(target=tarefa)

t1.start()
t2.start()

t1.join()
t2.join()
