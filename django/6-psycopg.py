import psycopg2
mydb=psycopg2.connect(
    database="RAWAL",
    user="postgres",
    password="1234",
    host="localhost",
    port=5432,
)
cursor=mydb.cursor()
query='select * from "student"'
cursor.execute(query)
array=list(cursor.fetchall())


print(array)
print("Given data is:")
for x in array:
    print(x)
def mergesort(mylist,index):
    if len(mylist)>1:
        mid=len(mylist)//2
        left=mylist[:mid]
        right=mylist[mid:]
        mergesort(left,index)
        mergesort(right,index)

        i=j=k=0
        while i< len(left) and j<len(right):
            if left[i][index]<=right[j][index]:
                mylist[k]=left[i]
                i+=1
            else:
                mylist[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            mylist[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            mylist[k]=right[j]
            j+=1
            k+=1
    else:
        return mylist
mergesort(array,2)
print()
print("hence the sorted list is")
for x in array:
    print(x)




