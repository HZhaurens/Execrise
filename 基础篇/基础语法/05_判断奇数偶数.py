'''
题目：判断一个数是奇数还是偶数

描述：编写一个Python程序，接收用户输入的一个整数，判断它是奇数还是偶数。
'''

# 解决方案
def is_even(number):
    """
    判断一个数是否为偶数
    
    参数:
        number (int): 需要判断的整数
    
    返回:
        bool: 如果是偶数返回True，否则返回False
    """
    return number % 2 == 0

def check_odd_even(number):
    """
    判断并输出一个数是奇数还是偶数
    
    参数:
        number (int): 需要判断的整数
    """
    if is_even(number):
        print(f"{number} 是偶数")
    else:
        print(f"{number} 是奇数")

# 示例输出
if __name__ == "__main__":
    try:
        # 从用户获取输入
        num = int(input("请输入一个整数: "))
        
        # 判断并显示结果
        check_odd_even(num)
    except ValueError:
        print("请输入有效的整数!")