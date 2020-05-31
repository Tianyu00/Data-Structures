# python3

from collections import namedtuple

Response = namedtuple("Response", ["was_dropped", "started_at"])
Request = namedtuple("Request", ["arrived_at", "time_to_process"])

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
    def process(self, request):
        while len(self.finish_time) > 0 and self.finish_time[0] <= request.arrived_at:
            self.finish_time.pop(0)
        if len(self.finish_time) == 0:
            self.finish_time.append(request.arrived_at + request.time_to_process)
            return Response(False, request.arrived_at)
        else:
            if len(self.finish_time) == self.size:
                return Response(True, -1)
            else:
                self.finish_time.append(self.finish_time[-1] + request.time_to_process)
                return Response(False, self.finish_time[-2])


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for i in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    if n_requests == 0:
        return 

    buffer = Buffer(buffer_size)
    responses=[]
    for request in requests:
        responses.append(buffer.process(request))

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
