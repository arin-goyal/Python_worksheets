class String:
    def __init__(self):
        self.text = ""

    def get_string(self):
        self.text = input("Enter a string: ")

    def print_string(self):
        print(self.text.upper())

Str = String()

Str.get_string()

Str.print_string()
