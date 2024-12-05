import lamda

nums = [1,2,3,4,5,6]
even = list(filter(lambda n : n%2==0, nums))
doubles = list(map(lambda n : n*n,even))

print(doubles)