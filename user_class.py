class User:

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        while True:
            user = f"{self.first_name} {self.last_name} \nUsername: {self.username} \nEmail: {self.email} \n{self.location}"
            print(user.title())
            break

    def greet_user(self):
        print(f"Welcome back {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

new_user = User('the knights', 'who sayy ni', 'the knights who sayy ni', 'knightswhosayni@hotmail.com', 'in the forest')
new_user.describe_user()
new_user.greet_user()

#print("\nMaking 3 login attempts...")
#new_user.increment_login_attempts()
#new_user.increment_login_attempts()
#new_user.increment_login_attempts()
#print(f"  Login attempts: {new_user.login_attempts}")


#print("Resetting login attempts...")
#new_user.reset_login_attempts()
#print(f"  Login attempts: {new_user.login_attempts}")

class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()



class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"\nPrivileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f" -{privilege}")  
        else:
            print("This user has no privileges")

greg = Admin('greg', 'hirsch', 'ghirsch', 'ghirsch@waystar.co', 'new york')
greg.describe_user()

greg_privileges = [
    'can add posts',
    'can delete posts',
    'can ban users',
]

greg.privileges.privileges = greg_privileges
greg.privileges.show_privileges()