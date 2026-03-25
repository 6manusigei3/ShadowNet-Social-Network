import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))

    def pop(self):
        if self.heap:
            priority, item = heapq.heappop(self.heap)
            return item, -priority

    def is_empty(self):
        return len(self.heap) == 0
