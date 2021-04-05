class CsvReader:
    def __init__(self, filename=None, sep=',', header=True, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.fp = open(self.filename, "r")
        except FileNotFoundError:
            exit("File Not Found")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

    def getdata(self):
        self.fp.seek(self.skip_top)
        lst = []
        lines = self.fp.readlines()
        if self.skip_bottom != 0:
            lines = lines[::self.skip_bottom]
        for line in lines:
            line = line.rstrip("\n")
            sm_lst = []
            for item in line.split(self.sep):
                item = item.rstrip()
                if item == '':
                    exit("Bad Csv File")
                sm_lst.append(item)
            lst.append(sm_lst)
        return lst

    def getheader(self):
        self.fp.seek(0)
        if self.header is True:
            return self.fp.readline()
        return None


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()

