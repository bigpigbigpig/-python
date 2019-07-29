
## 数据模型
不是特别的明白

## 数据结构
1. 列表推导 `[(x, y) for x in range(10) for y in range(10)]`
2. 生成器表达式 `(...)` 将列表推导的 `[]` 替换成 `()`, 逐一产生元素，避免浪费内存
3. 元组拆包 / 具名元组
    * 元组拆包 `a, b, *var = range(10)`
    * 具名元组 `collections.namedtuple('class name', 'dual name')`
4. list
    * 切片 `s[::-1]`
    * 赋值 `s[2:8] = [10,20]`
    * `+` `*` 
5. 数组
    * `array`当只存数字类型时，替换`list`
    * `memoryview`
    * `pickle.dump`
    * `Numpy` `Scipy`