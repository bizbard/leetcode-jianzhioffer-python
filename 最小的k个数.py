from typing import List
import random


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def partition(arr, left, right):
            randomIndex = random.randint(left, right)
            arr[left], arr[randomIndex] = arr[randomIndex], arr[left]
            pivot = arr[left]

            i = left
            j = right
            while i < j:
                while i<j and arr[j] >= pivot:
                    j -= 1
                while i<j and arr[i] <= pivot:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]

            arr[left], arr[i] = arr[i], arr[left]
            return i


        def quicksort(arr, i, j):
            if i > j:
                return
            pivotIndex = partition(arr, i, j)
            quicksort(arr, i, pivotIndex-1)
            quicksort(arr, pivotIndex+1, j)

        quicksort(arr, 0, len(arr)-1)
        return arr[:k]


if __name__ == '__main__':
    # ======= Test Case =======
    arr = [3,2,1]
    k = 2
    # ====== Driver Code ======
    sol = Solution()
    res = sol.getLeastNumbers(arr, k)
    print(res)