class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()

        n = len(self.data)
        mid = n // 2

        if n % 2 == 1:
            return float(self.data[mid])
        else:
            return (self.data[mid - 1] + self.data[mid]) / 2
                







        
        