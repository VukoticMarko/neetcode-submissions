class MyHashMap:

    def __init__(self):

        self.hm = []
        

    def put(self, key: int, value: int) -> None:
        for item in self.hm:
            if item[0] == key:
                item[1] = value
                return
        self.hm.append([key, value])

    def get(self, key: int) -> int:

        for i in range(len(self.hm)):

            if key == self.hm[i][0]:
                return self.hm[i][1]

        return -1
        

    def remove(self, key: int) -> None:

        for i in range(len(self.hm)):

            if key == self.hm[i][0]:
                self.hm.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)