'''
def diguiprint(n):
    if n==0:
        return
    print(n)
    diguiprint(n-1)


diguiprint(5)




def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result  = factorial(5)
print(result)



def fib(n):
    if n == 0:
        return 0
    if n ==1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

print(fib(20))
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 选第一个元素做基准
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [6, 3, 8, 2, 7, 5]
sorted_arr = quick_sort(arr)
print(sorted_arr)