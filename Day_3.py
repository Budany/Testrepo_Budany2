\n
换行

\r
回车

所有的东西都是一个object，每一个object都属于一种class

iterable包括tuple、list、dictionary、string、range，基本上包含多个element的东西就是一个iterable
iterator是iterable但反之则不一定，所有的sequence都是iterable，但反之则不然，sequence必须要有一定的顺序

round(x,n)n是保留的小数点的位数

f''
可以将表达式嵌入string以进行格式化

enumerate()
用于返回一个enumerate obejct，一个enumerate obeject中本身就是一个iterable,其包含的elements都是tuple，形如(index, item)

map(function, iterable)
用于返回一个iterable，其中包含的elements即是输入的iterable的各个elements应用了funciton之后的结果

lambda [arg1 [,arg2,.....argn]]:expression
用于创建匿名函数，expression是一个表达式

input()
返回的是一个string，有的时候需要eval()将input()的type转化为int

number:.nf
这里n是需要保留的小数位数

.split()
是应用于string的方法，输入的参数为指定的分隔符，最终会返回一个list



