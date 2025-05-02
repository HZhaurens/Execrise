'''
题目：计算圆的面积

描述：编写一个Python程序，接收用户输入的圆的半径，并计算圆的面积。
圆的面积计算公式：面积 = π * 半径的平方
'''

# 导入数学模块以使用π值
import math

# 解决方案
def calculate_circle_area(radius):
    """
    计算圆的面积
    
    参数:
        radius (float): 圆的半径
    
    返回:
        float: 圆的面积
    """
    return math.pi * radius ** 2

# 示例输出
if __name__ == "__main__":
    try:
        # 从用户获取半径输入
        radius = float(input("请输入圆的半径: "))
        
        # 检查半径是否为正数
        if radius <= 0:
            print("半径必须是正数!")
        else:
            # 计算并显示结果
            area = calculate_circle_area(radius)
            print(f"半径为 {radius} 的圆的面积是: {area:.2f}")
    except ValueError:
        print("请输入有效的数字!")