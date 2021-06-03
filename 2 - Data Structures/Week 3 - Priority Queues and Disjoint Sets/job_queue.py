import heapq

def process_jobs(n_workers, jobs):
    _queue = []

    for worker in range(n_workers):
        heapq.heappush(_queue, (0, worker))

    while _queue:
        t, worker = heapq.heappop(_queue)

        if jobs:
            print(worker, t)
            new_job_length = jobs.pop(0)
            heapq.heappush(_queue, (t + new_job_length, worker))
        else:
            break


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    process_jobs(n_workers, jobs)


if __name__ == "__main__":
    main()
