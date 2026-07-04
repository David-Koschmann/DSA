# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

def abbrev_name(name):
    name_parts = name.split()
    first_intial = name_parts[0][0].upper()
    last_initial = name_parts[1][0].upper()
    
    return f"{first_intial}.{last_initial}"