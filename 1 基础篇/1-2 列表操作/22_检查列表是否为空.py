'''
题目：检查列表是否为空

描述：编写一个Python程序，检查列表是否为空。使用多种方法实现。
'''

# 解决方案
def is_empty_len(lst):
    """
    使用len()函数检查列表是否为空
    
    参数:
        lst (list): 需要检查的列表
    
    返回:
        bool: 如果列表为空则返回True，否则返回False
    """
    return len(lst) == 0

def is_empty_direct(lst):
    """
    使用直接布尔评估检查列表是否为空
    
    参数:
        lst (list): 需要检查的列表
    
    返回:
        bool: 如果列表为空则返回True，否则返回False
    """
    # 在Python中，空列表在布尔上下文中被视为False
    return not lst

def is_empty_comparison(lst):
    """
    使用与空列表比较的方法检查列表是否为空
    
    参数:
        lst (list): 需要检查的列表
    
    返回:
        bool: 如果列表为空则返回True，否则返回False
    """
    return lst == []

def is_empty_try_except(lst):
    """
    使用异常处理方法检查列表是否为空
    
    参数:
        lst (list): 需要检查的列表
    
    返回:
        bool: 如果列表为空则返回True，否则返回False
    """
    try:
        # 尝试访问第一个元素
        lst[0]
        return False  # 如果没有抛出异常，则列表不为空
    except IndexError:
        return True  # 如果抛出IndexError异常，则列表为空

# 示例输出
if __name__ == "__main__":
    # 创建示例列表
    empty_list = []
    non_empty_list = [1, 2, 3]
    
    print(f"空列表: {empty_list}")
    print(f"非空列表: {non_empty_list}")
    
    # 使用len()函数方法
    print(f"\n使用len()函数检查:")
    print(f"空列表是否为空: {is_empty_len(empty_list)}")
    print(f"非空列表是否为空: {is_empty_len(non_empty_list)}")
    
    # 使用直接布尔评估方法
    print(f"\n使用直接布尔评估检查:")
    print(f"空列表是否为空: {is_empty_direct(empty_list)}")
    print(f"非空列表是否为空: {is_empty_direct(non_empty_list)}")
    
    # 使用与空列表比较的方法
    print(f"\n使用与空列表比较检查:")
    print(f"空列表是否为空: {is_empty_comparison(empty_list)}")
    print(f"非空列表是否为空: {is_empty_comparison(non_empty_list)}")
    
    # 使用异常处理方法
    print(f"\n使用异常处理检查:")
    print(f"空列表是否为空: {is_empty_try_except(empty_list)}")
    print(f"非空列表是否为空: {is_empty_try_except(non_empty_list)}")
    
    # 性能比较说明
    print(f"\n性能比较:")
    print(f"直接布尔评估(not lst)通常是最快的方法")
    print(f"len(lst) == 0 和 lst == [] 性能相似")
    print(f"异常处理方法通常是最慢的，不推荐在此场景使用")