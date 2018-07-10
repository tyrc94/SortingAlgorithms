class Sorting:
    def __init__(self, array):
        self.array = array
    
    def bubble_sort(self):
        while True:
            swapped = False
            for i in range(len(self.array)-1):
                if self.array[i] > self.array[i+1]:
                    tmp = self.array[i]
                    self.array[i] = self.array[i+1]
                    self.array[i+1] = tmp
                    swapped = True
            if swapped == False:
                break
    
    def insertion_sort(self):
        i = 1
        while i < len(self.array):
            j = i
            while j > 0 and self.array[j-1] > self.array[j]:
                tmp = self.array[j-1]
                self.array[j-1] = self.array[j]
                self.array[j] = tmp
                j -= 1
            i += 1
        
    def quick_sort(self, lo, hi):
        if lo < hi:
            p = self.partition(lo, hi)
            self.quick_sort(lo, p-1)
            self.quick_sort(p+1, hi)

    def partition(self, lo, hi):
        pivot = self.array[hi]
        i = lo - 1
        for j in range(lo, hi):
            if self.array[j] < pivot:
                i += 1
                tmp = self.array[i]
                self.array[i] = self.array[j]
                self.array[j] = tmp
            
        tmp = self.array[i + 1]
        self.array[i + 1] = self.array[hi]
        self.array[hi] = tmp

        return i+1

x = Sorting([3,8,12,1,16,1022,106,0,12,16,5,250])
res = x.quick_sort(0,len(x.array)-1)
print(x.array)