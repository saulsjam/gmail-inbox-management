# Gmail Inbox Management

This Python script uses the `simplegmail` package to mark an email as important or put it in the trash based on the sender's email address. The sender's address is compared to a list of emails that you upload in a CSV file. The script requires you to input an age range for the emails. The script will look for emails older than a given number of days and newer than a given number of days.

## Features

- Marks emails from specific addresses as important
- Trashes all other emails
- Counts the number of emails marked as important and trashed

## Requirements

- Python 3.x
- `simplegmail` package
- `csv` module
- `re` module

## Installation

- Install the required packages:
    ```sh
    pip install simplegmail
    ```

- Follow the setup instructions for `simplegmail` to configure authentication with your Gmail account: [simplegmail Setup](https://github.com/jeremyephron/simplegmail#setup)

## Usage

- Prepare a CSV file (`important_addresses.csv`) with a header row and a column named `email` containing important email addresses.

- Edit the script to specify the age range of emails to process by modifying the `older_than_days` and `newer_than_days` variables.

- Run the script:
    ```sh
    python your_script.py
    ```
