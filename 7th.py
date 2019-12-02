

def ans(lst, x):
    tflst = []
    for i in range(len(lst)):
        if x > lst[i]:
            tflst.append(True)
        elif x <= lst[i]:
            tflst.append(False)
    return tflst


print(ans([3, 7, 3, 8, 5, 0], 5))
