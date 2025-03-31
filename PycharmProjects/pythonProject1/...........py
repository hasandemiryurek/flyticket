checkedOutBooks = {
    "9781408288191": ["117987", "124876"],
    "9781408286999": ["124876"],
    "9781408288535": []
     }


def createStudentList():
 studentFile=open("students.txt","r")
 studentDict={}
 for line in studentFile:
  arr=line.strip().split()
  if len(arr)>2:
   studentDict[arr[0]]=arr[1]+","+arr[2]
 return studentDict

studentId=input("student id?")
isbn=input("isbn?")
if studentId not in checkedOutBooks[isbn]:
    checkedOutBooks[isbn].append(studentId)
print(checkedOutBooks)

def best():
 check = {}
 for i in checkedOutBooks.values():
    for b in i:
        if b in check:
            check[b]=check[b]+1
        else:
            check[b]=1
 maxi =""
 max = 0
 for i in check:
     if check[i] > max:
       max = check[i]
       maxi = i
 return maxi
print(best())

























