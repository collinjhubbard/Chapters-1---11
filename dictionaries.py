user_struct = {
    'uuid':'hfkjshdkjsdh',
    'userid':'1',
    'username': 'Kali',
    'user_password':'748ru9hf79h7304hf73fhg9324',
    'user_session':'blahblah'
}

#admin_userid = user_struct['userid']
#print(f"This user's id is {admin_userid}")

user_struct['location'] = 'EST'
user_struct['ip_address'] = '192.168.0.0'

print(user_struct)

alien = {'color':'green', 'x_position':0, 'y_position':25,'speed':'medium'}
print(f"Original position: {alien['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position of the alien
alien['x_position'] = alien['x_position'] + x_increment

print(f"The new position: {alien['x_position']}")