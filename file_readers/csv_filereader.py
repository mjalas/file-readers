import csv


class CSVFileReader(object):

    @staticmethod
    def read_file(filename, func, header=None, delimiter=' ', quotechar='|', debug=False):
        data = {}
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
            for row in reader:
                if debug:
                    print(row)
                if header and header in row[0]:
                    continue
                func(data, row)
        return data
