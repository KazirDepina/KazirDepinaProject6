import urllib.request
import json
from colorama import Fore, Back, init

init(autoreset=True)

# Download the salary data
downloaded_data = urllib.request.urlopen("http://webhost.bridgew.edu/jsantore/Fall2026/CS1/BLStechSalaries2025.json")
data = json.load(downloaded_data)

# Choose which type of jobs to analyze
major = input("Do you want COMP or CYBF jobs? ").lower()

while major != "comp" and major != "cybf":
    print(Fore.RED + "Please enter COMP or CYBF.")
    major = input("Do you want COMP or CYBF jobs? ").lower()

while True:

    print("\nSalary Analysis")
    print("[1] Find jobs with a high enough starting salary")
    print("[2] Find jobs with a high enough salary after 2 years")
    print("[3] Find the state with the highest starting salary")
    print("[4] Find the state with the highest two-year salary")
    print("[5] Additional analysis")
    print("[6] Quit")

    choice = input("Enter your choice: ")

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print(Fore.RED + "That is an invalid choice.")

    # Search by starting salary
    elif choice == "1":

        desired_salary = int(input("How much do you want to make starting out? "))

        print("\nJobs with a starting salary of at least $" + str(desired_salary))

        found_job = False

        for job in data:

            if major not in job["Occupation"].lower():
                continue

            if job["entry_wage"] >= desired_salary:
                print(Back.CYAN + Fore.BLACK +
                      job["Occupation"] + " - " +
                      job["Area"] + " - Starting Salary: $" +
                      str(job["entry_wage"]))

                found_job = True

        if found_job == False:
            print("No jobs were found with that starting salary.")

    # Search by two-year salary
    elif choice == "2":

        desired_salary = int(input("How much do you want to make after two years? "))

        print("\nJobs with a two-year salary of at least $" + str(desired_salary))

        found_job = False

        for job in data:

            if major not in job["Occupation"].lower():
                continue

            if job["wage_two_years_in"] >= desired_salary:
                print(Back.GREEN + Fore.BLACK +
                      job["Occupation"] + " - " +
                      job["Area"] + " - Two-Year Salary: $" +
                      str(job["wage_two_years_in"]))

                found_job = True

        if found_job == False:
            print("No jobs were found with that two-year salary.")

    # Find the highest starting salary
    elif choice == "3":

        highest_salary = 0
        highest_job = ""
        highest_state = ""

        for job in data:

            if major not in job["Occupation"].lower():
                continue

            if job["entry_wage"] > highest_salary:
                highest_salary = job["entry_wage"]
                highest_job = job["Occupation"]
                highest_state = job["Area"]

        if highest_job != "":
            print("\nState with the highest starting salary:")
            print(Fore.YELLOW + highest_job)
            print(Fore.YELLOW + highest_state)
            print(Fore.YELLOW + "Starting Salary: $" + str(highest_salary))

        else:
            print("No matching jobs were found.")

    # Find the highest two-year salary
    elif choice == "4":

        highest_salary = 0
        highest_job = ""
        highest_state = ""

        for job in data:

            if major not in job["Occupation"].lower():
                continue

            if job["wage_two_years_in"] > highest_salary:
                highest_salary = job["wage_two_years_in"]
                highest_job = job["Occupation"]
                highest_state = job["Area"]

        if highest_job != "":
            print("\nState with the highest two-year salary:")
            print(Fore.MAGENTA + highest_job)
            print(Fore.MAGENTA + highest_state)
            print(Fore.MAGENTA + "Two-Year Salary: $" + str(highest_salary))

        else:
            print("No matching jobs were found.")

    # Not implemented
    elif choice == "5":

        print(Back.BLUE + Fore.WHITE + "Not implemented")

    # Quit the program
    elif choice == "6":

        print("Thank you for using the salary analysis program!")
        break


