"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
from collections import deque


class PriorityQueue:
    def __init__(self):
        # todo для очереди можно использовать python dict
        self.my_priority_queue = deque()


    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing

        """
        # single_queue = [
        #     {
        #         "priority": "high",
        #         "elem": "value"
        #     },
        #     {
        #         "priority": "medium",
        #         "elem": "value"
        #     },
        #     {
        #         "priority": "low",
        #         "elem": "value"
        #     },
        # ]

        a = [value for value in range(elem)]
        for value in a:
            self.my_priority_queue.insert(value, priority)

        b = []
        for pr in a:
            b.append(self.my_priority_queue.popleft())

        self.my_priority_queue.insert(0, elem)
        return None



    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if not self.my_priority_queue:
            return None
        return self.my_priority_queue.pop()  # O(1)

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """

        if ind <= len(self.my_priority_queue):
            peek_val = self.my_priority_queue[-1 - ind]
            return peek_val
        else:
            return None

    def clear(self) -> None:
        """
        Clear my queue
        :return: None
        """
        self.my_priority_queue.clear()

        return None

