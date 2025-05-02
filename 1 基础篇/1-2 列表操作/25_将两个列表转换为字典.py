'''
题目：将两个列表转换为字典

描述：编写一个Python程序，将两个列表转换为字典，其中一个列表的元素作为键，另一个列表的元素作为值。使用多种方法实现。
'''

# 解决方案
def lists_to_dict_zip(keys, values):
    """
    使用zip()函数将两个列表转换为字典
    
    参数:
        keys (list): 作为字典键的列表
        values (list): 作为字典值的列表
    
    返回:
        dict: 由两个列表组成的字典
    """
    # 如果两个列表长度不同，只会使用较短列表的所有元素
    return dict(zip(keys, values))

def lists_to_dict_comprehension(keys, values):
    """
    使用字典推导式将两个列表转换为字典
    
    参数:
        keys (list): 作为字典键的列表
        values (list): 作为字典值的列表
    
    返回:
        dict: 由两个列表组成的字典
    """
    # 使用min确保不会超出任何一个列表的范围
    return {keys[i]: values[i] for i in range(min(len(keys), len(values)))}

def lists_to_dict_loop(keys, values):
    """
    使用循环将两个列表转换为字典
    
    参数:
        keys (list): 作为字典键的列表
        values (list): 作为字典值的列表
    
    返回:
        dict: 由两个列表组成的字典
    """
    result = {}
    # 使用较短列表的长度作为循环次数
    length = min(len(keys), len(values))
    
    for i in range(length):
        result[keys[i]] = values[i]
    
    return result

def lists_to_dict_map(keys, values):
    """
    使用map()函数将两个列表转换为字典
    
    参数:
        keys (list): 作为字典键的列表
        values (list): 作为字典值的列表
    
    返回:
        dict: 由两个列表组成的字典
    """
    # 使用较短列表的长度
    length = min(len(keys), len(values))
    return dict(map(lambda i: (keys[i], values[i]), range(length)))

# 示例输出
if __name__ == "__main__":
    # 创建示例列表
    keys = ["name", "age", "city", "email"]
    values = ["Alice", 25, "New York", "alice@example.com"]
    
    # 长度不同的列表
    keys2 = ["a", "b", "c", "d", "e"]
    values2 = [1, 2, 3]
    
    print(f"键列表: {keys}")
    print(f"值列表: {values}")
    
    # 使用zip()函数方法
    zip_dict = lists_to_dict_zip(keys, values)
    print(f"\n使用zip()函数转换: {zip_dict}")
    
    # 使用字典推导式方法
    comprehension_dict = lists_to_dict_comprehension(keys, values)
    print(f"使用字典推导式转换: {comprehension_dict}")
    
    # 使用循环方法
    loop_dict = lists_to_dict_loop(keys, values)
    print(f"使用循环转换: {loop_dict}")
    
    # 使用map()函数方法
    map_dict = lists_to_dict_map(keys, values)
    print(f"使用map()函数转换: {map_dict}")
    
    # 处理长度不同的列表
    print(f"\n处理长度不同的列表:")
    print(f"键列表: {keys2}")
    print(f"值列表: {values2}")
    print(f"使用zip()函数转换: {lists_to_dict_zip(keys2, values2)}")
    print(f"使用字典推导式转换: {lists_to_dict_comprehension(keys2, values2)}")
    print(f"使用循环转换: {lists_to_dict_loop(keys2, values2)}")
    print(f"使用map()函数转换: {lists_to_dict_map(keys2, values2)}")