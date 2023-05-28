# Work Transport Survey

This program collects information about employees' mode of transport and distance traveled to work. It updates a Google Spreadsheet with the survey responses and calculates the average distance traveled by all participants.

## Description

The Work Transport Survey is a Python program that uses the gspread library and Google Sheets API to collect employee data and perform calculations. It prompts users to enter their name, main mode of transport to work, and total distance traveled in miles. The collected data is then stored in a Google Spreadsheet.

The program also calculates the average distance traveled by all participants and updates the average distance in the spreadsheet.

## Features

### Introduction

- The survey starts with an line of text introducing the user to the survey.

### Questions

- Each of the questions follow the same structure:
    - The question itself
    - An example of what your answer needs to contain and what not to do, with an example entry being printed
    - A line of text asking the user to enter their answer in the line below.
    - Once the answer has been submitted, a line of text realting to the question is printed followed by their entry so that you can see in real time the data that you are entering.

- With the use of a uniform structure throughout the survey, it is easy for the user to follow along and not get lost in the data that has previously been entered. The questions are each posted and then asnwered one at a time to further aid the ease of use of the program.

### Data Validation

- When the user enters a value for the question reagrding travel distance, the program is designed not to accept an answer unless it is an integer. For example, is the user where to enter '1.3 miles@', this will return a value error as it is specified that the use of letters and symbols is not accepted within the answer for this question. The text returned by entering the example entry is as follows: 'Invalid input. Please enter a valid distance (numbers only)'
- The reasoning for this exemption is prevent the data that is pushed to the spreadsheet from being inconsistent and causing and potential issues with the rest of the spreadsheet.

### Data Sums

- Once the data has been collected and pushed to the 'methods' worksheet, thr program will then calculate the average distance that is travelled based on the number of entries that have been received. All of the distances are added toghether and then divided by the total number of entries to give this value. This calculation is called upon each time the survey is completed and uploads this value to the 'average' worksheet.
- The number of times that survey is completed is also added to the same 'average' worksheet, so that the persons who review the data can get a better idea and understanding of the average value that they are presented with.

### Final Statement

- After all of the survey questions have been answered and the calculations are uplaoded, a line of text appears to notify the user that the survey is complete and they can carry on going about their day. The program will not continue to run once all questions are answered.

## Testing

- When testing this program, I initialy encountered an issue where there was not a lines space between where the question details and the entry text was displayed. I fixed this by adding '\n' within the last print statement and the following input string.
- I also faced an issue with the calculate_total_participants() function where the expected value was not being displayed on the worksheet. This was because the function was not expecting the cell on the worksheet to be empty and was fixed by updating the code so that it checks if the value of the "A2" cell is None before converting it to an integer. Additionally, after updating the run_count value, it converts it back to a string and updates the cell in the "average" worksheet.
- I tested that when an invalid entry is submitted on the third question that the program returns an error, explanation and asks for the answer to be submitted again.
- As far as the first and second question are concerned, I did not create any rules to say that number or symbols cannot be used. This is because the data that is entered is not involved in any sort of calculation and is still valid. If for example when asked to provide your main mode of transport, the user enters BMW M5, the person reviewing the data will be able to tell that they travel by car.
- I have tested and confirmed that the code works as intended in the Code Institute Heroku terminal.
- No errors where returned when checking my code on pyhtonchecker.com 

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku
-Steps for delpoyment:
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to Pyhton and NodeJS in this order
    - Link the Heroku app to the repository
    - Click Deploy

## Credits

- Lines 1 - 13 of the code in the run.py file where heavily inspired by the Love Sandwiches essentials project provided by The Code Institue learing material.
- Code institue for the deployment terminal

## Link to worksheet
- Here is a link to the worksheet where the data is stored: https://docs.google.com/spreadsheets/d/1mwcvVwqqPWcnyQWeXtNNBYJB2Z9f3CAHiIwDPmlQIDM/edit?usp=sharing
