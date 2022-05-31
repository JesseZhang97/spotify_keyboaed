def http_error(status):
    match status:
        case 400:
            return print("Bad request")
        case 404:
            return print("Not found")
        case 418:
            return "I'm a teapot"

        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return "Something's wrong with the internet"


def my_function():
    print("Hello from a function")


my_function()
http_error(400)
