
def cal_moyenne(list_a):
    sum = 0

    if not len(list_a):
        return 0

    for val in list_a:
        sum = sum + val
    
    return sum/len(list_a)



def cal_mediane(list_a):
    list_a.sort()
    a = len(list_a)%2
    mid = int(len(list_a)/2)
    if a:
        return list_a[mid]
    else:
        return (list_a[mid] + list_a[mid-1])/2



def cal_ecart(list_a):
    moyenne = cal_moyenne(list_a)
    ecart = 0.0

    for val in list_a:
        ecart = ecart + (val - moyenne) * (val - moyenne)

    return ecart


def is_geometrique(list_a):
    start = float(list_a[1]) / float(list_a[0])

    if 0 in list_a:
        return False
    
    for i in range(2, len(list_a)) :
        if list_a[i] == list_a[i-1] * start :
            continue
        else:
            return False
    
    return True


def is_arithmetique(list_a):
    start = list_a[1] - list_a[0]
    
    for i in range(2, len(list_a)) :
        if list_a[i] == list_a[i-1] + start :
            continue
        else:
            return False
    
    return True


def is_geometrique2(n, list_a):
    start = float(list_a[1]) / float(list_a[0])
    suivant = []

    if 0 in list_a:
        return False
    
    for i in range(1, len(list_a)) :
        if list_a[i] == list_a[i-1] * start :
            continue
        else:
            return False
    
    if n:
        suivant.append(list_a[-1] * start)

        for i in range(n-1):
            suivant.append(suivant[-1] * start)
    
    return True, suivant


def is_arithmetique2(n, list_a):
    dis = list_a[1] - list_a[0]
    suivant = []
    
    for i in range(2, len(list_a)) :
        if list_a[i] == list_a[i-1] + dis :
            continue
        else:
            return False
    
    if n:
        suivant.append(list_a[-1] + dis)

        for i in range(n-1):
            suivant.append(suivant[-1] + dis)
    
    return True, suivant