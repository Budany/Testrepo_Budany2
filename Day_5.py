列表推导(list comprehension)，new_list = [expression for item in iterable]
返回一个list，和map(function, iterable)的功能差不多

生成器表达式(generator expression), generator = (expression for item in iterable)
大量数据的时候，用于节省内存，或是用于生成处理无限序列

对于dictionary，dic.get(k,0)
该方法是用来获得dic中 key k的值，如果不存在则返回0
