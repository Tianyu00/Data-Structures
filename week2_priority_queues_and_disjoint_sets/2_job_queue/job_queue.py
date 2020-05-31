# python3

from collections import namedtuple
import numpy as np

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Operator():
    def __init__(self, n_workers, jobs):
        self.n_workers = n_workers
        self.jobs = jobs
        self.finish_time = np.zeros(n_workers)
        self.log = []
    def do_jobs(self):
        for job in self.jobs:
            i = np.argmin(self.finish_time)
            self.log.append(AssignedJob(i, int(self.finish_time[i])))
            self.finish_time[i] += job
        return self.log

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    operator = Operator(n_workers, jobs)
    assigned_jobs = operator.do_jobs()

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
