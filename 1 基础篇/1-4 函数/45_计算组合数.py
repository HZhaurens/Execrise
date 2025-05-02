# 45_计算组合数.py

def factorial(n):
    """计算阶乘
    
    Args:
        n: 要计算阶乘的非负整数
        
    Returns:
        n的阶乘
    """
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def combination(n, k):
    """计算组合数 C(n,k)
    
    组合数公式：C(n,k) = n! / (k! * (n-k)!)
    表示从n个不同元素中取出k个元素的组合数量
    
    Args:
        n: 总元素数量
        k: 要选取的元素数量
        
    Returns:
        组合数 C(n,k)
    """
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

# 测试
try:
    n = int(input("请输入总元素数量n: "))
    k = int(input("请输入要选取的元素数量k: "))
    
    if n < 0 or k < 0:
        print("请输入非负整数!")
    else:
        result = combination(n, k)
        print(f"C({n},{k}) = {result}")
        
        # 打印杨辉三角形（帕斯卡三角形）的前n+1行
        print("\n杨辉三角形（帕斯卡三角形）:")
        for i in range(n + 1):
            for j in range(i + 1):
                print(combination(i, j), end=" ")
            print()
except ValueError:
    print("请输入有效的整数!")