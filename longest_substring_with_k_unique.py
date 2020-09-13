import re
CHAR_RANGE = 128


def longestSubstr(str, k):

	end = begin = 0

	window = set()
	freq = [0] * CHAR_RANGE
	low = high = 0

	while high < len(str):

		window.add(str[high])
		freq[ord(str[high])] = freq[ord(str[high])] + 1

		while len(window) > k:
			freq[ord(str[low])] = freq[ord(str[low])] - 1
			if freq[ord(str[low])] == 0:
				window.remove(str[low])

			low = low + 1

		if end - begin < high - low:
			end = high
			begin = low

		high = high + 1

	return str[begin:end + 1]


if __name__ == '__main__':
    str = "3aabacbebebe"
    k = int(str[0])
    str_1 = re.sub("\d", "", str)
    print(longestSubstr(str, k))
