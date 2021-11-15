def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    ind = -1
    while left <= right:
        mid = (left + right) // 2
        if lst01[mid] == 1 and lst01[mid-1] == 0:
            return mid
        elif lst01[mid] == 0 and lst01[mid+1] == 1:
            return mid+1
        elif lst01[mid+1] == 0:
            left = mid + 1
        elif lst01[mid-1] == 1:
            right = mid - 1


def main():
    print(findChange([0, 0, 0, 0, 0, 1, 1, 1]))
