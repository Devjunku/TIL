def solution(n):
    n_s = list(str(n))

    for s in n_s:
        if s == "0" or n % int(s) != 0:
            return False

    return True

if __name__ == "__main__":
    print(solution(110))