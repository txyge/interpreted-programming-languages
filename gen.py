import random

def create_file(filename, N, K):
    with open(filename, 'w') as f:
        f.write(f"{N} {K}\n")
        for _ in range(N):
            height = random.randint(-10_000_000, 10_000_000)
            f.write(f"{height}\n")

# Параметры для файла A
N_A = 1000  # или любое другое значение в пределах 1 < N ≤ 10 000 000
K_A = 500   # или любое другое значение в пределах 1 < K < N

# Параметры для файла B
N_B = 2000  # или любое другое значение в пределах 1 < N ≤ 10 000 000
K_B = 1000  # или любое другое значение в пределах 1 < K < N

create_file('27-170a.txt', N_A, K_A)
create_file('27-170.txt', N_B, K_B)
