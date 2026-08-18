def table_generate(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"
    with open(
        f"The-Ultimate-Python-Course-main/The-Ultimate-Python-Course-main/Chapter 9 - PS/tables/table{n}.txt",
        "w",
    ) as f:
        f.write(table)


for i in range(2, 21):
    table_generate(i)
