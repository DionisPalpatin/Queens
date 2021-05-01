import os


class Field():
    def __init__(self, size, quan_queens):
        self.size = size
        self.queens = quan_queens
        self.used_places = list()
        self.matrix = list()
        self.temp_quan = 0
        self.all_variants = list()


    def check(self, i, j):
        flag = True
        for k in range(len(self.used_places)):
            if i == self.used_places[k][0] or j == self.used_places[k][1] or\
                abs(i - self.used_places[k][0]) == abs(j - self.used_places[k][1]):
                flag = False
                break
        return flag

    def creat_folder(self, folder):
        if not os.path.exists(f"J:\\Files\\Python\\Homeworks\\Queens\\Variations\\{folder}"):
            os.mkdir(f"J:\\Files\\Python\\Homeworks\\Queens\\Variations\\{folder}")


    def creat_file(self, filename, folder, positions):
        with open(f"J:\\Files\\Python\\Homeworks\\Queens\\Variations\\{folder}\\{filename}.txt", "w") as f:
            for i in range(len(positions)):
                for j in range(len(positions[i])):
                    f.write(positions[i][j])
                f.write("\n")


    def matrix_done(self):
        for i in range(self.size):
            self.matrix.append([])
            for j in range(self.size):
                self.matrix[i].append("0")



    #эта функция работает не совсем верно, я ее еще не трогал
    #поэтому она закоммитчена в head file'е
    def check_list(self):
        i = 0
        while i < len(self.all_variants) - 1:
            j = i + 1
            while j < len(self.all_variants):
                flag = True
                line = 0
                while line < self.size and flag:
                    if self.all_variants[i][line] == self.all_variants[j][line]:
                        del self.all_variants[j]
                        flag = False
                j += 1
            i += 1