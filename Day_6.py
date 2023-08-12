with open() as f:
类似于双击打开文件，()中参数'r'代表该file object被设定为了只读模式，所以不能改变它的文件内容　

.read()
是适用于text file 的方法

with open() as f:    if condition:    def function(): 
这些都是可以创造代码块的结构和语句。在这里，with 是创造了一个指定上下文的代码块，上文是打开一个文件，下文是关闭这个文件

.write()
也是用于text file的方法，

一个txt文件中的内容为string

当一个python script(脚本)被其他python script导入时，它被称之为作为模块(module)使用
库(library)包含一个或者多个script，其本质是一组已经写好的代码，便于重用，
重用指的是导入了一个python script作为module使用的python script可以不需要重新写代码而直接使用module中的function，variable，class
当我们import 一个 module的时候，意味着执行了这个module，也正是因为这样才可以使用这个被执行的module中的function，variable，class

.split()用于分离一个string来生成list的时候，需要注意，必须要有seperator，否则无法完成，如果没有seperator,可以用list comprehension来生成

