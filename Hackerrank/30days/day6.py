if __name__ == "__main__":

    def Even(s):
        l = len(s)
        output = ""
        for i in range(0, l, 2):
            output += s[i]
        return output

    def Odd(s):
        l = len(s)
        output = ""
        for i in range(1, l, 2):
            output += s[i]
        return output

    n = int(input())
    for i in range(n):
        s = input()
        print(Even(s) + " " + Odd(s))