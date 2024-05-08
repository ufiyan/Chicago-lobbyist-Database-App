#
# Name: Sufiyan Ahmed Syed
# Author: Kidani Ellen
# Project2: The Chicago Lobbyist Database
#
import sqlite3
import objecttier

def display_general_statistics(dbConn):

    num_lobbyists = objecttier.num_lobbyists(dbConn)
    num_employers = objecttier.num_employers(dbConn)
    num_clients = objecttier.num_clients(dbConn)

    print("General Statistics:")
    print(f"  Number of Lobbyists: {num_lobbyists:,}")
    print(f"  Number of Employers: {num_employers:,}")
    print(f"  Number of Clients: {num_clients:,}\n")

#Allows the user to search for lobbyists by entering a name.
#The search can be based on either the first or last name and supports wildcards (_ for a single character and % for multiple characters).
#The user is prompted to enter a lobbyist name or partial name, with wildcard characters if desired.
#The application searches the database for lobbyists matching the provided name criteria.
#It Displays the list of matching lobbyists, including their ID, name, and contact phone number.
# If more than 100 lobbyists are found, it prompts the user to narrow down the search criteria.
def lookup_lobbyists_by_name(dbConn, name):
    lobbyists = objecttier.get_lobbyists(dbConn, name);
    return lobbyists

#The purpose of this command is to fetches and displays detailed information for a specific lobbyist, identified by their ID.
# The user is prompted to enter the ID of the lobbyist whose details they wish to view.
# Retrieves detailed information for the specified lobbyist from the database.
# Displays detailed information about the lobbyist, including ID, full name, address, email, phone, fax, years registered, employers, and total compensation.
def lookup_lobbyist_details_by_id(dbConn, lobbyist_id):
    details = objecttier.get_lobbyist_details(dbConn, lobbyist_id)
    if not details:
        print("\nNo lobbyist with that ID was found.")
        return None
    else:
        years_registered = ", ".join(map(str, details.Years_Registered))

        # Correcting the 'Total Compensation' formatting to include commas
        total_compensation_formatted = f"${details.Total_Compensation:,.2f}"

        # Adjusted to match the corrected code's address format
        address = f"{details.Address_1} {details.Address_2} , {details.City} , {details.State_Initial} {details.Zip_Code}".strip()
        address += " United States"  # Adding "United States" to the address

        print(f"{details.Lobbyist_ID} :")
        full_name = f"{details.Salutation} {details.First_Name} {details.Middle_Initial} {details.Last_Name} {details.Suffix}".strip()
        print(f"  Full Name: {full_name}")
        print(f"  Address: {address}")
        print(f"  Email: {details.Email}")
        print(f"  Phone: {details.Phone}")


        print(f"  Fax: {details.Fax}")
        print(f"  Years Registered: {years_registered},")

        if details.Employers:
            employers = ", ".join(details.Employers)
        else:
            employers = "No employers listed"
        print(f"  Employers: {employers},")
        print(f"  Total Compensation: {total_compensation_formatted}")

#The purpose of the command 4 is to registers an existing lobbyist for a new year, indicating their continued activity.
# The user provides the year and the lobbyist ID for registration.
# Adds a new entry to the database, associating the lobbyist with the specified year.
# Confirmation message indicating successful registration or an error message if the lobbyist ID does not exist.
def register_lobbyist_for_new_year(dbConn):
    # Prompt user for the year and lobbyist ID
    year = input("Enter year: ")
    lobbyist_id = input("Enter the lobbyist ID: ")

    # Call the function from objecttier to add a new year for the lobbyist
    result = objecttier.add_lobbyist_year(dbConn, lobbyist_id, year)

    # Check the result and print the appropriate message
    if result == 1:
        print("\nLobbyist successfully registered.")
    else:
        print("\nNo lobbyist with that ID was found.")

def set_lobbyist_salutation(dbConn, lobbyist_id, salutation):
    # This function calls the objecttier function to set the salutation for a lobbyist
    result = objecttier.set_salutation(dbConn, lobbyist_id, salutation)
    return result

# The purpose of this command is to identifies and displays the top N lobbyists based on their total compensation for a specified year.
# The user is prompted to enter the number N (to indicate how many top lobbyists to display) and the year of interest.
# The application retrieves and ranks lobbyists by their total compensation for the given year, then selects the top N lobbyists from this ranking.
# Lists the top N lobbyists for the specified year, showing each lobbyist's name, phone number, total compensation, and a comma-separated list of their clients, ordered by the client name.
def COMMAND3(dbConn):
  print()
  try:
      num_lobbyists = int(input("Enter the value of N: "))
  except ValueError:
      print("Invalid input. Please enter a positive integer for N...\n")
  else:
      if num_lobbyists > 0:
          input_year = input("Enter the year: \n").strip()

          top_lobbyists = objecttier.get_top_N_lobbyists(dbConn, num_lobbyists, input_year)

          if top_lobbyists:
              index = 1
              while index <= len(top_lobbyists):
                  lobbyist = top_lobbyists[index - 1]
                  print(f"{index} . {lobbyist.First_Name} {lobbyist.Last_Name}")
                  print(f"  Phone: {lobbyist.Phone}")
                  print(f"  Total Compensation: ${lobbyist.Total_Compensation:,.2f}")
                  client_list = ', '.join(lobbyist.Clients)
                  print(f"  Clients: {client_list}, \n")
                  index += 1
      else:
          print("Please enter a positive value for N...\n")
def main():
    dbConn = sqlite3.connect('Chicago_Lobbyists.db')
    print("** Welcome to the Chicago Lobbyist Database Application **\n")
    display_general_statistics(dbConn)
    print("Please enter a command (1-5, x to exit): ")
    command = input()
    while command != "x":
        if command == "1":
            name = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
            lobbyists = lookup_lobbyists_by_name(dbConn, name)
            print(f"\nNumber of lobbyists found: {len(lobbyists)}")
            if len(lobbyists) > 100:
                print("There are too many lobbyists to display, please narrow your search and try again...")
            else:
                for lobbyist in lobbyists:
                    print(f"{lobbyist.Lobbyist_ID} : {lobbyist.First_Name} {lobbyist.Last_Name} Phone: {lobbyist.Phone}")
        elif command == "2":
            lobbyist_id = input("Enter Lobbyist ID: \n")
            lookup_lobbyist_details_by_id(dbConn, lobbyist_id)
        elif command == "3":
            COMMAND3(dbConn)
        elif command == "4":
            register_lobbyist_for_new_year(dbConn)
        #Purpose: The purpose of this functions is to Updates or sets the salutation for a specific lobbyist in the database.
        # The user is prompted to enter the lobbyist ID and the new salutation to be set.
        # Updates the salutation field of the specified lobbyist in the database.
        # Confirmation message indicating the successful update of the lobbyist's salutation or an error message if the lobbyist ID does not exist.
        elif command == "5":
            lobbyist_id = input("Enter the lobbyist ID: ").strip()
            salutation = input("Enter the salutation: ").strip()
            result = set_lobbyist_salutation(dbConn, lobbyist_id, salutation)
            if result:
                print("\nSalutation successfully set.")
            else:
                print("No lobbyist with that ID was found.")
        else:
            print("**Error: unknown command, try again...")

        # Prompt for the next command
        print("Please enter a command (1-5, x to exit): ")
        command = input().strip()
    dbConn.close()

if __name__ == '__main__':
    main()