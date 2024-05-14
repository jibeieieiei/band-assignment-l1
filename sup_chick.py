def sup_chicken(n: int, k: int, point: str):
    # n: numbers of chicken
    # k: the length of the roof supermain can carry
    # x: position in x-axis (point: str)
    x = [int(i) for i in point.strip().split()]
    cover = -99
    for i in range(n):
        # Initial Cover
        n_cover = 1
        for j in range(i, n):
            if x[i] != x[j]:
                max_pos = x[i] + k
                if x[j] < max_pos:
                    n_cover += 1
        if n_cover > cover:
            cover = n_cover
    print(cover)
    return cover


def main():
    nk = input().split()
    n, k = int(nk[0]), int(nk[1])
    point = input()
    sup_chicken(n, k, point)
    # sup_chicken(5, 5, "2 5 10 12 15")
    # sup_chicken(6, 10, "1 11 30 34 35 37")


if __name__ == "__main__":
    main()
