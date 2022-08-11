# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data



def save_csv(csvoutput_path):
            
    with open(csvoutput_path, "w", newline='') as csv_file:
        csv_writer_obj = csv.writer(csv_file, delimiter=",")
        file_columns = ["Lender", "Max Loan Amount", "Max LTV",	"Max DTI",	"Min Credit Score",	"Interest Rate"]

        csv_writer_obj.writerow(file_columns)

        for each_loan in qualifying_loans:
            csv_writer_obj.writerow(each_loan)