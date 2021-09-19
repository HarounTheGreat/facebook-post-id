path = "enter your post url"
s = path
s=s[s.find('m')+2:]+"azezea"
new=""
for i in range(len(s)):
    if s[i] in ["0","1","2","3","4","5","6","7","8","9"] :
        new=new+s[i]
    if s[i] not in ["0","1","2","3","4","5","6","7","8","9"] :
        break   
new2= ""
new1= ""
for i in range(len(s)): 
    if s[i] in ["/"] and s[i+1] in ["0","1","2","3","4","5","6","7","8","9"] : 
        new2=s[i+1:]
        for j in range(len(new2)) :
            if new2[j] in ["0","1","2","3","4","5","6","7","8","9"] :
                new1=new1+new2[j]
path=new + "_" + new1