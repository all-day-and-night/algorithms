import heapq


def solution(operations):
    answer = []
    max_heap = []
    min_heap = []

    for operation in operations:
        operation = operation.split()
        if operation[0] == 'I':
            heapq.heappush(max_heap, [-int(operation[1]), int(operation[1])])
            heapq.heappush(min_heap, int(operation[1]))

        else:
            if len(min_heap) == 0:
                continue
            elif operation[1] == '1':
                max_value = heapq.heappop(max_heap)[1]
                min_heap.remove(max_value)

            elif operation[1] == '-1':
                min_value = heapq.heappop(min_heap)
                max_heap.remove([-min_value, min_value])

    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]