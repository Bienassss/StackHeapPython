import csv

class CSVDataHandler:
    def __init__(self, filename='output.csv'):
        self.filename = filename

    def write_numbers_to_csv_heap(self, numbers):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            index = 0
            count = 1
            while index < len(numbers):
                next_row = numbers[index:index + count]
                writer.writerow(next_row)
                index += count
                count *= 2

    def write_numbers_to_csv_stack(self, stack):
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for item in stack:
                writer.writerow([item])

    @staticmethod
    def __validate_numbers(func):
        def wrapper(self, *args, **kwargs):
            rows = func(self, *args, **kwargs)
            for row in rows:
                for num in row:
                    if not str(num).isdigit():
                        raise ValueError(f"Found a non-numeric value: '{num}'")
            return rows
        return wrapper

    @__validate_numbers
    def __read_rows_from_csv(self):
        rows = []
        with open(self.filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                rows.append(row)
        return rows

    def read_numbers_from_csv(self):
        rows = self.__read_rows_from_csv()
        numbers = []
        for row in rows:
            numbers.extend([int(num) for num in row])
        return numbers

    def clear_csv(self):
        open(self.filename, 'w').close()
