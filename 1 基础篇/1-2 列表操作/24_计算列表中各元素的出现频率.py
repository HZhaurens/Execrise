'''
题目：计算列表中各元素的出现频率

描述：编写一个Python程序，计算列表中各元素的出现频率。使用多种方法实现。
'''

# 解决方案
def count_frequency_loop(lst):
    """
    使用循环和字典计算列表中各元素的出现频率
    
    参数:
        lst (list): 需要计算频率的列表
    
    返回:
        dict: 包含元素及其出现频率的字典
    """
    frequency = {}
    
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    return frequency

def count_frequency_counter(lst):
    """
    使用collections.Counter计算列表中各元素的出现频率
    
    参数:
        lst (list): 需要计算频率的列表
    
    返回:
        Counter: 包含元素及其出现频率的Counter对象
    """
    from collections import Counter
    return Counter(lst)

def count_frequency_get(lst):
    """
    使用字典的get()方法计算列表中各元素的出现频率
    
    参数:
        lst (list): 需要计算频率的列表
    
    返回:
        dict: 包含元素及其出现频率的字典
    """
    frequency = {}
    
    for item in lst:
        # get()方法在键不存在时返回默认值0
        frequency[item] = frequency.get(item, 0) + 1
    
    return frequency

def count_frequency_setdefault(lst):
    """
    使用字典的setdefault()方法计算列表中各元素的出现频率
    
    参数:
        lst (list): 需要计算频率的列表
    
    返回:
        dict: 包含元素及其出现频率的字典
    """
    frequency = {}
    
    for item in lst:
        # setdefault()方法在键不存在时设置默认值0并返回
        frequency.setdefault(item, 0)
        frequency[item] += 1
    
    return frequency

# 示例输出
if __name__ == "__main__":
    # 创建示例列表
    numbers = [1, 2, 3, 2, 1, 3, 4, 5, 1, 2, 6, 7, 8, 7]
    fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
    
    print(f"数字列表: {numbers}")
    print(f"水果列表: {fruits}")
    
    # 使用循环和字典方法
    print(f"\n使用循环和字典计算频率:")
    print(f"数字列表频率: {count_frequency_loop(numbers)}")
    print(f"水果列表频率: {count_frequency_loop(fruits)}")
    
    # 使用collections.Counter方法
    print(f"\n使用collections.Counter计算频率:")
    print(f"数字列表频率: {count_frequency_counter(numbers)}")
    print(f"水果列表频率: {count_frequency_counter(fruits)}")
    
    # 使用字典的get()方法
    print(f"\n使用字典的get()方法计算频率:")
    print(f"数字列表频率: {count_frequency_get(numbers)}")
    print(f"水果列表频率: {count_frequency_get(fruits)}")
    
    # 使用字典的setdefault()方法
    print(f"\n使用字典的setdefault()方法计算频率:")
    print(f"数字列表频率: {count_frequency_setdefault(numbers)}")
    print(f"水果列表频率: {count_frequency_setdefault(fruits)}")
    
    # 使用Counter的其他功能
    from collections import Counter
    counter = Counter(fruits)
    print(f"\nCounter的其他功能:")
    print(f"最常见的2个元素: {counter.most_common(2)}")
    print(f"元素总数: {sum(counter.values())}")