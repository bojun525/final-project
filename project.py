# ========= 讀取輸入 =========
n_react = int(input("反應物數量: "))
n_prod  = int(input("生成物數量: "))

reactants = []
products = []

print("\n輸入反應物（係數、初始濃度）")
for i in range(n_react):
    coeff = float(input(f"反應物 {i+1} 係數: "))
    conc  = float(input(f"反應物 {i+1} 初始濃度: "))
    reactants.append((coeff, conc))

print("\n輸入生成物（係數、初始濃度）")
for i in range(n_prod):
    coeff = float(input(f"生成物 {i+1} 係數: "))
    conc  = float(input(f"生成物 {i+1} 初始濃度: "))
    products.append((coeff, conc))

K = float(input("\n輸入平衡常數 K: "))

# ========= 平衡函數 =========
def equilibrium(x):
    num = 1.0
    den = 1.0

    for coeff, conc0 in products:
        C = conc0 + coeff * x
        if C <= 0:
            return 1e6
        num *= C ** coeff

    for coeff, conc0 in reactants:
        A = conc0 - coeff * x
        if A <= 0:
            return 1e6
        den *= A ** coeff

    return K - num / den

# ========= 二分法求解 =========
x_low = 0.0
x_high = min(conc / coeff for coeff, conc in reactants)
tolerance = 1e-6

while x_high - x_low > tolerance:
    x_mid = (x_low + x_high) / 2
    if equilibrium(x_mid) > 0:
        x_low = x_mid
    else:
        x_high = x_mid

x_solution = (x_low + x_high) / 2

# ========= 輸出結果 =========
print("\n平衡濃度：")

for i, (coeff, conc0) in enumerate(reactants):
    print(f"反應物 {i+1}: {conc0 - coeff * x_solution:.4f}")

for i, (coeff, conc0) in enumerate(products):
    print(f"生成物 {i+1}: {conc0 + coeff * x_solution:.4f}")
