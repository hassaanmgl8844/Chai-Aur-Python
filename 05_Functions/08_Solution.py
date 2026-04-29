# **Kwargs in Python Done
def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="Billu",power="Blue",enemy="Jutt")