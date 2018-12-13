""" Classify """
def main():
    """ Main """
    lst = []
    dxx = {}
    txt = ''
    while True:
        num = input()
        if num == "END":
            break
        else:
            lst.append(num)
    lst.sort()
    for i in lst:
        year = int(i[0:2]), int(i[2:4])
        if year in dxx:
            dxx[year] += 1
        else:
            dxx[year] = 1
    for j in sorted(dxx):
        if j[0] == txt:
            print('--', j[1], dxx[j])
        else:
            print(j[0], j[1], dxx[j])
            txt = j[0]
main()
