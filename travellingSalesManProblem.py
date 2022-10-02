n = 4 # there are four nodes in example graph (graph is 1-based)
dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [
	0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]

memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]


def fun(i, mask):
	if mask == ((1 << i) | 3):
		return dist[1][i]
	if memo[i][mask] != -1:
		return memo[i][mask]

	res = 10**9
	for j in range(1, n+1):
		if (mask & (1 << j)) != 0 and j != i and j != 1:
			res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
	memo[i][mask] = res # storing the minimum value
	return res


ans = 10**9
for i in range(1, n+1):
	ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])

print("The cost of most efficient tour = " + str(ans))
