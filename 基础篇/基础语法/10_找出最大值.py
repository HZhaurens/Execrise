'''
题目：找出两个数中的最大值

描述：编写一个Python程序，接收用户输入的两个数，并找出其中的最大值。
'''

# 解决方案
def find_maximum(a, b):
    """
    找出两个数中的最大值
    
    参数:
        a (float/int): 第一个数
        b (float/int): 第二个数
    
    返回:
        float/int: 两个数中的最大值
    """
    # 方法一：使用if-else语句
    if a > b:
        return a
    else:
        return b

def find_maximum_builtin(a, b):
    """
    使用内置函数找出两个数中的最大值
    
    参数:
        a (float/int): 第一个数
        b (float/int): 第二个数
    
    返回:
        float/int: 两个数中的最大值
    """
    # 方法二：使用内置的max函数
    return max(a, b)

# 示例输出
if __name__ == "__main__":
    try:
        # 从用户获取输入
        num1 = float(input("请输入第一个数: "))
        num2 = float(input("请输入第二个数: "))
        
        # 使用if-else方法
        max_value = find_maximum(num1, num2)
        print(f"使用if-else方法找到的最大值: {max_value}")
        
        # 使用内置函数方法
        max_value_builtin = find_maximum_builtin(num1, num2)
        print(f"使用内置函数方法找到的最大值: {max_value_builtin}")
        
        # 处理相等的情况
        if num1 == num2:
            print("两个数相等")
    except ValueError:
        print("请输入有效的数字!")