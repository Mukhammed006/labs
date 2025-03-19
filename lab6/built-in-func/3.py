def determine(test_num, test):
    rev_test = ''.join((reversed(test)))
    if test==rev_test:
        print("YES, It is a palindrom")
    else:
        print("NO, It is not a palindrom")

a = input()

determine(1, a)