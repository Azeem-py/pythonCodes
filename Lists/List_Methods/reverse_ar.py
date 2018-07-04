#added by @Azharoo
#Python 3

"""
The reverse() ���� ����� ����� �����.
The reverse() �� ���� �� �����.
The reverse() �� ���� �� ����. ���� ��� ��� ������� ������ �������.
"""

#���� 1 : Reverse a List

# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# List Reverse
os.reverse()

# updated list
print('Updated List:', os)



#Example 2: Reverse a List Using Slicing Operator

# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# Reversing a list	
#Syntax: reversed_list = os[start:stop:step] 
reversed_list = os[::-1]

# updated list
print('Updated List:', reversed_list)



#Example 3: Accessing Individual Elements in Reversed Order

# Operating System List
os = ['Windows', 'macOS', 'Linux']

# ����� ������� ���� �����
for o in reversed(os):
    print(o)



# ���� 4 : (��� ������� ������ ����� )

def my_f(list):
  list1 = list.reverse() 
  return list1

list =[10,20,40]

print(my_f(list)) ## ������ ��� None 



def my_f(list):
  list1 = list.reverse() 
  return list

list =[10,20,40]

print(my_f(list))## [40, 20, 10]

"""
����� �������� �������

������

�� ����� ������

reverse()
�� ���� �������� ��� ������� ��� ������ ������ ������� �������
 
��� �� ������� ������ ��� ������� ���� ��� ����� ������� ��� ��
 
��� ������� �� ������ ������

��� ����� �� ����� ������ ����� ���� ������ ���� �������

���� ����� ������ ������

����� �� ����� ������ � �� ����� ������ �� ������� ����� � ����� ������
"""
