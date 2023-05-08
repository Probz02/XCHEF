import time
import getpass
import subprocess
print(r"""
$$\   $$\  $$$$$$\  $$\                  $$$$$$\        $$\      $$\           $$\   $$\     $$\      $$$$$$$$\                  $$\ 
$$ |  $$ |$$  __$$\ $$ |                $$  __$$\       $$$\    $$$ |          $$ |  $$ |    \__|     \__$$  __|                 $$ |
\$$\ $$  |$$ /  \__|$$$$$$$\   $$$$$$\  $$ /  \__|      $$$$\  $$$$ |$$\   $$\ $$ |$$$$$$\   $$\         $$ | $$$$$$\   $$$$$$\  $$ |
 \$$$$  / $$ |      $$  __$$\ $$  __$$\ $$$$\           $$\$$\$$ $$ |$$ |  $$ |$$ |\_$$  _|  $$ |$$$$$$\ $$ |$$  __$$\ $$  __$$\ $$ |
 $$  $$<  $$ |      $$ |  $$ |$$$$$$$$ |$$  _|          $$ \$$$  $$ |$$ |  $$ |$$ |  $$ |    $$ |\______|$$ |$$ /  $$ |$$ /  $$ |$$ |
$$  /\$$\ $$ |  $$\ $$ |  $$ |$$   ____|$$ |            $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$\ $$ |        $$ |$$ |  $$ |$$ |  $$ |$$ |
$$ /  $$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |            $$ | \_/ $$ |\$$$$$$  |$$ |  \$$$$  |$$ |        $$ |\$$$$$$  |\$$$$$$  |$$ |
\__|  \__| \______/ \__|  \__| \_______|\__|            \__|     \__| \______/ \__|   \____/ \__|        \__| \______/  \______/ \__|
""")
input("Press enter to continue...")


# Username and password authentication
authenticated = False
while not authenticated:
    username = input("Enter your username: ")
    password = getpass.getpass(prompt='Enter your password: ')

    if username == "Corey" and password == "Admin123":
        authenticated = True
    else:
        print("Invalid username or password. Please try again.")

print("Authentication successful!")
time.sleep(2) # wait for 2 seconds

# loading the resources
print (r""" Loading resources 0% """)
time.sleep(4) # wait for 4 seconds
print (r""" Injecting SSL 31% """)
time.sleep(6) # wait for 6 seconds
print (r""" Rebooting config 81% """)
print (r"""Loading ...""")
print (r"""Loading ..""")
print (r"""Loading ...""")
print (r"""Loading ..""")
print (r"""Loading ...""")
print (r"""Complete""")

print (r"""
-------------------------------------------------------------
-                  XCHEF TOOLS                              -
-                                                           -
-     Useful Websites      1                                -
-     Ip Stresser v1       2                                -
-     Minecraft Ip grabber 3                                -
-     Discord Link         4                                -
-                                                           -
-                                                           -
-                                                           -
-                                                           -                                                        -
-               More Coming Soon                            -
-                                                           -
-                                                           -
-                                                           -
-------------------------------------------------------------
""")


# options

option = input("Pick an option: ")

if option == "1":
    # run application 1
    print("Running application 1...")
elif option == "2":
    # run application 2
   subprocess.run(["start", "ip stresser.py"], shell=True)
elif option == "3":
    # run application 3
    print("Running application 3...")
elif option == "4":
    # run application 4
    print("Running application 4...")
else:
    print("Invalid option selected.")
