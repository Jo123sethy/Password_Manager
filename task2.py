def main():
  key = "loadkey()"
  while True:
      print("\nPassword Manager")
      print("1. Generate Strong Password")
      print("2. Store Password")
      print("3. Retrieve Password")
      print("4. Exit")

      choice = input("Enter your choice: ")

      if choice == '1':
          length = int(input("Enter the length of the password: "))
          password = "generate random password(length)"
          print(f"Generated Password: {password}")

      elif choice == '2':
          category = input("Enter the category: ")
          website = input("Enter the website: ")
          username = input("Enter the username: ")
          password = input("Enter the password: ")
          store_password(category, website, username, password, key)
          print("Password stored successfully!")

      elif choice == '3':
          category = input("Enter the category: ")
          website = input("Enter the website: ")
          decrypted_password = retrieve_password(category, website, key)
          if decrypted_password:
              print(f"Retrieved Password: {decrypted_password}")
          else:
              print("Password not found!")

      elif choice == '4':
          print("Exiting Password Manager. Goodbye!")
          break

      else:
          print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()

