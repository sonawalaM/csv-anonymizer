import csv
import hashlib

def anonymize_value(value):
    return hashlib.sha256(value.encode()).hexdigest()

def anonymize_csv(input_file, output_file, columns_to_anonymize):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            for column in columns_to_anonymize:
                if column in row:
                    row[column] = anonymize_value(row[column])
            writer.writerow(row)
