class programmer:
    company = "microsoft"

    def __init__(self, nama, paisa, zip):
        self.name = nama
        self.salary = paisa
        self.pincode = zip


hello = programmer("Danish", 1200000, 192231)
hello.language = "python"
print(hello.company, hello.name, hello.salary, hello.pincode, hello.language)


javid = programmer("javid", 1200000, 192231)
javid.language = "js"
print(javid.company, javid.name, javid.salary, javid.pincode, javid.language)
