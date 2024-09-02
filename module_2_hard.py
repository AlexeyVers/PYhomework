for i in range(3, 21):
    key_ = str()
    for k in range(1, i + 1):
        for u in range(1, i + 1):
            if i >= k + u and (k + u) % i == 0:
                key_ = str(key_) + str(k) + str(u)
    print(i, '-', key_)
