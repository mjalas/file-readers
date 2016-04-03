from unittest import TestCase
from file_readers.csv_filereader import CSVFileReader


def data_collector(data, row):
    if 'personnel' not in data:
        data['personnel'] = []
    values = {'name': row[0], 'age': int(row[1]), 'title': row[2]}
    data['personnel'].append(values)


class TestCSVFileReader(TestCase):

    def test_read_file(self):
        test_file = "data/test.csv"
        data = CSVFileReader.read_file(test_file, func=data_collector, header='Name', delimiter=";")
        row = data['personnel'][0]
        self.assertEqual(row['name'], 'John')
        self.assertEqual(row['age'], 24)
        self.assertEqual(row['title'], 'Developer')
