'''
题目：计算两个数的和

描述：编写一个Python程序，接收用户输入的两个数字，并计算它们的和。
'''

# 解决方案
def calculate_sum(a, b):
    """
    计算两个数的和
    
    参数:
        a (float/int): 第一个数
        b (float/int): 第二个数
    
    返回:
        float/int: 两个数的和
    """
    return a + b

# 示例输出
if __name__ == "__main__":
    # 从用户获取输入
    try:
        num1 = float(input("请输入第一个数: "))
        num2 = float(input("请输入第二个数: "))
        
        # 计算并显示结果
        result = calculate_sum(num1, num2)
        print(f"{num1} + {num2} = {result}")
    except ValueError:
        print("请输入有效的数字!")