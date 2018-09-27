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
>> (中间过了个中秋假，而且发版忙就停了几天，继续打卡)
11. Sep 27 p415-443
