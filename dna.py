# Implement a program that identifies to whom a sequence of DNA belongs

import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read database file into a variable
    database = []
    input_data = open(sys.argv[1])
    reader = csv.DictReader(input_data)
    for row in reader:
        data = {}
        for column in row:
            try:
                data[column] = int(row[column])
            except:
                data[column] = row[column]
        database.append(data)
    input_data.close()

    # Read DNA sequence file into a variable
    input_sequence = open(sys.argv[2])
    sequence = input_sequence.read()
    input_sequence.close()

    # Find longest match of each STR in DNA sequence
    sequence_data = {}
    for header in database[0].keys():
        if type(database[0][header]) == int:
            sequence_data[header] = longest_match(sequence, header)

    # Check database for matching profiles
    for profile in database:
        count = 0
        for header in sequence_data.keys():
            if profile[header] == sequence_data[header]:
                count += 1
        if count == len(sequence_data.keys()):
            print(profile["name"])
            return
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
