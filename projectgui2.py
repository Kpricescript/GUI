from tkinter import *
from tkinter import messagebox
import random


FONT = ("Courier", 10, "bold")


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)


    password_input.delete(0,END)
    password_input.insert(0,str(password))


def add():
    keys = ["website", "username", "password"]

    if website_input.get() == "" or website_input.get() == "" or password_input.get() == "":
        messagebox.showinfo(title="Listen Up", message="no empty fields allowed")

    else:

        value_entry = [website_input.get(), username_input.get(), password_input.get()]
        entry_dict = {key: value for (key, value) in zip(keys, value_entry)}

        if messagebox.askyesno(title="please Confirm", message=f"{entry_dict}\n it this okay?"):
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

            with open("data.txt", "a") as data_file:
                data_file.write(f"{str(entry_dict)},\n")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# the canvas
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)

# email/username label
username = Label(text="Email/Username: ", font=FONT)
username.grid(row=2, column=0)

# password: label
password = Label(text="Password: ", font=FONT)
password.grid(row=3, column=0)

# website_input box
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

# username_input box
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)

# password_input box
#password_input = Entry(width=20,show="*")
password_input = Entry(width=20)
password_input.grid(row=3, column=1)

# generate password button
gen_pass = Button(text="Generate password", command=generate_password)
gen_pass.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", command=add)
add_button.grid(row=4, column=2)

window.mainloop()

class Password():

    def __init__(self): 
    # List of lower-case elements for password
        self.lower_case_lellers_list = [
            'a','b','c','d','e','f',
            'g','h','i','j','k','l',
            'm','n','o','p','q','r',
            's','t','u','v','w','x',
            'y','z']
        # List of upper-case elements for password
        self.upper_case_letter_list = [
            'A','B','C','D','E','F',
            'G','H','I','J','K','L',
            'M','N','O','P','Q','R',
            'S','T','U','V','W','X',
            'Y','Z']
        # List of number elements for password
        self.numbers_list = ['0','1','2','3','4','5','6','7','8','9']

        # List of symbol elements for password: Excludes quotes and slashes
        self.symbols_list = [
            '~','`','!','@','#','$',
            '%','^','&','*','(',')',
            '_','-','+','=','{','}',
            '[',']','|',':',';','<',
            '>','.','?']

        # Combined list of elemnts for remaining characters after specified elements are added
        self.remaining_chars = list(
                self.lower_case_lellers_list +
                self.upper_case_letter_list +
                self.numbers_list +
                self.symbols_list)

        self.get_length = 8
        self.get_lower = 0
        self.get_upper = 0
        self.get_nums = 0
        self.get_symbols = 0
        self.passSpecs = {}
        self.password_elements = []

        # Request user input for definition of password
    @classmethod
    def generate_user_input(self):
            self.get_length = abs(int(input("Please enter the minimum length for your password?: ")))
            self.get_lower = abs(int(input("Please enter the minimum number of lower-case letters. Enter '0' if you do not wish to include this element: ")))
            self.get_upper = abs(int(input("Please enter the minimum number of upper-case letters: Enter '0' if you do not wish to include this element: ")))
            self.get_nums = abs(int(input("Please enter the minimum number of numbers?: Enter '0' if you do not wish to include this element: ")))
            self.get_symbols = abs(int(input("Please enter the minimum number of special symbols?: Enter '0' if you do not wish to include this element: ")))

            passSpecs = {'length': self.get_length, 'lower':self.get_lower, 'upper':self.get_upper, 'numbers':self.get_nums, 'symbols':self.get_symbols}

            return passSpecs


        # Takes the output of the previous function as an argument and creates the password


#Define object for Password class
characters = Password()


#Edit: Move passGen outside class to reduce errors
#should pass the dictionary to the function will generate a password
def passGen(passSpecs):
            import random
            characters.password_elements = []
            print("")
       
            
            # Fulfill the user required characters first 
            for i in range (passSpecs['lower']):
                characters.password_elements.append(random.choice(characters.lower_case_lellers_list))
            for i in range (passSpecs['upper']):
                characters.password_elements.append(random.choice(characters.upper_case_letter_list))
            for i in range (passSpecs['numbers']):
                characters.password_elements.append(random.choice(characters.numbers_list))
            for i in range (passSpecs['symbols']):
                characters.password_elements.append(random.choice(characters.symbols_list))

            # Full list of characters to fill in based on the user requirements if not over max
            while len(characters.password_elements) < (passSpecs['length']):
                    characters.password_elements.append(random.choice(characters.remaining_chars))          
                
            random.shuffle(characters.password_elements)
            password = "".join(characters.password_elements)
            
  
            return password
    



#Since passGen was removed from class, we'll call the normal function
print(passGen(Password.generate_user_input()))
