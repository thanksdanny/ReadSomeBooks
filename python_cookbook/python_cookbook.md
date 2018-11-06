# python cookbook
1. day 01 p01-p39 (第一章 数据结构和算法)
    * p10 的程序 yeild还需要再理解一下
    * 查找最大或最小的 N 个元素(使用heapq模块的两个函数nlargest()和nsmallest()) p12

2. day 02 p40-p50(第二章 字符串和文本)
    * re.split()比str.split()能更灵活切割
    ```python
    # demo
    line = 'asdf fjsk; adef, fjek,askd, foo'
    import re
    re.split(r'[;,\s]\s*', line)
    ```
    * 匹配字面字符串，str.endwith() str.startwith() str.find()
    * 字符串搜索替换
    * 讲了挺多正则的东西，可以多看看 
3. day 03 p50-70(第二章 字符串和文本)
    * unicode本土化
    * 删除不需要的字符
4. day 04 p71-100(第三章:数字日期和时间)
    * 数字四舍五入，round(value, ndigits)
    * 数字格式化输出
    * 大型数组运算可以使用NumPy
    * 某一天最后出现的日期，比如星期五
``` python
#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
Topic:最后的周五
Desc:
"""
from datetime import datetime, timedelta
weeksdays = ['Monkey', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previout_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date
```