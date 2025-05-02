'''
题目：克隆或复制列表

描述：编写一个Python程序，克隆或复制一个列表。使用多种方法实现。
'''

# 解决方案
def clone_list_slice(lst):
    """
    使用切片操作克隆列表
    
    参数:
        lst (list): 需要克隆的列表
    
    返回:
        list: 克隆后的新列表
    """
    return lst[:]

def clone_list_copy(lst):
    """
    使用copy()方法克隆列表
    
    参数:
        lst (list): 需要克隆的列表
    
    返回:
        list: 克隆后的新列表
    """
    return lst.copy()

def clone_list_list(lst):
    """
    使用list()函数克隆列表
    
    参数:
        lst (list): 需要克隆的列表
    
    返回:
        list: 克隆后的新列表
    """
    return list(lst)

def clone_list_comprehension(lst):
    """
    使用列表推导式克隆列表
    
    参数:
        lst (list): 需要克隆的列表
    
    返回:
        list: 克隆后的新列表
    """
    return [item for item in lst]

def clone_list_extend(lst):
    """
    使用extend()方法克隆列表
    
    参数:
        lst (list): 需要克隆的列表
    
    返回:
        list: 克隆后的新列表
    """
    new_list = []
    new_list.extend(lst)
    return new_list

def clone_list_deepcopy(lst):
    """
    使用deepcopy()函数克隆列表（深拷贝）
    
    参数:
        lst (list): 需要克隆的列表
    
    返回:
        list: 克隆后的新列表
    """
    import copy
    return copy.deepcopy(lst)

# 示例输出
if __name__ == "__main__":
    # 创建示例列表
    original_list = [1, 2, 3, 4, 5]
    nested_list = [1, 2, [3, 4], 5]
    
    print(f"原始列表: {original_list}")
    print(f"嵌套列表: {nested_list}")
    
    # 使用切片操作
    slice_clone = clone_list_slice(original_list)
    print(f"\n使用切片操作克隆: {slice_clone}")
    print(f"是否是不同对象: {slice_clone is not original_list}")
    
    # 使用copy()方法
    copy_clone = clone_list_copy(original_list)
    print(f"\n使用copy()方法克隆: {copy_clone}")
    print(f"是否是不同对象: {copy_clone is not original_list}")
    
    # 使用list()函数
    list_clone = clone_list_list(original_list)
    print(f"\n使用list()函数克隆: {list_clone}")
    print(f"是否是不同对象: {list_clone is not original_list}")
    
    # 使用列表推导式
    comprehension_clone = clone_list_comprehension(original_list)
    print(f"\n使用列表推导式克隆: {comprehension_clone}")
    print(f"是否是不同对象: {comprehension_clone is not original_list}")
    
    # 使用extend()方法
    extend_clone = clone_list_extend(original_list)
    print(f"\n使用extend()方法克隆: {extend_clone}")
    print(f"是否是不同对象: {extend_clone is not original_list}")
    
    # 使用deepcopy()函数（深拷贝）
    deepcopy_clone = clone_list_deepcopy(nested_list)
    print(f"\n使用deepcopy()函数克隆嵌套列表: {deepcopy_clone}")
    print(f"是否是不同对象: {deepcopy_clone is not nested_list}")
    
    # 浅拷贝与深拷贝的区别演示
    print(f"\n浅拷贝与深拷贝的区别演示:")
    shallow_copy = clone_list_slice(nested_list)
    deep_copy = clone_list_deepcopy(nested_list)
    
    # 修改嵌套列表中的嵌套元素
    nested_list[2][0] = 'X'
    
    print(f"修改后的原始嵌套列表: {nested_list}")
    print(f"浅拷贝的嵌套列表: {shallow_copy} (嵌套元素也被修改)")
    print(f"深拷贝的嵌套列表: {deep_copy} (嵌套元素不受影响)")