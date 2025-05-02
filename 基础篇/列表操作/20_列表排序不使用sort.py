'''
题目：列表排序(不使用sort())

描述：编写一个Python程序，对列表进行排序，但不使用内置的sort()或sorted()函数。实现多种排序算法。
'''

# 解决方案
def bubble_sort(numbers):
    """
    使用冒泡排序算法对列表进行排序
    
    参数:
        numbers (list): 需要排序的列表
    
    返回:
        list: 排序后的列表
    """
    # 创建列表的副本，避免修改原始列表
    result = numbers.copy()
    n = len(result)
    
    # 冒泡排序算法
    for i in range(n):
        # 每次循环后，最大的元素会被放到最后，所以下一次循环可以少比较一个元素
        for j in range(0, n-i-1):
            if result[j] > result[j+1]:
                # 交换元素
                result[j], result[j+1] = result[j+1], result[j]
    
    return result

def selection_sort(numbers):
    """
    使用选择排序算法对列表进行排序
    
    参数:
        numbers (list): 需要排序的列表
    
    返回:
        list: 排序后的列表
    """
    # 创建列表的副本，避免修改原始列表
    result = numbers.copy()
    n = len(result)
    
    # 选择排序算法
    for i in range(n):
        # 假设当前位置的元素是最小的
        min_idx = i
        # 在剩余未排序的元素中寻找最小值
        for j in range(i+1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        
        # 将找到的最小元素放到已排序序列的末尾
        result[i], result[min_idx] = result[min_idx], result[i]
    
    return result

def insertion_sort(numbers):
    """
    使用插入排序算法对列表进行排序
    
    参数:
        numbers (list): 需要排序的列表
    
    返回:
        list: 排序后的列表
    """
    # 创建列表的副本，避免修改原始列表
    result = numbers.copy()
    n = len(result)
    
    # 插入排序算法
    for i in range(1, n):
        key = result[i]
        j = i-1
        # 将比key大的元素向右移动
        while j >= 0 and result[j] > key:
            result[j+1] = result[j]
            j -= 1
        result[j+1] = key
    
    return result

def merge_sort(numbers):
    """
    使用归并排序算法对列表进行排序
    
    参数:
        numbers (list): 需要排序的列表
    
    返回:
        list: 排序后的列表
    """
    # 创建列表的副本，避免修改原始列表
    result = numbers.copy()
    
    # 如果列表长度小于等于1，则已经排序好
    if len(result) <= 1:
        return result
    
    # 分割列表
    mid = len(result) // 2
    left = merge_sort(result[:mid])
    right = merge_sort(result[mid:])
    
    # 合并两个已排序的子列表
    return merge(left, right)

def merge(left, right):
    """
    合并两个已排序的列表
    
    参数:
        left (list): 左侧已排序列表
        right (list): 右侧已排序列表
    
    返回:
        list: 合并后的已排序列表
    """
    result = []
    i = j = 0
    
    # 比较两个列表的元素并合并
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 添加剩余的元素
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# 示例输出
if __name__ == "__main__":
    # 创建示例列表
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    print(f"原始列表: {numbers}")
    
    # 使用冒泡排序
    bubble_sorted = bubble_sort(numbers)
    print(f"\n冒泡排序结果: {bubble_sorted}")
    
    # 使用选择排序
    selection_sorted = selection_sort(numbers)
    print(f"选择排序结果: {selection_sorted}")
    
    # 使用插入排序
    insertion_sorted = insertion_sort(numbers)
    print(f"插入排序结果: {insertion_sorted}")
    
    # 使用归并排序
    merge_sorted = merge_sort(numbers)
    print(f"归并排序结果: {merge_sorted}")
    
    # 验证原始列表没有被修改
    print(f"\n验证原始列表没有被修改: {numbers}")
    
    # 比较不同排序算法的结果
    print(f"\n所有排序算法的结果是否一致: {bubble_sorted == selection_sorted == insertion_sorted == merge_sorted}")