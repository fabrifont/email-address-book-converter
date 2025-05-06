import gui
import csv_utils as csv
import argparse

def main():
     parser = argparse.ArgumentParser()
     parser.add_argument("file")
     file = parser.parse_args().file
     file_utf8 = csv.convert_csv_utf8(file)
     file_outlook = csv.format_csv(file_utf8)
     new_filename = file.replace(".csv", "") + "_CONVERTED.csv"
     csv.save_csv(file_outlook, new_filename)

main()