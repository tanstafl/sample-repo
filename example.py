recycle_bin = [1,2, "Fastcampus", [], 5,4, 5.6,"패스트캠퍼스"]
recycle_bin
list(filter(lambda x:isinstance(x,int), recycle_bin))
solve = list(map(lambda a: a**2, (filter(lambda x:isinstance(x,int), recycle_bin))))
print(solve)
