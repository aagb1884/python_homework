# def test_return_10(self):
#     return_10_result = return_10 ()
#     self.assertEqual( 10, return_10_result)

# def return_10():
#     return 10

# test2

# def test_add(self):
#       add_result = add( 1, 2 )
#       self.assertEqual( 3, add_result )

# def add(int1, int2):
#     return (int1 + int2) #updated

# def test_subtract(self):
#       subtract_result = subtract( 10, 5 )
#       self.assertEqual( 5, subtract_result ) #assert bracketed values are same

# def subtract(int1, int2):
#         return (int1 - int2) #updated

# def test_multiply(self):
#       multiply_result = multiply( 4, 2 )
#       self.assertEqual( 8, multiply_result )

# def multiply (int1, int2):
#       return (int1 * int2) #updated

# def test_divide(self):
#       divide_result = divide( 10, 2 )
#       self.assertEqual( 5, divide_result )
 
# // = floor divide that will round down if doesn't divide easily

# def divide (int1, int2):
#     return (int1 / int2)

# def test_length_of_string(self):
#       test_string = "A string of length 21"
#       string_length = length_of_string( test_string )
#       self.assertEqual( 21, string_length )  

# use len here len = length, as there are parameters can't just assert 21

# def length_of_string (length):
#     return (measurement)
# measurement = 21

# def test_join_string(self):
#       string_1 = "Mary had a little lamb, "
#       string_2 = "its fleece was white as snow"
#       joined_string = join_string( string_1, string_2 )
#       self.assertEqual( "Mary had a little lamb, its fleece was white as snow", joined_string )

# def join_string( string_1, string_2):
#       return f"{string_1}{string_2}" #updated    
# 
# can work as return string_1 + string_2 - no need to add parentheses 

# def test_add_string_as_number(self):
#       add_result = add_string_as_number( "1", "2" )
#       self.assertEqual( 3, add_result )

# def add_string_as_number(str_1, str_2):
#       return (int(str_1) + int(str_2))

# no need for brackets as return = keyword

# def test_number_to_full_name__month_1(self):
#       result = number_to_full_month_name( 1 )
#       self.assertEqual( "January", result )

number_month = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
}

# def number_to_full_month_name( number ):
#       return (number_month[1])

# def test_number_to_full_name__month_3(self):
#       result = number_to_full_month_name( 3 )
#       self.assertEqual( "March", result )

# def number_to_full_month_name( number ):
#       return (number_month[3])

# def number_to_full_month_name( number ):
#       return (number_month[9])

# def test_number_to_short_month_name__month_1(self):
#       first_month_string = number_to_short_month_name( 1 )
#       self.assertEqual( "Jan", first_month_string )

# def number_to_short_month_name(short_month_name):
#       short_month_name = (number_month[1])[0:3]
#       return short_month_name

# def number_to_short_month_name(short_month_name):
#       short_month_name = (number_month[4])[0:3]
#       return short_month_name

# def number_to_short_month_name(short_month_name):
#       short_month_name = (number_month[10])[0:3]
#       return short_month_name

def reverse_the_string(str):
#     return """.join(list(reversed)(str))
      string_reversed = ''
      index = len(str)
      while index > 0:
            string_reversed += str [ index -1 ]
            index = index -1
      return string_reversed
# while loop makes it greater than 0, string_reversed - an open variable -
# whatever value is add 1 to string while moving back through index
# strings can be like lists hence square bracket
# index = no. figures in string
# so 

# def reverse_string(string):
#     new_string = ""
#     for char in string:
#         new_string = char + new_string
#     return new_string

# new string is open, for loop looks at each characters
# 1st iteration  new_string = S + blank new_string = S
# 2nd iteration c + new_string = cS
# and so on

def fahrenheit_to_celsius(fahrenheit):
      celsius = (fahrenheit - 32) * (5.0/9.0)
      return round(celsius, 2)
