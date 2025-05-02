'''
题目：将摄氏温度转换为华氏温度

描述：编写一个Python程序，接收用户输入的摄氏温度，并将其转换为华氏温度。
转换公式：华氏温度 = 摄氏温度 * 9/5 + 32
'''

# 解决方案
def celsius_to_fahrenheit(celsius):
    """
    将摄氏温度转换为华氏温度
    
    参数:
        celsius (float): 摄氏温度
    
    返回:
        float: 华氏温度
    """
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    将华氏温度转换为摄氏温度
    
    参数:
        fahrenheit (float): 华氏温度
    
    返回:
        float: 摄氏温度
    """
    return (fahrenheit - 32) * 5/9

# 示例输出
if __name__ == "__main__":
    try:
        # 从用户获取输入
        celsius = float(input("请输入摄氏温度: "))
        
        # 转换并显示结果
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
        
        # 额外功能：华氏转摄氏
        print("\n华氏温度转换为摄氏温度示例:")
        test_fahrenheit = 98.6  # 人体正常体温（华氏）
        test_celsius = fahrenheit_to_celsius(test_fahrenheit)
        print(f"{test_fahrenheit}°F = {test_celsius:.2f}°C")
        
        # 一些常见温度点
        print("\n常见温度点:")
        print(f"水的冰点: 0°C = {celsius_to_fahrenheit(0):.2f}°F")
        print(f"水的沸点: 100°C = {celsius_to_fahrenheit(100):.2f}°F")
        print(f"人体正常体温: 37°C = {celsius_to_fahrenheit(37):.2f}°F")
    except ValueError:
        print("请输入有效的数字!")