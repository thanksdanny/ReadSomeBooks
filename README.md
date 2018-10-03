# Python 学习手册
1. Sep 12  p87-p157
2. Sep 13  p157-p166
3. Sep 14  p166-p209:学会了如何重新使用字符串的格式化，get到了怎么用format格式化
4. Sep 15  p210-p238 : 列表与字典的基本使用
5. Sep 16  p239-271
	* 生命一个元祖时候，结束为止需要价个逗号：y=(40,)
	* 文件的简单实用操作（每行读取文件的方法，回头马克一个p247）
	* 这部分需要重新回顾
	* 引用与拷贝
6. Sep 17  p272-p291 
7. Sep 18  P292-p321
8. Sep 19  p322-p359 
	* zip() 与 map()的配合for寻欢的使用
	* zip()构造字典
		* D2={}
		* for (k, v) in zip(keys, vals):D2[k] = v
	* 第二种办法构造字典
		* keys = ['a', 'b', 'c']
		* vals = [1, 3, 5]
		* D3 = dict(zip(keys, vals))
	* enumerate内置函数用法
9. Sep 20  p360-403
	* lines =[line.rstrip() for line in lines]
	* lines = [line.rstrip() for line in open('scriptl.py') if line[o] == 'p']
		* res =[]
		* for line in open('scriptl.py'):
		* 	if line[o] == 'p':
		*		res.append(line.rstrip())
10. Sep 21 p404-414
> (中间过了个中秋假，而且发版忙就停了几天，继续打卡)
11. Sep 27 p415-443
	* 作用域这块有点深，不是很好理解，尤其是方法嵌套；
	* global/nonlocal 这两个还待理解
12. Sep 28 p444-471 （18章 参数）
	* 参数顺序法则
		* 在函数调用中，参数必须以此顺序出现：任何参数位置（value），后面跟着任何关键字参数（name=value）和*sequence形式的组合，后面跟着**dict形式。
		* 在函数头部，参数必须以此顺序出现：任何一般参数（name），紧跟着任何默认参数（name=value），如果有的话，后面是\*name（或者在Pyhton3.0中是\*）的形式，后面跟着任何 name 或者 name=value keyword-only 参数（在python 3.0中），后面跟着 **name形式。
	* \* 与 \** 的运用 p456
	* 三种 min 操作,计算最小值
		* ``` python
			def min1(*args):
				res = args[0]
				for arg in args[1:]:
					res = arg
				return res

			def min2(first, *rest):
				for arg in rest:
					if arg < first:
						first = arg
				return first

			def min3(*args):
				tmp = list(args)
				tmp.sort()
				return tmp[0]

			print(min1(3,4,1,2))
			print(min2("bb", "aa")) 
		```
	* set函数应用
13. Sep 29 p472-493 （19章 函数的高级话题）
	* 比较高级的进阶，这个大概了解下回头再回顾
	* lambda 的使用
	* map 的使用
	* 函数式编程工具：filter、reduce
14. Sep 30 p494-536（20章 迭代与解析）
	* 嵌套列表的解释，这样的高级嵌套看起来很酷，但理解起来真的有点困难，还不如分多几层写这样比较清晰，但运行复杂时，使用高级方法会使程序速度更快，如下面一点；
	* map调用比等效的 for 快两倍，而列表解析比 map 调用还要再快一些；
15. Oct 01 p537-552 (21章 模块：宏伟蓝图)
	* 模块搜索路径
		1. 程序主目录
		2. PYTHONPATH目录（如果已进行了设置)
		3. 标准链接库目录
		4. 任何.pth文件的内容（如果存在的话）
	* python在平台上配置的模块搜索路径，可以查看 sys.path
16. Oct 02 p553-569	(22章 模块代码编写基础)
	* from 只是把变量名从一个模块复制到另一个模块，并不会对模块名本身进行复制；
	* 简单的模块倾向使用 import，而不是 from；
	* from 语句是用于明确列举出想要的变量；
	* 当必须使用两个不同模块内定义的相同变量名的变量时，才必须使用 import，不能用 from；
	* 导入模块的全局作用域，一定是在其所在的文件，无论在哪个文件调用； p562
	* 模块的重载，reload()
17. Oct 03 p570-591(23章 模块包)
	* 使用包导入都必须有 __init__.py 这个文件
	* 相对引入 p580
