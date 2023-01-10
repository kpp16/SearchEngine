class Queue:
    queue_data: list = []

    def __init__(self) -> None:
        self.queue_data = []


    def push(self, link: str) -> None:
        self.queue_data.append(link)


    def pop(self) -> str:
        top: str = self.queue_data[0];
        self.queue_data.pop(0)
        return top


    def size(self) -> int:
        return len(self.queue_data)
    

    def top(self) -> str:
        return self.queue_data[0]


    def is_empty(self) -> bool:
        return self.size() == 0
