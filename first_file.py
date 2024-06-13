# arr=[5,3,6,8,4,1,2,9]
# maxi=arr[0]
# mini=arr[0]
# for i in range (len(arr)-1):  
#     maxi=max(maxi,arr[i+1])
#     mini=min(mini,arr[i+1])
# print(maxi)
# print(mini)
# print(maxi+mini)


# a=int(input())
# b=a*a
# if b%10==a:
#     print("same")
# else:
#     print("not same")


# a="allergy"
# c="allergic"
# b=[0]*26
# for i in range(len(a)):
#     b[ord(a[i])-97]+=1
# for i in range(len(c)):
#     b[ord(c[i])-97]-=1
# for i in range(len(b)):
#     num=i
#     if b[i]!=0:
#         print("false")
#         break
# if b[num]==0:
#     print("true")


# n=4   ## no of bulbs
# b=[0]*n
# for i in range(n):  ##can be soved by taking sqrt of the num
#     counter=0
#     while (counter<n):
#         counter+=i+1
#         if i==0:
#             b[1]*n
#         if counter<=n:
#             b[counter-1]=1-b[counter-1]
# num=0
# for i in range(n):
#    if b[i]==1:
#       num+=1
# print(num)

str="saveChangesInTheEditor"
b=""
for i in str:
    if i.islower():
        b+=i.upper()
    else:
        print(b)
        b=""
        b+=i.lower()
        
print(b)   



           
          
               
               


        
        
