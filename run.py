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

    transport = get_transport_method()
    distance = get_travel_distance()

    data = {
        'name': input_string,
        'transport': transport,
        'distance': distance
    }

    update_worksheet(data)


def get_transport_method():
    """
    Retrieve the mode of transport the user takes to travel to work.
    """
    print("Please provide us with your main mode of transport to work.")
    print("For example, if you cycle 0.4 miles to a train station and then take a train for 3 miles, your answer would be Train.\n")

    input_string = input("Enter your mode of transport below:\n")
    print(f"Your main mode of transport: {input_string}")
    return input_string


def get_travel_distance():
    """
    Retrieve the total distance traveled to work in miles.
    """
    print("Please provide us with the total distance you travel to work (in miles).")
    print("When entering your answer, please do not include the units.")
    print("Example answer: 1.4\n")

    distance = validate_travel_distance()
    print(f"The distance you travel: {distance} miles.")
    return distance


def validate_travel_distance():
    while True:
        input_string = input(
            "Enter the distance you travel below:\n")
        try:
            distance = float(input_string)
            return distance
        except ValueError:
            print("Invalid input. Please enter a valid distance (numbers only)")


def update_worksheet(data):
    """
    Update the spreadsheet with the provided data.
    Calculates the average distance travelled to work for all participants
    """
    sheet = SHEET.worksheet("methods")

    name = data['name']
    transport = data['transport']
    distance = data['distance']

    next_row = len(sheet.get_all_values()) + 1

    sheet.update(f"A{next_row}", name)
    sheet.update(f"B{next_row}", transport)
    sheet.update(f"C{next_row}", distance)

def calculate_average_distance():
    """
    Calculates the average distance travelled to work for all participants
    """
    sheet = SHEET.worksheet("methods")

    distances = sheet.col_values(3)[1:]

    total_distance = sum(float(distance) for distance in distances)
    avg_distance = total_distance / len(distances)

    average_sheet = SHEET.worksheet("average")
    average_sheet.update("B2", avg_distance)

    print(avg_distance)

def main():
    """
    Run all functions
    """
    get_employee_name()
    calculate_average_distance()

main()
