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


#The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
def love6(a, b):
  if a + b == 6:
    return True
  elif a - b == 6:
    return True
  elif b - a == 6:
    return True
  elif a == 6 or b == 6:
    return True
  else:
    return False


#Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10
def in1to10(n, outside_mode):
  if not outside_mode:
    if n >= 1 and n <= 10:
      return True
    else:
      return False
  elif outside_mode:
    if n <= 1 or n >= 10:
      return True
    else:
      return False

#Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
def near_ten(num):
  if num % 10 <= 2:
    return True
  elif num % 10 >= 8 and num % 10 <= 10:
    return True
  else:
    return False

#Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
  if a == b:
    return c
  elif a == c:
    return b
  elif b == c:
    return a
  elif a == b and b == c and a == c:
    return 0
  else:
    return a + b + c

#Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c == 13:
    return a + b
  else:
    return a + b + c


#Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

def no_teen_sum(a, b, c):
  fix_teen(a)
  sum = fix_teen(a) + fix_teen(b) + fix_teen(c)
  return sum



def fix_teen(n):
  if n == 13 or n == 14 or n == 17 or n ==18 or n == 19:
    n = 0
  else:
    n = n
  return n


#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().
def round_sum(a, b, c):
  sum = round10(a) + round10(b) + round10(c)
  return sum



def round10(n):
  if n % 10 < 5:
    n = n - (n % 10)
  elif n % 10 >= 5:
    x = 10 - (n % 10)
    n = n + x
  return n


#Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close_far(a, b, c):
  if (abs(a - b) <= 1 and abs(a - c) >= 2) or (abs(a - c) <= 1 and abs(a - b) >= 2):
    return True
  else:
    return False

"""RUBY TRANSLATION

def close_far(a,b,c)
  if (a-b).abs <= 1 && (a-c).abs >= 2 || (a-c).abs <= 1 && (a-b).abs >= 2
    return True
  else
    return False
  end
end


"""

#We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.
def make_bricks(small, big, goal):
  if big*5 + small == goal:
    return True
  elif big*5 == goal:
    return True
  elif small == goal:
    return True
  elif (big-1) * 5 + small == goal:
    return True
  elif (big-1) *5 + small > goal:
    while big >= 0:
      big = big -1
      if big*5 + small == goal:
        return True
      elif big == 0:
        break
  elif big*5 + small == goal:
    return True
  elif big*5 + small > goal:
    while small > 0:
      small = small -1
      if big*5 + small == goal:
        return True
      elif small == 0:
        break
  else:
    return False


#Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
  if a != b and b != c and a != c:
    sum = a + b + c
    return sum
  elif a == b and b != c and a != c:
    sum = c
    return sum
  elif b == c and a != b and a != c:
    sum = a
    return sum
  elif a == b and b == c and a == c:
    return 0
  elif a == c and b != a and b != c:
    return b

#Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
  newstr = ""
  for c in str:
    newstr = newstr + c*2
  return newstr

 """RUBY TRANSLATION
def double_char(str)
  newstr = ""
  str.each_char do |c|
    newstr = newstr + c * 2
  end
  newstr

end


 """


#Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
  counter = 0
  for i in range(0,len(str)-1):
    if str[i] == "h" and str[i+1] == "i":
      counter = counter + 1
    elif str[i:i+2] == "hi":
      counter = counter + 1
  return counter


 """
 #RUBY TRANSLATION
def count_hi(str)
  counter = 0
  for i in 0..str.length -2
    if str[i] == "h" && str[i+1] == "i"
      counter += 1
    elsif str[i..i+1] == "hi"
      counter += 1
    end
  end
  counter

end
"""

 #Return True if the string "cat" and "dog" appear the same number of times in the given string.
 def cat_dog(str):
  ccount = 0
  dcount = 0
  for i in range(0, len(str) - 2):
    if str[i:i+3] == "cat":
      ccount = ccount + 1
    elif str[i:i+3] == "dog":
      dcount = dcount + 1
  if ccount == dcount:
    return True
  elif ccount != dcount:
    return False

"""RUBY TRANSLATION
def cat_dog(str)
  ccount = 0
  dcount = 0
  for i in 0..str.length-3
    if str[i..i+2] == "cat"
      ccount += 1
    elsif str[i:i+2] == "dog"
      dcount += 1
    end
    if ccount == dcount
      return True
    elsif ccount != dcount
      return False
    end
  end

end

"""

#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
  counter = 0
  for i in range(0, len(str) - 3):
    if str[i:i+2] == "co" and str[i+3] == "e":
      counter = counter + 1
    elif str[i] == "c" and str[i+1] == "o" and str[i+3] == "e":
      counter = counter + 1
  return counter

  """RUBY TRANSLATION
def count_code(str)
  counter = 0
  for i in 0..str.length-4
    if str[i..i+1] == "co" && str[i+3] == "e"
      counter += 1
    elsif str[i] == "c" && str[i+1] == "o" && str[i+3] == "e"
      counter += 1
    end
  return counter
  end


end


  """


#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
  blength = len(b)
  alength = len(a)
  if a[(alength-blength):].lower() == b.lower():
    return True
  elif b[(blength-alength):].lower() == a.lower():
    return True
  else:
    return False

"""RUBY TRANSLATION
def end_other(a,b)
  blength = a.length
  alength = b.length
  if a[(alength-blength)..alength-1].downcase == b.downcase
    return True
  elsif b[(blength-alength)..blength-1].downcase == a.downcase
    return True
  else
    return False
  end
end
"""

#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
def xyz_there(str):
  counter = 0
  if len(str) <= 2:
    return False
  else:
    for i in range(0,len(str)-2):
      if str[i-1] != "." and str[i:i+3] == "xyz" or str[i:] == "xyz" and str[i-1] != ".":
        counter += 1
        return True
  if counter == 0:
    return False


#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
  counter = 0
  for x in nums:
    if x % 2 == 0:
      counter += 1
  return counter

"""RUBY TRANSLATION
def count_evens(nums)
  counter = 0
  nums.each do |x|
    if x % 2 == 0
      counter += 1
    end
  end
  return counter
end
"""

#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
  nums.sort()
  answer = nums[-1] - nums[0]
  return answer

 """Ruby
 def bif_diff(nums)
   nums.sort
   answer = nums[-1] - nums[0]
   return answer
 end
 """

 #Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
def centered_average(nums):
  nums.sort()
  newnums = nums[1:-1]
  summ = sum(newnums)
  answer = summ/len(newnums)
  return answer

 """Ruby
def centered_average(nums)
  nums.sort
  newnums = nums[1:-2]
  summ = newnums.reduce(:+)
  answer = summ/newnums.length
  return answer
end

 """
