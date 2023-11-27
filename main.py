def generate_queries(option, search_term):
    queries = []
    if option == "1":
        queries = [
            f'intext:"{search_term}" (intitle:"Patent" OR intitle:"Patent Application" OR intitle:"Invention")',
            f'intext:"{search_term}" (intitle:"Cybersecurity" OR intitle:"Security Threat" OR intitle:"Hack")',
            f'intext:"{search_term}" (intitle:"Research" OR intitle:"Publication" OR intitle:"Study")',
            f'intext:"{search_term}" (intitle:"Confidential Agreement" OR intitle:"Non-disclosure Contract" OR intitle:"Confidential Accord")'
        ]
    elif option == "2":
        queries = [
            f'intext:"{search_term}" (intitle:"Contact List" OR intitle:"Directory" OR intitle:"Phonebook")',
            f'intext:"{search_term}" (intitle:"Customer Information" OR intitle:"Client List" OR intitle:"Personal Contacts")'
        ]
    elif option == "3":
        queries = [
            f'intext:"{search_term}" (intitle:"Emails" OR intitle:"Email Database" OR intitle:"Email Addresses")',
            f'intext:"{search_term}" (intitle:"Inbox" OR intitle:"Sent Items" OR intitle:"Email Correspondence")'
        ]
    elif option == "4":
        queries = [
            f'intext:"{search_term}" (intitle:"Social Media Profiles" OR intitle:"Social Network" OR intitle:"User Profile")',
            f'intext:"{search_term}" (intitle:"Timeline" OR intitle:"Posts" OR intitle:"Connections")'
        ]

    return queries

if __name__ == "__main__":
    print("Select an option:")
    print("1. Name")
    print("2. Phone Number")
    print("3. Email")
    print("4. Social Media Profile")

    selected_option = input("Enter your choice (e.g., 1): ")

    if selected_option in ["1", "2", "3", "4"]:
        search_term = input("Enter the search term: ")
        generated_queries = generate_queries(selected_option, search_term)
        if generated_queries:
            print("Generated Google Dork queries:")
            for query in generated_queries:
                print(query)
        else:
            print("No queries found for this option.")
    else:
        print("Invalid option")
