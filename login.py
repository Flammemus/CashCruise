def login(db):
    while True:
        print("\nChoose one of the options below:\n")
        print("1. Create new account")
        print("2. Log in to existing account")
        print("3. Display all accounts")
        print("4. Exit\n")

        action = input("(1/2/3/4): ")
        
        if action == "1":
            try:
                while True:
                    accountName = input("Account name: ")
                    doc_ref = db.collection("Accounts").document(accountName)

                    if doc_ref.get().exists:
                        print("Account name already exists. Please choose another one.")
                    else:
                        break

                accountPassword = input("Password (Don't choose usual password, I have no security): ")
                new_doc_ref = db.collection("Accounts").document(accountName).set({
                    "Password": accountPassword,
                    "Balance": 0
                })

                print("Account created successfully")
                return db.collection("Accounts").document(accountName), accountName
            except Exception as e:
                print(f"Error creating account: {e}")
                return None, None

        elif action == "2":
            accountName = input("Account name: ")
            doc_ref = db.collection("Accounts").document(accountName)

            if not doc_ref.get().exists:
                print("\nAccount not found")
                return None, None

            storedPassword = doc_ref.get().to_dict().get("Password")
            enteredPassword = input("Enter Password: ")

            if enteredPassword == storedPassword:
                print("Login successful")
                return doc_ref, accountName
            else:
                print("Incorrect password.")
                return None, None
            
        elif action == "3":
            accountsRef = db.collection("Accounts")
            docs = accountsRef.stream()

            print()
            for doc in docs:
                print(f"- {doc.id}")
            
        elif action == "4":
            print("Exiting...")
            return None, None
        
        elif action == "5":
            doc_ref = db.collection("Accounts").document("Test")
            return doc_ref, "Test"

        else:
            print("Invalid option. Please try again.")
