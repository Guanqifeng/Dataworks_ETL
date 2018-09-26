# 编写一个程序，该程序基于分子中的氢、碳和氧原子的数量计算碳水化合物的分子
# 量（以克/摩尔计）。程序应提示用户输入氢原子的数量、碳原子的数量和氧原子的数量。然
# 后程序基于这些单独的原子量打印所有原子的总组合分子量。

def main(n):
    print("Calculate Round Area from diameter !")
    C = 12.0107
    H = 1.00794
    O = 15.9994
    formula_value = C*n+(H*2+O)*n
    print("Carbohydrates quality is :"+str(formula_value))
if __name__ == '__main__':
    n = eval(input("Please enter your number of C: "))
    main(n)