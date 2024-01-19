if __name__ == '__main__':

    a = []

    a.append(12)
    a.append(9)
    a.append(7)
    a.append(4)

    s = 0
    for i in range(len(a)):
        s = s + a[i]

    print(f"list: {a}\nsum: {s}, avg: {s/len(a)}")



