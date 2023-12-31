# Section 10.12 Self Check snippets

# Exercise 2
from collections import namedtuple

# Create a namedtuple type called 'Time'
Time = namedtuple('Time', ['hour', 'minute', 'second'])

# Create an instance of Time
t = Time(13, 30, 45)

# Access its members
print(t.hour, t.minute, t.second)  # Outputs: 13 30 45

# Display its string representation
print(t)  # Outputs: Time(hour=13, minute=30, second=45)

# This is a great example of how Python’s namedtuple can be used to create a custom data structure. 
# In this case, a Time object is created that has hour, minute, and second attributes. 

        


##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
