x = "Global"                 # Global

def outer():

    y = "Enclosing"          # Enclosing

    def inner():

        z = "Local"          # Local

        print(z)             # Local
        print(y)             # Enclosing
        print(x)             # Global
        print(len("Python")) # Built-in

    inner()

outer()