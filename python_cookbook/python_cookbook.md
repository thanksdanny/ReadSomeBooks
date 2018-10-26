# python cookbook
1. day 01 p01-p39 (第一章 数据结构和算法)
    * p10 的程序 yeild还需要再理解一下
    * 查找最大或最小的 N 个元素(使用heapq模块的两个函数nlargest()和nsmallest()) p12

2. day 02 p40-p80(第二章 字符串和文本)
    * re.split()比str.split()能更灵活切割
    ```python
    # demo
    line = 'asdf fjsk; adef, fjek,askd, foo'
    import re
    re.split(r'[;,\s]\s*', line)
    ```
    *
