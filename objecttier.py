#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
        self._Lobbyist_ID = Lobbyist_ID
        self._First_Name = First_Name
        self._Last_Name = Last_Name
        self._Phone = Phone

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
    def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2,
                 City, State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers,
                 Total_Compensation):
        self._Lobbyist_ID = Lobbyist_ID
        self._Salutation = Salutation
        self._First_Name = First_Name
        self._Middle_Initial = Middle_Initial
        self._Last_Name = Last_Name
        self._Suffix = Suffix
        self._Address_1 = Address_1
        self._Address_2 = Address_2
        self._City = City
        self._State_Initial = State_Initial
        self._Zip_Code = Zip_Code
        self._Country = Country
        self._Email = Email
        self._Phone = Phone
        self._Fax = Fax
        self._Years_Registered = Years_Registered
        self._Employers = Employers
        self._Total_Compensation = Total_Compensation

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def Salutation(self):
        return self._Salutation

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Middle_Initial(self):
        return self._Middle_Initial

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Suffix(self):
        return self._Suffix

    @property
    def Address_1(self):
        return self._Address_1

    @property
    def Address_2(self):
        return self._Address_2

    @property
    def City(self):
        return self._City

    @property
    def State_Initial(self):
        return self._State_Initial

    @property
    def Zip_Code(self):
        return self._Zip_Code

    @property
    def Country(self):
        return self._Country

    @property
    def Email(self):
        return self._Email

    @property
    def Phone(self):
        return self._Phone

    @property
    def Fax(self):
        return self._Fax

    @property
    def Years_Registered(self):
        return self._Years_Registered

    @property
    def Employers(self):
        return self._Employers

    @property
    def Total_Compensation(self):
        return self._Total_Compensation

##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
        self._Lobbyist_ID = Lobbyist_ID
        self._First_Name = First_Name
        self._Last_Name = Last_Name
        self._Phone = Phone
        self._Total_Compensation = Total_Compensation
        self._Clients = Clients

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone

    @property
    def Total_Compensation(self):
        return self._Total_Compensation

    @property
    def Clients(self):
        return self._Clients

##################################################################
#
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   try:
      result = datatier.select_one_row(dbConn, "SELECT COUNT(*) FROM LobbyistInfo")
      return result[0] if result else 0
   except Exception as e:
      print(f"Error occurred: {e}")
      return -1

##################################################################
#
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   try:
      result = datatier.select_one_row(dbConn, "SELECT COUNT(*) FROM EmployerInfo")
      return result[0] if result else 0
   except Exception as e:
      print(f"Error occurred: {e}")
      return -1

##################################################################
#
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   try:
      result = datatier.select_one_row(dbConn, "SELECT COUNT(*) FROM ClientInfo")
      return result[0] if result else 0
   except Exception as e:
      print(f"Error occurred: {e}")
      return -1

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and %
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID;
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   try:
      sql = """
       SELECT Lobbyist_ID, First_Name, Last_Name, Phone
       FROM LobbyistInfo
       WHERE First_Name LIKE ? OR Last_Name LIKE ?
       ORDER BY Lobbyist_ID ASC
       """
      params = [pattern, pattern]
      results = datatier.select_n_rows(dbConn, sql, params)

      if results:
         return [Lobbyist(*row) for row in results]
      else:
         return []
   except Exception as e:
      print(f"Error occurred while fetching lobbyists: {e}")
      return []

