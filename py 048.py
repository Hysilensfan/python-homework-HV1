# first method
# this method is slower but it's easier to understand
for f in range(int(input())):
    storing, index_counts, tot = [], [], 1  # create two lists and initialize counter. Note: lists must not reference each other; otherwise results will affect each other
    P_1 = P_2 = P_3 = P_4 = P_5 = ""  # initialize P1~P5 as empty strings
    for w in [bin(x).replace("0b", "").zfill(4) for x in [int(g, 16) for g in input()]]:  # convert input from hexadecimal → integer → binary, remove Python's "0b", then pad to 4 bits. Final format: nnnn nnnn nnnn nnnn
        storing += w  # concatenate them together
    for i in range(5):
        storing.insert((2 ** i) - 1, f"P{i + 1}")  # insert P1~P5
    for n in storing:
        if n == "1":  # when encountering 1, add its position to index_counts
            index_counts.append(tot)
        tot += 1
    storing, tot = [], 0  # reset storing and counter. Note: counter is reset to 1 here
    index_counts = [bin(x).replace("0b", "").zfill(5) for x in index_counts]  # convert positions to binary and pad to 5 bits. Final format like: nnnnn nnnnn nnnnn nnnnn
    for u in range(len(index_counts)):
        P_1 += index_counts[u][0]  # append bit 1 of that binary value
        P_2 += index_counts[u][1]  # append bit 2 of that binary value
        P_3 += index_counts[u][2]  # append bit 3 of that binary value
        P_4 += index_counts[u][3]  # append bit 4 of that binary value
        P_5 += index_counts[u][4]  # append bit 5 of that binary value
    storing.append(P_1)
    storing.append(P_2)
    storing.append(P_3)
    storing.append(P_4)
    storing.append(P_5)  # append P1~P5 respectively into the list
    for b in range(len(storing)):
        for t in storing[b]:
            if t == "1":  # if the binary string contains 1, increment counter
                tot += 1
        storing[b] = 0 if tot % 2 == 0 else 1  # even parity check: even count → 0; otherwise → 1
        tot = 0  # reset counter for next iteration
    print(*storing[::-1], sep="")  # unpack and print without separators

# The final print section could also be written like this:
# for c in storing[::-1]:
  #     print(c,end="")
  # print(end="\n")

# second method
for _ in range(int(input())):
    data = input()

    bits = []

    # hex → bits
    for c in data:
        b = bin(int(c, 16))[2:].zfill(4)
        for bit in b:
            bits.append(bit)

    # parity buckets(used for five groups) 
    p = [0, 0, 0, 0, 0]
    pos = 1

    for bit in bits:
        if bit == "1":
            for i in range(5):
                if pos & (1 << i):
                    p[i] += 1
        pos += 1

    # even/odd decide
    for i in range(5):
        p[i] %= 2

    # output(reverse the order)
    print(p[4], p[3], p[2], p[1], p[0], sep="")
