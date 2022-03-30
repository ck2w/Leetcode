
# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/

# 1. merge + sort, time: O((m+n)log(m+n))
def kth1(arr1, arr2, m, n, k):     
    return sorted(arr1+arr2)[k-1]


# 2. merge, time: O(k), space: O(1)
def kth2(arr1, arr2, m, n, k): 
    count = 0
    curr = 0
    while count < k:
        if arr1[0] > arr2[0]:
            curr = arr2.pop(0)
        else:
            curr = arr1.pop(0)
        count = count + 1
    return curr


# 3. divide and conquer, time: O(logn+logm)
def kth3(arr1, arr2, m, n, k):
    # if k > len(lst1) + len(lst2) or k < 1:
    #     return None
    
    # if (k == 1):
    #     if(arr1[st1] < arr2[st2]):
    #         return arr1[st1]
    #     else:
    #         return arr2[st2]


    if n == 1 or m == 1:
        if m == 1:
            arr2, arr1 = arr1, arr2
            m = n
        if k == 1:
            return min(arr1[0], arr2[0])
        elif k == m + 1:
            return max(arr1[0], arr2[0])
        else:
            if arr2[k - 1] < arr1[0]:
                return arr2[k - 1]
            else:
                return max(arr1[0], arr2[k - 2])

    mid1 = (n-1) // 2
    mid2 = (m-1) // 2
    # print(mid1, mid2)
    # print(arr1, arr2)
    if mid1 + mid2 + 1 < k:
        if arr1[mid1] < arr2[mid2]:
            # k is not in array1[:mid+1]
            return kth3(arr1[mid1 + 1:], arr2, n - mid1 - 1, m, k - mid1 - 1)
        else:
            # k is not in array2[:mid+1]
            return kth3(arr1, arr2[mid2 + 1:], n, m - mid2 - 1, k - mid2 - 1)
    else:
        if arr1[mid1] < arr2[mid2]:
            # k is not in arr2[mid2+1:]
            return kth3(arr1, arr2[:mid2 + 1], n, mid2 + 1, k)
        else:
            # k is not in arr1[mid1+1:]
            return kth3(arr1[:mid1 + 1], arr2, mid1 + 1, m, k)


# 4. divide and conquer, time: O(logk)
def kth4(arr1, arr2, m, n, k, st1 = 0, st2 = 0):    
    # In case we have reached end of array 1
    if (st1 == m):
        return arr2[st2 + k - 1]
 
    # In case we have reached end of array 2
    if (st2 == n):
        return arr1[st1 + k - 1]
 
    # k should never reach 0 or exceed sizes
    # of arrays
    if (k == 0 or k > (m - st1) + (n - st2)):
        return -1
         
    # Compare first elements of arrays and return
    if (k == 1):
        if(arr1[st1] < arr2[st2]):
            return arr1[st1]
        else:
            return arr2[st2]
 
    curr = int(k / 2)
 
    # Size of array 1 is less than k / 2
    if(curr - 1 >= m - st1):
 
        # Last element of array 1 is not kth
        # We can directly return the (k - m)th
        # element in array 2
        if (arr1[m - 1] < arr2[st2 + curr - 1]):
            return arr2[st2 + (k - (m - st1) - 1)]
        else:
            return kth4(arr1, arr2, m, n,
                       k - curr, st1, st2 + curr)
 
    # Size of array 2 is less than k / 2
    if (curr - 1 >= n - st2):
        if (arr2[n - 1] < arr1[st1 + curr - 1]):
            return arr1[st1 + (k - (n - st2) - 1)]
        else:
            return kth4(arr1, arr2, m, n,
                       k - curr,st1 + curr, st2)
    else:
         
        # Normal comparison, move starting index
        # of one array k / 2 to the right
        if (arr1[curr + st1 - 1] < arr2[curr + st2 - 1]):
            return kth4(arr1, arr2, m, n, k - curr,
                       st1 + curr, st2)
        else:
            return kth4(arr1, arr2, m, n, k - curr,
                       st1, st2 + curr)
  
    
# Driver code
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
print(kth1(arr1, arr2, 5, 4, k))

arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
print(kth2(arr1, arr2, 5, 4, k))

arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
print(kth3(arr1, arr2, 5, 4, k))

arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
print(kth4(arr1, arr2, 5, 4, k))
 