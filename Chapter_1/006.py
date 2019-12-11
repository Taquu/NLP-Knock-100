def n_gram(target, n):
    return[target[num:num+n] for num in range (len(target) - n + 1)]

target_1 = "paraparaparadise"
target_2 = "paragraph"

#bi-gramの作成
X = n_gram(target_1, 2)
Y = n_gram(target_2, 2)

#和集合の作成
X_Y_union = set(X) | set(Y)
print("和集合:" + str(X_Y_union))

#積集合の作成
X_Y_inter = set(X) & set(Y)
print("積集合:" + str(X_Y_inter))

#差集合の作成
X_Y_diff = set(X) - set(Y)
print("差集合:" + str(X_Y_diff))

#'se'の有無の確認
print("seがXに含まれる:" + str("se" in X))
print("seがYに含まれる:" + str("se" in Y))
