# import os for environment varialbles and to add environment variables use the command export 
#ex export pass=subbu
import os
name = os.getenv("name")
print(name)

password = os.getenv("password")

print(password)