a=input("Enter String:")
vowel=0
for i in range(0,len(a)):
    if (a[i]!=" "):
        if (a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='0'
            or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I'
            or a[i]=='O' or a[i]=='U'):
            vowel=vowel+1
            
print("Total Vowels=",vowel)

input()
