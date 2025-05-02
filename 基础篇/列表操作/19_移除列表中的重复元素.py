'''
题目：移除列表中的重复元素

描述：编写一个Python程序，移除列表中的重复元素。使用多种方法实现。
'''

# 解决方案
def remove_duplicates_set(numbers):
    """
    使用集合(set)移除列表中的重复元素
    
    参数:
        numbers (list): 包含元素的列表
    
    返回:
        list: 移除重复元素后的列表
    """
    # 使用集合的特性自动去除重复元素，然后转回列表
    return list(set(numbers))

def remove_duplicates_loop(numbers):
    """
    使用循环方法移除列表中的重复元素
    
    参数:
        numbers (list): 包含元素的列表
    
    返回:
        list: 移除重复元素后的列表
    """
    result = []
    for item in numbers:
        if item not in result:
            result.append(item)
    return result

def remove_duplicates_dict(numbers):
    """
    使用字典方法移除列表中的重复元素
    
    参数:
        numbers (list): 包含元素的列表
    
    返回:
        list: 移除重复元素后的列表
    """
    # 利用字典键的唯一性去除重复元素
    return list(dict.fromkeys(numbers))

def remove_duplicates_comprehension(numbers):
    """
    使用列表推导式移除列表中的重复元素
    
    参数:
        numbers (list): 包含元素的列表
    
    返回:
        list: 移除重复元素后的列表
    """
    result = []
    [result.append(item) for item in numbers if item not in result]
    return result

# 示例输出
if __name__ == "__main__":
    # 创建示例列表
    numbers = [1, 2, 3, 2, 1, 5, 6, 7, 8, 8, 7]
    strings = ["apple", "banana", "apple", "orange", "banana", "grape"]
    
    print(f"原始数字列表: {numbers}")
    print(f"原始字符串列表: {strings}")
    
    # 使用集合方法
    print(f"\n使用集合方法移除重复元素:")
    print(f"数字列表: {remove_duplicates_set(numbers)}")
    print(f"字符串列表: {remove_duplicates_set(strings)}")
    
    # 使用循环方法
    print(f"\n使用循环方法移除重复元素:")
    print(f"数字列表: {remove_duplicates_loop(numbers)}")
    print(f"字符串列表: {remove_duplicates_loop(strings)}")
    
    # 使用字典方法
    print(f"\n使用字典方法移除重复元素:")
    print(f"数字列表: {remove_duplicates_dict(numbers)}")
    print(f"字符串列表: {remove_duplicates_dict(strings)}")
    
    # 使用列表推导式方法
    print(f"\n使用列表推导式方法移除重复元素:")
    print(f"数字列表: {remove_duplicates_comprehension(numbers)}")
    print(f"字符串列表: {remove_duplicates_comprehension(strings)}")
    
    # 注意：使用集合方法会改变元素的原始顺序
    print(f"\n注意：使用集合方法会改变元素的原始顺序，而其他方法会保留原始顺序")