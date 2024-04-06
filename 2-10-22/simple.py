
# from macpath import split


def read_file (file_name):
    fobj = None
    data = None
    try:
        fobj = open(file_name , 'r')
        data = fobj.read()
    except Exception :
        print("Check your program again")
    finally:
        if fobj is not None:
            fobj.close()
    return data


if __name__ == "__main__":
    out = read_file("2-10-22\list.csv")
    print(out)
    line_data = out.split("\n")
    print(line_data)

    all_keys = line_data[0].split(",")
    data1 = line_data[1],split(",")
    d = {}

    for i in range (0,len(all_keys)):
        d[all_keys[i]] = data1[i]
        print(d)
