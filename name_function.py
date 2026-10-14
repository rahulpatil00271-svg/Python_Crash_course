

# This is basically a seperate file for function
# This can be accesed when name_function is called
# syntax to call : from name_function import get_formatted_name



def get_formatted_name(first,middle, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title() #Title formates the name So 1st letter is always Capital