##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
    try:
        sql_basic_info = """
       SELECT 
           li.Salutation, li.First_Name, li.Middle_Initial, li.Last_Name, li.Suffix, 
           li.Address_1, li.Address_2, li.City, li.State_Initial, li.ZipCode, li.Country, 
           li.Email, li.Phone, li.Fax,
           GROUP_CONCAT(DISTINCT ly.Year) AS Years_Registered,
           (SELECT SUM(Compensation_Amount) 
            FROM Compensation 
            WHERE Lobbyist_ID = li.Lobbyist_ID) AS Total_Compensation
       FROM LobbyistInfo li
       LEFT JOIN LobbyistYears ly ON li.Lobbyist_ID = ly.Lobbyist_ID
       WHERE li.Lobbyist_ID = ?
       GROUP BY li.Lobbyist_ID
       """
        cursor = dbConn.cursor()
        cursor.execute(sql_basic_info, [lobbyist_id])
        basic_info_result = cursor.fetchone()

        if not basic_info_result:
            return None

        sql_employers = """
       SELECT DISTINCT Employer_Name FROM EmployerInfo 
       JOIN LobbyistAndEmployer ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID 
       WHERE LobbyistAndEmployer.Lobbyist_ID = ?
       ORDER BY Employer_Name ASC
       """
        cursor.execute(sql_employers, [lobbyist_id])
        employers_result = cursor.fetchall()
        employers = [employer[0] for employer in employers_result] if employers_result else []

        lobbyist_details = LobbyistDetails(
            Lobbyist_ID=lobbyist_id,
            Salutation=basic_info_result[0],
            First_Name=basic_info_result[1],
            Middle_Initial=basic_info_result[2],
            Last_Name=basic_info_result[3],
            Suffix=basic_info_result[4],
            Address_1=basic_info_result[5],
            Address_2=basic_info_result[6],
            City=basic_info_result[7],
            State_Initial=basic_info_result[8],
            Zip_Code=basic_info_result[9],
            Country=basic_info_result[10],
            Email=basic_info_result[11],
            Phone=basic_info_result[12],
            Fax=basic_info_result[13],
            Years_Registered=basic_info_result[14].split(',') if basic_info_result[14] else [],
            Employers=employers,
            Total_Compensation=float(basic_info_result[15]) if basic_info_result[15] is not None else 0.0
        )
        return lobbyist_details
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid.
#          An empty list is also returned if an internal error
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
    try:
        # Retrieve the top N lobbyists based on total compensation for the given year
        sql = """
        SELECT 
            l.Lobbyist_ID,
            l.First_Name, 
            l.Last_Name, 
            l.Phone, 
            SUM(c.Compensation_Amount) AS TotalCompensation
        FROM 
            LobbyistInfo l
        JOIN 
            Compensation c ON l.Lobbyist_ID = c.Lobbyist_ID
        WHERE 
            strftime('%Y', c.Period_Start) = ? OR strftime('%Y', c.Period_End) = ?
        GROUP BY 
            l.Lobbyist_ID
        ORDER BY 
            TotalCompensation DESC
        LIMIT ?
        """
        params = [year, year, N]
        nrows = datatier.select_n_rows(dbConn, sql, params)

        lobbyists = []
        for row in nrows:
            Lobbyist_ID, First_Name, Last_Name, Phone, TotalCompensation = row

            client_sql = """
            SELECT cl.Client_ID, cl.Client_Name
            FROM ClientInfo cl
            JOIN Compensation c ON cl.Client_ID = c.Client_ID
            WHERE c.Lobbyist_ID = ? AND (strftime('%Y', c.Period_Start) = ? OR strftime('%Y', c.Period_End) = ?)
            ORDER BY cl.Client_Name ASC
            """
            client_rows = datatier.select_n_rows(dbConn, client_sql, [Lobbyist_ID, year, year])

            clients = []
            totalNames = {}

            for client_id, client_name in client_rows:
                if client_name not in totalNames or client_id not in totalNames.get(client_name, set()):
                    clients.append(client_name)
                    if client_name in totalNames:
                        totalNames[client_name].add(client_id)
                    else:
                        totalNames[client_name] = {client_id}

            clients.sort()

            lobbyists.append(LobbyistClients(
                Lobbyist_ID=Lobbyist_ID,
                First_Name=First_Name,
                Last_Name=Last_Name,
                Phone=Phone,
                Total_Compensation=TotalCompensation,
                Clients=clients
            ))

        return lobbyists
    except Exception as e:
        print(f"Error occurred: {e}")
        return []

##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below),
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
    try:
        cursor = dbConn.cursor()
        cursor.execute("SELECT 1 FROM LobbyistInfo WHERE Lobbyist_ID = ?", (lobbyist_id,))
        if cursor.fetchone() is None:
            return 0
        else:
            cursor.execute("INSERT INTO LobbyistYears (Lobbyist_ID, Year) VALUES (?, ?)", (lobbyist_id, year))
            dbConn.commit()
            return 1  # Return 1 to indicate success
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0  # Return 0 in case of any error

##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
   try:
      sql = "UPDATE LobbyistInfo SET Salutation = ? WHERE Lobbyist_ID = ?"
      params = [salutation, lobbyist_id]
      result = datatier.perform_action(dbConn, sql, params)
      return 1 if result > 0 else 0
   except Exception as e:
      print(f"Error occurred: {e}")
      return 0
