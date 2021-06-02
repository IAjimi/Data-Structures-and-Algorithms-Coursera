import sys

def compute_min_refills(distance, tank, stops):
	num_refills = 0
	current_refill = 0
	n = len(stops)
	stops = [0] + stops

	while current_refill <= n:
		last_refill = current_refill

		if stops[last_refill] + tank >= distance: return num_refills
		if current_refill == n: return -1 # unreachable point
		if stops[current_refill + 1] - stops[last_refill] > tank: return -1 # unreachable point

		while (current_refill < n) and (stops[current_refill + 1] - stops[last_refill] <= tank): # keep going,  if > m then refuel
			if stops[current_refill] + tank >= distance: return num_refills + 1 # reached endpoint
			current_refill += 1

		num_refills += 1

	return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
