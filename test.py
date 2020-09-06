# from functools import cmp_to_key
# from collections import defaultdict

################################################
# Another code
# class Player:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# def comparator(one, two):
#     import ipdb; ipdb.set_trace()
#     if one[-1] == two[-1]:
#         if one[0] > two[0]:
#             return 1
#         else:
#             return -1
#     else:
#         return two[-1] - one[-1]

# n = int(input())
# data = []
# for i in range(n):
#     name, score = input().split()
#     score = int(score)
#     player = (name, score)
#     data.append(player)

# data = sorted(data, key=cmp_to_key(comparator))
# for i in data:
#     print(i[0], i[-1])
###############################################

###############################################
# Another code

# def print_formatted(number):

#     w = len(str(bin(number)).replace('0b',''))
#     for i in range(1,number+1):
#         d = str(i).rjust(w,' ')
#         b = bin(i)[2:].rjust(w,' ')
#         o = oct(i)[2:].rjust(w, ' ')
#         h = hex(i)[2:].rjust(w, ' ').upper()
#         print(d, o, h, b)

# # if __name__ == '__main__':
# n = int(input())
# print_formatted(n)
################################################

#################################################
# Another code

# def cmp_fun(a, b):
#     import ipdb; ipdb.set_trace()
#     if a[-1] > b[-1]:
#         return 1
#     elif a[-1] < b[-1]:
#         return -1
#     else:
#         return 0

# list1 = ['geeks', 'for', 'geeks']
# l = sorted(list1, key = cmp_to_key(cmp_fun))
# print('sorted list :', l)
################################################

###############################################
# Another Code
# arr = [1, 3, 9, 9, 27, 81]
# ra = 3
# d1 = defaultdict(int)
# d2 = defaultdict(int)

# count = 0
# for i  in reversed(arr):
#     print('i', i, 'i*ra', i*ra)
#     if i*ra in d2:
#         count += d2[i*ra]
#         print('count', count)
#     if i*ra in d1:
#         d2[i] += d1[i*ra]

#     d1[i] += 1

# print(count)
#################################################

#################################################
# Another Code

# codec = {'a': '1', 'c': '3', 'b': '2', 'e': '5', 'd': '4', 'g': '7', 'f': '6',
#          'i': '9', 'h': '8', 'k': '11', 'j': '10', 'm': '13', 'l': '12',
#          'o': '15', 'n': '14', 'q': '17', 'p': '16', 's': '19', 'r': '18',
#          'u': '21', 't': '20', 'w': '23', 'v': '22', 'y': '25', 'x': '24', 'z': '26'}
# codec = dict(sorted(codec.items(), key=lambda x: x[0]))

# def num_waays(key, key_len):

#     count = 0
#     if key == 0:
#         return 1
#     elif key_len < 2 and key in codec.values():
#         return 1
#     else:
#         if key[0] in codec.values():
#             count += 1
#             if key[0]+key[1] in codec.values():
#                 count += 1
#     return count

# n = input()
# print(num_waays(n, len(n)))

#################################################

#################################################
# Another Code

# Function to print the matrix
# def print_matrix(mat):
#     for i in range(len(mat)):
#         for j in range(len(mat)):
#             print(str(mat[i][j]), end=" ")
#         print()

# # Function to transpose the matrix


# def transpose_matrix(mat):
#     for i in range(len(mat)):
#         for j in range(i, len(mat)):
#             mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

# # Function to reverse the columns of the matrix


# def reverse_columns(mat):
#     for i in range(len(mat)):
#         k = len(mat) - 1
#         for j in range(k-1):
#             mat[j][i], mat[k][i] = mat[k][i], mat[j][i]
#             k = k - 1


# # Main Function
# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("The array before rotation is ")
# print_matrix(mat)

# transpose_matrix(mat)
# reverse_columns(mat)

# print("\nThe array after rotation is ")
# print_matrix(mat)

# # mat 2
# mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# print("The array before rotation is ")
# print_matrix(mat2)

# transpose_matrix(mat2)
# reverse_columns(mat2)

# print("\nThe array after rotation is ")
# print_matrix(mat2)

##################################################

# class FlightQueryViewset(viewsets.ViewSet):
#     """Allowed for all user to get query data"""
#     permission_classes = (AllowAny, )

#     def create(self, request):

#         request_date = self.request.data['request_date']
#         # request_data is the attribute we are getting from frontend for flight query
#         # it can be any thing and im asssuming here that all api takes this response
#         response_airline1 = requests.get(
#             'http://airline_1/json/', request_date).json()
#         all_responses.append(response_airline1)
#         response_airline2 = requests.get(
#             'http://airline_2/json/', request_date).json()
#         all_responses.append(response_airline2)
#         response_airline3 = requests.get(
#             'http://airline_3/json/', request_date).json()
#         all_responses.append(response_airline3)
#         response_airline4 = requests.get(
#             'http://airline_4/json/', request_date).json()
#         all_responses.append(response_airline4)
#         response_airline5 = requests.get(
#             'http://airline_5/json/', request_date).json()
#         all_responses.append(response_airline5)

