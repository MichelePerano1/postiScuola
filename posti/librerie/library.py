import random
import string

cognomi = [
    "BERTAINA", "BERTOLOTTI", "BONACCORSO", "BRERO", "BRUNO", "DARBESIO", "EL FOURATI", "EL JABER", "FISSOLO",
    "FRACCHIA", "GARELLO", "GENOVESE", "IZZA", "KACMOLI", "LAPALORCIA", "LERDA", "PANI", "PERANO", "PIRRA",
    "STEFFENINO", "TARICCO"
]

cryptKeys = [
    [2, 4, 6, 1, 7, 3, 5],  # 0
    [5, 3, 6, 7, 1, 2, 4],  # 1
    [6, 1, 4, 2, 7, 5, 3],  # 2
    [5, 3, 1, 6, 4, 7, 2],  # 3
    [4, 2, 7, 1, 3, 5, 6],  # 4
    [4, 6, 2, 7, 3, 1, 5],  # 5
    [3, 5, 2, 6, 1, 7, 4],  # 6
    [3, 5, 7, 1, 6, 4, 2],  # 7
    [3, 4, 7, 2, 6, 1, 5],  # 8
    [3, 7, 2, 5, 1, 6, 4]  # 9
]


def has_duplicates(matrix):
    freq = {}
    for row in matrix:
        for num in row:
            if num in freq:
                return True
            freq[num] = 1
    return False


def input_posti(oldPosti, rows, cols, students):

    for i in range(rows):
        for j in range(cols):
            try:
                oldPosti[i][j] = int(input(f"{(j + 1) + (i * cols)}: "))
                if oldPosti[i][j] == 0:
                    random.shuffle(students)
                    for i in range(rows):
                        for j in range(cols):
                            oldPosti[i][j] = students[j + (i * cols)]
                    return
            except ValueError:
                print("Invalid input, please enter a number.")

    if has_duplicates(oldPosti):
        print("\nRipetizione nella scrittura dei posti, riscriverli.\n")


def print_posti(posti, rows, cols):
    print("\n")
    for i in range(rows):
        for j in range(cols):
            print(posti[i][j], end=" ")
        print("\n")
    print("\n")


def choose_keys():
    random_keys = random.sample(range(0, 10), 3)
    #print("\nChiavi scelte:")
    #for key in random_keys:
     #   print(f"\n{key}: {cryptKeys[key]}")
    #print("\n")
    return random_keys


def print_final_posti(posti, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(cognomi[posti[i][j] - 1], end=" ")
            if j == 2 or j == 4:
                print("|", end=" ")
            if j == 6:
                print("\n", end="")
    print("\n")


def generation_posti(oldPosti, rows, cols, students, newPosti, hash_list, finalPosti):
    random.shuffle(students)
    random.shuffle(hash_list)

    for i in range(rows):
        for j in range(cols):
            if hash_list[j] <= 5:
                newPosti[(i + 2) % rows][j] = oldPosti[i][j]
            else:
                newPosti[(i + 1) % rows][j] = oldPosti[i][j]

    #print_posti(newPosti, rows, cols)

    random_keys = choose_keys()

    for i in range(rows):
        for j in range(cols):
            finalPosti[i][j] = newPosti[i][cryptKeys[random_keys[i]][j] - 1]

    return finalPosti

def transform(posti,rows,cols):
    k=0
    checkForDoubles(posti)
    postiT=[[0] * 7 for _ in range(3)]
    for i in range(rows):
        for j in range(cols):
            try:
                postiT[i][j]=cognomi.index(posti[7*i+j])+1
            except:
                postiT[i][j]='error'
                k=1
    return postiT,k

def checkForDoubles(posti):
    k=0
    doubles=[]
    for i in range(len(posti)):
        j=i+1
        while(j<len(posti)):
            if(posti[i]==posti[j]):
                doubles.append([i,j])
                k=1
            j+=1
    if k==1:
        for item in doubles:
            posti[item[0]]='error'
            posti[item[1]]='error'
    return k




def main(oldPosti):
    rows=3
    cols=7
    nStud = 21
    students = list(range(1, nStud + 1))
    random.seed()

    hash_list = list(range(1, cols + 1))
    newPosti = [[0 for _ in range(cols)] for _ in range(rows)]
    finalPosti = [[0 for _ in range(cols)] for _ in range(rows)]

    #print_posti(oldPosti, rows, cols)

    finalPosti = generation_posti(oldPosti, rows, cols, students, newPosti, hash_list, finalPosti)

    postiT=["" for _ in range(21)]
    for i in range(rows):
        for j in range(cols):
            postiT[7*i+j]=cognomi[finalPosti[i][j]-1]
    postiT=toCammelCase(postiT)
    print(postiT)
    return postiT


def toCammelCase(s):
    news=s
    for i in range(len(s)):
        news[i]=s[i].title()
    return news