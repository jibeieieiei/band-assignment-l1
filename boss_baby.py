# Boss Baby's Revenge

def boss_baby_revenge(text: str = "SSRSSRSSSRR"):

    res = "Bad Boy"

    if text[0] == "R" or text[-1] == "S":
        return res

    # Initial Params
    s_time = 0
    r_time = 0
    find_r = False

    for char in text:
        if char == 'S':
            # When we find R
            if find_r:  # find_r == True
                s_time, r_time, find_r = [1, 0, False]
            else:
                s_time += 1
                res = "Bad Boy"
        if char == 'R':
            r_time += 1
            find_r = True
        # Check Finish With R
        if find_r:
            if r_time - s_time >= 0:
                res = "Good Boy"
    return res


def main():
    text = input()
    result = boss_baby_revenge(text)
    print(result)


if __name__ == "__main__":
    main()
