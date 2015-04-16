# Pure-Python-Password-Manager
The goal of this project is to create a simple password manager written in Python, that has no dependencies other than those provided in the standard libraries.
Before this can be used, all the python files, must be changed to reflect the exact location of the password files. All of the locations are examples.
The encrypt-password takes a file that uses the following format.
T: The title of the credentials (e.g. github.com, gmail.com)
E: The email you registered with
U: Your username
P: Your password
This format is loose, and only the "T:" section needs to be adhered to. If you sign in through Facebook, simply say that below the "T:" tag in whatever manner you want.
Once you have the file ready, and have changed the pathname to the unencrypted file, so it points to your password file, simply run the encryp-password.py file, and it will convert your file into one that is enciphered. It will create a new file for this, and you can then delete the file you have that contains the plain passwords.
Now create a file named whatever you wish, and include in it one line of text that lists the password you want to use, when you run the password accessing script. This is a safety measure.
Once you have set all the proper file locations in the password-manager.py script, simply run it, and then, when prompted, enter the password you created in the set before this one.
Now you can search and browse through all your passwords, securely.
When you want to add more passwords, simply run the decrypt-password.py script, and open the file it creates. Now add at the bottom your new accounts, save it, and then run the encrypt-password.py file, making sure it points to the location of the file that the decrypt-password.py created. Once again, you may now delete the file containing the plain passwords, and once more continue browsing through your login credentials.
For the most security, convert the Python script into an executable file, so only through reverse engineering could they find the file names for the password files you have made.
I am not liable for any loss of your information, or the unauthorized access of your accounts.
