from setuptools import find_namespace_packages


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return # This empty return ends the function right here, instead of giving errors, in case of an empty string input
    first_name = f_name.title()
    last_name = l_name.title()

    #print(f"{first_name} {last_name}")

    # Instead of printing it out, like in line 8, we will return the output

    return f"{first_name} {last_name}"

print(format_name("sid", "prasad"))

# or

actor_name = format_name("", "hood") # this line of code should not run because of line 5
print(actor_name)