class MyClass:
    __pq = 30

    @property
    def pq(self):
        return self.__pq

    @pq.setter
    def pq(self, pq):
        self._pq = pq
        return self.__pq

m = MyClass
m.pq = 10
print (m.pq)
