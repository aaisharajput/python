#24.WAP to calculate number of days between two dates.
from datetime import date 
 
date_1 = date(2023, 2, 4)  
date_2 = date(2024, 2, 4)  
print("1st Date: ",date_1)
print("2nd Date: ",date_2)
print ("Number of Days between the given Dates are: ", (date_2 - date_1).days, "days")