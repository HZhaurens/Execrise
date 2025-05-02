'''
题目：合并两个列表

描述：编写一个Python程序，将两个列表合并为一个新的列表。
'''

# 解决方案
def merge_lists_plus(list1, list2):
    """
    使用+运算符合并两个列表
    
    参数:
        list1 (list): 第一个列表
        list2 (list): 第二个列表
    
    返回:
        list: 合并后的新列表
    """
    return list1 + list2

def merge_lists_extend(list1, list2):
    """
    使用extend方法合并两个列表
    
    参数:
        list1 (list): 第一个列表
        list2 (list): 第二个列表
    
    返回:
        list: 合并后的新列表
    """
    result = list1.copy()  # 创建第一个列表的副本
    result.extend(list2)   # 将第二个列表添加到副本中
    return result

def merge_lists_comprehension(list1, list2):
    """
    使用列表推导式合并两个列表
    
    参数:
        list1 (list): 第一个列表
        list2 (list): 第二个列表
    
    返回:
        list: 合并后的新列表
    """
    return [item for item in list1] + [item for item in list2]

# 示例输出
if __name__ == "__main__":
    # 创建两个示例列表
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    
    print(f"列表1: {list1}")
    print(f"列表2: {list2}")
    
    # 使用+运算符合并
    merged_plus = merge_lists_plus(list1, list2)
    print(f"\n使用+运算符合并: {merged_plus}")
    
    # 使用extend方法合并
    merged_extend = merge_lists_extend(list1, list2)
    print(f"使用extend方法合并: {merged_extend}")
    
    # 使用列表推导式合并
    merged_comprehension = merge_lists_comprehension(list1, list2)
    print(f"使用列表推导式合并: {merged_comprehension}")
    
    # 验证原始列表没有被修改
    print(f"\n验证原始列表1: {list1}")
    print(f"验证原始列表2: {list2}")