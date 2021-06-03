# from collections import namedtuple

# Request = namedtuple("Request", ["arrived_at", "time_to_process"])
# Response = namedtuple("Response", ["was_dropped", "started_at"])


# class Buffer:
#     def __init__(self, size):
#         self.size = size
#         self.finish_time = []

#     def process(self, request):
#         # write your code here
#         return Response(False, -1)


# def process_requests(requests, buffer):
#     responses = []
#     for request in requests:
#         responses.append(buffer.process(request))
#     return responses


# def main():
#     buffer_size, n_requests = map(int, input().split())
#     requests = []
#     for _ in range(n_requests):
#         arrived_at, time_to_process = map(int, input().split())
#         requests.append(Request(arrived_at, time_to_process))

#     buffer = Buffer(buffer_size)
#     responses = process_requests(requests, buffer)

#     for response in responses:
#         print(response.started_at if not response.was_dropped else -1)


def process_requests(requests, buffer_size):
    queue = []
    start_times = []

    for p in requests:
        # Process all elements in queue that FINISH PROCESSING before this packet arrives
        while queue and queue[0] <= p[0]:
            queue.pop(0)
        # Then add new element to queue (or not)
        if len(queue) < buffer_size:
            start = max(p[0], queue[-1] if queue else 0)
            queue.append(start + p[1]) # storing end time of packet
            start_times.append(start)
        else:
            start_times.append(-1)
            
    return start_times

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append((arrived_at, time_to_process))

    start_times = process_requests(requests, buffer_size)

    for s in start_times:
        print(s)
            

if __name__ == "__main__":
    main()
