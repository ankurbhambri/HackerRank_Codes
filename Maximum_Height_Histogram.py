class MHA():

    def __init__(self, arr):
        self.arr = arr

    def nsr(self):
        nsr = []
        for i in range(len(arr)):
            next = len(arr)
            for k in range(i+1, len(arr), 1):
                if arr[i] > arr[k]:
                    next = arr[k]
                    break
            if next == len(arr):
                nsr.append(len(arr))
            else:
                nsr.append(arr.index(next))
        return nsr

    def nsl(self):

        nsl = []
        for i in range(len(arr)):
            prev = -1       
                        #(Start, Stop, Step) 
            for k in range(i-1, -2, -1):
                if arr[i] > arr[k]:
                    prev = arr[k]
                    break
            if prev == -1:
                nsl.append(-1)
            else:
                nsl.append(arr.index(prev))
        return nsl

    def final_compute(self):
        mha = list()
        nsr = self.nsr()
        nsl = self.nsl()
        for i in range(len(arr)):
            mha.append(arr[i]*(nsr[i] - nsl[i] -1))
        return mha

arr = [6,2,5,4,5,1,6]
obj = MHA(arr)
print(obj.final_compute())
