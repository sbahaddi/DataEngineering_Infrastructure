from faker import Faker
import csv


def main():
    output = open('data/faker_data1M.CSV', 'w')
    fake = Faker()
    header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']
    mywriter = csv.writer(output)
    mywriter.writerow(header)
    for _ in range(1000000):
        mywriter.writerow([fake.name(), fake.random_int(min=18, max=80, step=1), fake.street_address(
        ), fake.city(), fake.state(), fake.zipcode(), fake.longitude(), fake.latitude()])
    output.close()


if __name__ == "__main__":
    main()
    pass
