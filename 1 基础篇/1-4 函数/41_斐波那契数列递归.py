# 41_斐波那契数列递归.py

def fibonacci(n):
    """使用递归计算斐波那契数列的第n项
    
    斐波那契数列：0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) 当 n > 1
    
    Args:
        n: 要计算的项数（从0开始）
        
    Returns:
        斐波那契数列的第n项
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 测试
try:
    num = int(input("请输入一个非负整数: "))
    if num < 0:
        print("请输入非负整数!")
    else:
        result = fibonacci(num)
        print(f"斐波那契数列的第{num}项是: {result}")
        
        # 打印斐波那契数列前n+1项
        print(f"斐波那契数列的前{num+1}项:")
        for i in range(num + 1):
            print(fibonacci(i), end=" ")
        print()
except ValueError:
    print("请输入有效的整数!")