#         # here i am gussing every api give an response
#         # iam assuming keys in all api responses are price, date_time and seat_avaliablity
#         context = {}
#         flight_responses = []
#         for i in all_responses:
#             context = {
#                 'price': i['price'],
#                 'date_time': i['date_time']
#                 'seat_avaliablity': i['seat_avaliablity']
#             }
#             # adding all response values so that we can easily rensed it on our page
#             flight_responses.append(context)

#         # sorting list of response dictionaries on the bases of there prices
#         final_flight_responses = list(sorted(flight_responses, key = lambda i: i['price']))

#         return response.Ok(final_flight_responses)

#################################################

#################################################
# Another Code

# A manager is an interface through which database query operations are provided to Django models. At least one Manager exists for every model in a Django application, objects is the default manager of every model that retrieves all objects in the database.

# We can use a custom Manager in a particular model by extending the base Manager class and instantiating your custom Manager in your model.

# There are two reasons you might want to customize a Manager, to add extra Manager methods, or to modify the initial queryset for the Manager returns.

# example: -
# class Employee(models.Model):
#       name = models.CharField(max_length=200)
#       active = models.BooleanField(default=True)

#       # custom manager replaces objects manger
#       all_employees = models.Manager()

#       def __str__(self):
#             return self.str(name)

# # First, define the Manager subclass.
# class EmployeeManager(models.Manager):
#     def get_queryset(self):
#         return super(EmployeeManager, self).get_queryset().filter(active=True)

# use case:-
# In this example Employee.objects.all() will return all employees in the database but with the use of model manager class  Employee.active_objects.all() will only return the ones who are in active state.
#################################################

#################################################

# def given_array(given_list, n):
#     carry = 1
#     for i in reversed(range(n)):
#         import ipdb; ipdb.set_trace()
#         print(i, given_list[i])
#         if (given_list[i] + 1) >= 10:
#             given_list[i] = given_list[i] + carry - 10
#             if i==0 and given_list[i] == 0:
#                 given_list.insert(0, 1)
#         else:
#             given_list[i] += 1
#             return given_list
#     return given_list

# print('Enter the length of Array')
# ll = int(input())
# val = [int(input()) for k in range(ll)]
# print('Your array', val)
# val = given_array(val, ll)
# print(val)

#################################################
#################################################
# Another Code

# ll = [1, 2, 2, 2, 4, 5, 7, 8, 9, 11, 12, 14, 20, 16, 18, 25, 3, 3, 30, 22, 22]
# lv = []

# n = max(ll)

# for i in range(1, n):
#     lv.append(i)

# vv = set(lv) - set(ll)

# print(lv)
# print(ll)
# print(vv)
#################################################
#################################################
# Another Code
# def pyramid(rows):
#     for i in range(rows):
#         print(' '*(rows-i-1)+'e '*(i+1))
#     for j in range(rows-1, 0, -1):
#         print(' '*(rows-j)+'e '*(j))

# pyramid(5)

# def pattern(n):

#     k = 2 * n - 2
#     vow = ['a', 'b', 'c', 'd', 'e']
#     for i in range(0, n):
#         for j in range(0 , k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0 , i + 1 ):
#             # import ipdb; ipdb.set_trace()
#             # print(j)
#             if i==j:
#                 print(vow[-1], end="")
#             # else:
#             #     print(vow[-1][:i-j], end="")

#         print("\r")

# k = n - 2
# for i in range(n , -1, -1):
#     for j in range(k , 0 , -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0 , i + 1):
#         print("* ", end="")
#     print("\r")

# pattern(5)
# def occurrence(arr, int):
#     dd = {}
#     for i in arr: # calculating repentance of element in array
#         if i in dd.keys():
#             dd[i] += 1
#         else:
#             dd[i] = 1

#     if dd[int]: # matching int as key in dictionary
#         print(dd[int])
#     else:
#         print("Integer not present in array")

# occurrence([2,3,4,3,2,1], 3)

# for row in range(1, 6):

#     for column in range(0, row+1):

#         print(" ", end="")

#     for column2 in range(row, 5):

#         print(chr(column2+64), end="")

#     for column3 in range(5, row-1, -1):

#         print(chr(column3+64), end="")

#     print()

#################################################
# Another Code

# ---------e---------
# -------d-e-d-------
# -----c-d-e-d-c-----
# ---b-c-d-e-d-c-b---
# -a-b-c-d-e-d-c-b-a-
# ---b-c-d-e-d-c-b---
# -----c-d-e-d-c-----
# -------d-e-d-------
# ---------e---------


def pyramid(n):

    for row in range(1, n+1):

        for column in range(0, row+1):

            print(" ", end="")

        for column2 in range(row, n):

            print(chr(column2+64), end="")

        for column3 in range(n, row-1, -1):

            print(chr(column3+64), end="")

        print()

pyramid(5)



# def test(n):
#     count = 1
#     nos_space = 1
#     start = 0

#     for i in range(1, n*2):
#         spc = n - nos_space

#         for _ in range(spc, 1, -1):
#             print('', end='')

#         if i < n:
#             start = i
#             nos_space -=1

#         else:
#             start = n*2-i
#             nos_space -=1

#         for j in range(0, count):
#             print(start, end='')

#             if j < count//2:
#                 start -=1
#             else:
#                 start +=1
#         if i<n:
#             count = count + 2
#         else:
#             count = count - 2

#         print()

# test(5)
        




#################################################
