codec = {'a': '1', 'c': '3', 'b': '2', 'e': '5', 'd': '4', 'g': '7', 'f': '6',
         'i': '9', 'h': '8', 'k': '11', 'j': '10', 'm': '13', 'l': '12',
         'o': '15', 'n': '14', 'q': '17', 'p': '16', 's': '19', 'r': '18',
         'u': '21', 't': '20', 'w': '23', 'v': '22', 'y': '25', 'x': '24', 'z': '26'}
codec = dict(sorted(codec.items(), key=lambda x: x[0]))

def num_waays(key, key_len):

    count = 0
    if key == 0:
        return 1
    elif key_len < 2 and key in codec.values():
        return 1
    else:
        if key[0] in codec.values():
            count += 1
            if key[0]+key[1] in codec.values():
                count += 1
    return count

n = input()
print(num_waays(n, len(n)))