def fact(x):
  if x == 1:
    return 1
  else:
    result = x * fact(x - 1)
    print(result)
    return result


x = 5
fact(x)
