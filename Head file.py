import Field


def recursion():
    if field.temp_quan < field.queens:
        for i in range(field.size):
            for j in range(field.size):
                if field.check(i, j):
                    field.matrix[i][j] = "1"
                    field.used_places.append([i, j])
                    field.temp_quan += 1
                    recursion()
    else:
        field.all_variants.append(field.matrix)

        
    field.matrix[field.used_places[-1][0]][field.used_places[-1][1]] = "0"
    del field.used_places[-1]
    field.temp_quan -= 1

    
size, quan = map(int, input().split())
field = Field.Field(size, quan)
field.matrix_done()
folder = f"Variant with {field.queens} queens"
field.creat_folder(folder)


for i in range(field.size):
    for j in range(field.size):
        field.matrix[i][j] = "1"
        field.used_places.append([i, j])
        field.temp_quan = 1
        recursion()
print("done")
# field.check_list()


with open(r"J:\Files\Python\Homeworks\Queens\Variations\Temp.txt", "w") as f:
    for i in range(len(field.all_variants)):
        for line in range(size):
            for column in range(size):
                f.write(field.all_variants[i][line][column])
            f.write("\n")
        f.write("\n")
print("Finish")