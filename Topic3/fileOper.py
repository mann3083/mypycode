import random


def write_to_file(loc):
    str1 = 'ABC|CDE|EFG|FHG|ABC|CDE|EFG|1FHGABC|CDE|EFG|2FHGABC|CDE|EFG|3FHGABC|CDE|EFG|FHG|ABC|CDE|EFG|FHG|ABC|CDE|EFG|1FHGABC|CDE|EFG|2FHGABC|CDE|EFG|3FHGABC|CDE|EFG|FHG'
    # mode = 'r' if mode == '' else mode
    try:
        delm = '|'
        # File open part
        with open("st.txt", 'w') as f:
            sp = str1.split(delm)
            for x in range(2000):
                sp[(len(sp) - 1) // 2] = getRandomNum(7)
                f.write(delm.join(sp))
                f.write('\n')
    except:
        # In case of some issue
        print("Some Error in Write to File")


def getRandomNum(digits):
    try:
        temp = int(random.random() * 10000000)
        num = str(temp)
        while len(num) != digits:
            num = str(int(random.random() * 10000000))
        return num
    except:
        print("Some Error in Get random Number")
        return 0


write_to_file('')
