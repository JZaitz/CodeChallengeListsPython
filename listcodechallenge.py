#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False


#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  else:
    return False

#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
def make_pi():
  return [3,1,4]


#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  else:
    return False

#Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
  return nums[0] + nums[1] + nums[2]

#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(nums):
  new = [nums[1], nums[2], nums[0]]
  return new

#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
  if nums[0] >= nums[-1]:
    return [nums[0], nums[0], nums[0]]
  elif nums[-1] > nums[0]:
    return [nums[-1], nums[-1], nums[-1]]
  else:
    return nums

#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0

#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
  newarray = [a[1], b[1]]
  return newarray

#Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
def make_ends(nums):
  if len(nums) == 1:
    return [nums[0], nums[0]]
  elif len(nums) >= 2:
    newarray = [nums[0], nums[-1]]
    return newarray


#Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
  if nums[0] == 2 or nums[0] == 3:
    return True
  elif nums[1] == 2 or nums[1] == 3:
    return True
  else:
    return False

#When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
def cigar_party(cigars, is_weekend):
  if cigars >= 40 and cigars <= 60 and not is_weekend:
    return True
  elif cigars >= 40 and is_weekend:
    return True
  else:
    return False

#You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  if you >= 8 or date >= 8:
    return 2
  else:
    return 1


#The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
def squirrel_play(temp, is_summer):
  if temp >= 60 and temp <= 90 and not is_summer:
    return True
  elif is_summer and temp >= 60 and temp <= 100:
    return True
  else:
    return False

#You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
  if is_birthday and speed <= 65:
    return 0
  elif is_birthday and speed >= 66 and speed <= 85:
    return 1
  elif is_birthday and speed >= 86:
    return 2
  elif speed >= 61 and speed <= 80:
    return 1
  elif speed >= 81:
    return 2
  elif speed <= 60:
    return 0

#Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
def sorta_sum(a, b):
  answer = a + b
  if answer >= 10 and answer <= 19:
    return 20
  else:
    return answer

#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
def alarm_clock(day, vacation):
  if not vacation:
    if day >= 1 and day <=5:
      return "7:00"
    else:
      return "10:00"
  elif vacation:
    if day >= 1 and day <=5:
      return "10:00"
    else:
      return "off"
      
