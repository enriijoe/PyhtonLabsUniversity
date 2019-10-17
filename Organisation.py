class Organization:
    def __init__(self):
        name = input("Enter the name of the organization: ")
        address = input("Enter the address of this organization: ")
        director = input("Enter the director's name of this organization: ")
        phone = input("Enter the phone number of this organization: ")
        self.nameOfOrganization = name
        self.addressOfOrganization = address
        self.directorOfOrganization = director
        self.phoneNumber = phone

    def output(self):
        data = ("ORGANISATION: " + self.nameOfOrganization + "; "
                + "ADDRESS: " + self.addressOfOrganization + "; "
                + "DIRECTOR: " + self.directorOfOrganization + "; "
                + "PHONE NUMBER: " + self.phoneNumber + ".")
        print("====================================================================")
        print(data)
        print("====================================================================")

    def return_name(self):
        return self.nameOfOrganization

    def file_data(self):
        fdata = ("ORGANISATION: " + self.nameOfOrganization + ";\n"
                 + "ADDRESS: " + self.addressOfOrganization + ";\n"
                 + "DIRECTOR: " + self.directorOfOrganization + ";\n"
                 + "PHONE NUMBER: " + self.phoneNumber + ".\n"
                 + "====================================================================\n")

        file = open("OrganizationData.txt", "a")
        file.write(fdata)
        file.close()


def file_reading():
    file2 = open("OrganizationData.txt", "r")
    for line in file2:
        print(line)
    file2.close()


Organizations = list()
Names = list()
file_data = list()

i = 0
n = int(input("Enter an exact number of organisations: "))
while i < n:
    newOrganization = Organization()

    Organizations.append(newOrganization.file_data())
    Names.append(newOrganization.return_name())
    newOrganization.output()
    i = i + 1

sort = sorted(Names)
print("Sorted names of organisations:")
print(sort)

file_reading()

