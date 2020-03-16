def minimumSwaps(arr):
    count = 0
    corr_arr = sorted(arr)
    lut = {i:j for i, j in enumerate(arr)}

    for i, j in enumerate(arr):
        cor_val = corr_arr[i]
        if j != cor_val:
            cor_idx = lut[cor_val]
            arr[i], arr[cor_idx] = arr[cor_idx], arr[i]
            lut[j] = cor_idx
            lut[cor_val] = i
            count += 1
    return count
