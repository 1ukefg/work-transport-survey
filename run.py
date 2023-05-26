import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('work-transport-survey')


def get_employee_name():
    """
    Retrieve the Emplyee name, mode of transport and distance travelled to work  from the user.
    """
    print("Thank you for taking the time to participate in the survey!")
    print("Lets start of by taking your first and last name.")
    print("An example entry could be: Tom Jerry\n")

    input_string = input("Enter your name below:\n")
    print(f"Your name: {input_string}")

def get_transport_method():
    """
    Retrieve the mode of transport the user takes to travel to work.
    """
    print("Please provide us with your main mode of transport to work.")
    print("For example, if you cycle 0.4 miles to a train station and then take a train for 3 miles, your answer would be Train.\n")

    input_string = input("Enter your mode of transport below:\n")
    print(f"Your main mode of transport: {input_string}")

def get_travel_distance():
    """
    Retrieve the total distance travelled to work in miles.
    """
    print("Please provide us with the total distance you travel to work (in miles).")
    print("When entering your answer, please do not include the units")
    print("Example answer: 1.4\n")
    
    input_string = input("Enter the distance you travel below:\n")
    print(f"The distance you travel: {input_string} miles.")

get_employee_name()
get_transport_method()
get_travel_distance()
