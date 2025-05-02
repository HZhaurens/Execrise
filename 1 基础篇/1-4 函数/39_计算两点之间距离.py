# 39_计算两点之间距离.py

import math

def calculate_distance(x1, y1, x2, y2):
    """计算二维平面上两点之间的距离
    
    使用欧几里得距离公式：d = √[(x2 - x1)² + (y2 - y1)²]
    
    Args:
        x1: 第一个点的x坐标
        y1: 第一个点的y坐标
        x2: 第二个点的x坐标
        y2: 第二个点的y坐标
        
    Returns:
        两点之间的距离
    """
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

# 测试
print("请输入第一个点的坐标:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("请输入第二个点的坐标:")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

distance = calculate_distance(x1, y1, x2, y2)
print(f"两点之间的距离为: {distance}")