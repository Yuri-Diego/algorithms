# Implementacao do BubbleSort, algoritmo de ordenacao.
# Melhor caso (Best case): O(n), quando o array ja esta ordenado.
# Pior caso (Worst case): O(n^2).

def bubbleSort(nums):
    size = len(nums)

    for _ in nums:
        is_sorted = True
        print(nums)
        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                is_sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        if is_sorted:
            return
        
# Array sorted
bubbleSort([1,2,3,4,5])

bubbleSort([5,4,3,2,1])