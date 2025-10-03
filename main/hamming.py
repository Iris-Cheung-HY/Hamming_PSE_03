def hamming_distance(strand1, strand2):
    hamming_count = 0

    if len(strand1) != len(strand2):
        raise ValueError ("Not the same length")


    for char in range(0, len(strand1)):
        if strand1[char] != strand2[char]:
            hamming_count += 1
    return hamming_count


