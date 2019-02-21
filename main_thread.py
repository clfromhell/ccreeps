import multiprocessing
from worker_class import Worker

if __name__ == "__main__":
    worker = Worker("test.txt")
    worker.check_for_cmd()

