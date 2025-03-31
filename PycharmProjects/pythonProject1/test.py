def cap(a):
    x = ".!?"
    y = a.capitalize()
    for i in range(1, len(a)):
        if a[i-1] in x:
            y = y[0:i] + " " + y[i+1].capitalize() + y[i+2:]
    return y

print(cap("sadkj. aflsk! ddsf? eırj"))
