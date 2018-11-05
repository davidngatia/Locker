class Password: 
 username = "macharia"
 password = "2000"
 print("welcome to my password programm")
 print()
 usernameGuess =input("Please enter your username: ")
 passwordGuess =input("PLease enter your password: ")

 if username == usernameGuess and password == passwordGuess:
     print("Login Successful")
 else:
     print("oops! try again")