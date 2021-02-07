

# Given a sorted array of positive integers, rearrange the array alternately 
# i.e first element should be the maximum value, second minimum value, 
# third-second max, fourth-second min and so on.

# Examples:

# Input: arr[] = {1, 2, 3, 4, 5, 6, 7}
# Output: arr[] = {7, 1, 6, 2, 5, 3, 4}

# Input: arr[] = {1, 2, 3, 4, 5, 6}
# Output: arr[] = {6, 1, 5, 2, 4, 3}


# def MeanderingArray(array):
#     array.sort()
#     res = []
#     l, r = 0, len(array) - 1
#     while len(res) < len(array):
#         res.append(array[r])
#         r -= 1
#         if len(res) == len(array):
#             break
#         res.append(array[l])
#         l += 1
#     return res

def MeanderingArray(arr, n): 
  
    # initialize index of first minimum  
    # and first maximum element  
    max_ele = arr[n - 1] 
    min_ele = arr[0] 
  
    # traverse array elements  
    for i in range(n): 
          
        # at even index : we have to  
        # put maximum element 
        if i % 2 == 0: 
            arr[i] = max_ele 
            max_ele -= 1
  
        # at odd index : we have to 
        # put minimum element 
        else: 
            arr[i] = min_ele 
            min_ele += 1