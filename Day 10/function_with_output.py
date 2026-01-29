def format_name(first_name, last_name):
    """ Take a first and last name and format it
    to return the title case version of the name. """
    first_name = first_name.title()
    last_name = last_name.title()

    return f"{first_name} {last_name}"


print(format_name("JOHNn", "Doe"))

