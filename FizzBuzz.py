a=list(map(int,input().split()))
numbers=[]
for i in range(1,a[2]+1):
    numbers.append(i)
one=a[0]
two=a[1]
st=[]
for j in numbers:
    divide=j%one
    divide1=j%two
    if(divide==0 or divide==one):
        if(divide1==0 or divide1==two):
            st.append('FizzBuzz')
        else:
            st.append('Fizz')
    elif(divide1==0 or divide1==two):
        st.append('Buzz')
    else:
        st.append(j)
for k in st:
    print(k)
