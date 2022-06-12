def mergesort(mylist):
    if len(mylist)>1:
        mid=len(mylist)//2
        left=mylist[:mid]
        right=mylist[mid:]
        mergesort(left)
        mergesort(right)

        i=j=k=0
        while i< len(left) and j<len(right):
            if left[i]<=right[j]:
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
mylist=[1,2,5,7,4,9]
mergesort(mylist)
print(mylist)


