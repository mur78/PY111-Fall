"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        # todo для очереди можно использовать python list
        self.my_queue = []

        # начало очереди - слева  - deque
        # конец очереди - справа - enque

        # append, pop(-1) -> O(1)
        # insert, del, pop(0) - > O(n)

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        #self.queue.append(elem)
        self.my_queue.insert(0, elem)
        return None


    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if not self.my_queue:
            return None
        return self.my_queue.pop()  # O(1)

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """

        if ind <= len(self.my_queue):
            peek_val = self.my_queue[-1 - ind]
            return peek_val
        else:
            return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.my_queue.clear()

        return None
