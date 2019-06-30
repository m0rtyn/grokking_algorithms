def sum_of_array(arr):
  result = arr[0]
  if len(arr) == 1:
    return result
  else:
    result += sum_of_array(arr[1:-1])
    return result

array = [1,2,3]

print(sum_of_array(array))

# print(array[0:-2])