# Given a list of users, create a function to find the user with a user_id of 4.


users = [
    {"user_id": 1, "first_name": "Margaret", "last_name": "Chicken"},
    {"user_id": 2, "first_name": "Bill", "last_name": "Gates"},
    {"user_id": 3, "first_name": "Steve", "last_name": "Jobs"},
    {"user_id": 4, "first_name": "Guido", "last_name": "van Rossum"},
    {"user_id": 5, "first_name": "Brendan", "last_name": "Eich"},
]


# ### Task:
# Write a solution to the above task and then submit it as a new github repo.

def find_user(list, user_id):
    for user in users:
        if user["user_id"] == user_id:
            return user
    return "no user found"


print(find_user(users, 4))
print(find_user(users, 3)) #test
print(find_user(users, 6)) #test  



# def find_chicken_by_name( list, chicken_name ):
#   found_chicken = None
#   for chicken in list:
#     if chicken["name"] == chicken_name:
#       found_chicken = chicken

#   return found_chicken
