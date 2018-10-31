def main():
    correct_password = 'password1234'
    attempts = 0
    try:
        while attempts <= 3:
            user_password = str(input("Please enter your password: "))
            if user_password == correct_password:
                print('Authentication Successful!')
                break
            else:
                attempts += 1
                print('Password incorrect!')
    except ValueError:
        print("String only")
    except KeyboardInterrupt:
        print("Don't press CTRL+C")
    except:
        print("Something bad happened!")

if __name__ == "__main__":
    main()
        

    

