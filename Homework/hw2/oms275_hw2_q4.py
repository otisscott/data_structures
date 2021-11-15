def e_approx(n):
    under = 1
    approx = 1
    for i in range(n+1):
        if i != 0:
            under *= i
            approx += 1/under
    return approx


def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)
