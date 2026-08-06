def lcsub(s1, s2):
	m = len(s1)
	n = len(s2)

	dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if s1[i - 1] == s2[j - 1]:
				dp[i][j] = dp[i - 1][j - 1] + 1
			else:
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

	i = m
	j = n
	lcs = ""

	while i > 0 and j > 0:
		if s1[i - 1] == s2[j - 1]:
			lcs = s1[i - 1] + lcs
			i -= 1
			j -= 1
		elif dp[i - 1][j] > dp[i][j - 1]:
			i -= 1
		else:
			j -= 1

	return lcs, dp[m][n]


seq1 = input("Enter the first sequence: ")
seq2 = input("Enter te second sequence: ")

lcs, length = lcsub(seq1, seq2)

print("\nLongest Common Subsequence:", lcs)
print("Length of LCS:", length)

# Enter the first sequence: ritesh
# Enter te second sequence: eh

# Longest Common Subsequence: eh
# Length of LCS: 2
