def presence_in(word,slist):
    count=0
    for string in slist:
        string=string.lower()
        if(string.count(word)>0):
            count=count+1
    if (count==0):
        return -1
    else:
        return count

import nltk
import nltk.data
import sys
from nltk.corpus import stopwords
import os
sentdec=nltk.data.load('tokenizers/punkt/english.pickle')
path=sys.argv[1]
files=[]
for filename in os.listdir(path):
   if filename.endswith(".txt"):
      files.append(filename)
stop = stopwords.words('english')
stop=[x.encode('UTF8') for x in stop]
query=(raw_input("Enter query: ")).lower()
query_words=query.split()
filtered_query = [w for w in query_words if not w in stop]
print 'query=',filtered_query
selectedsen=[]
imp=[]
ld=[]
counter=[0]*len(files)
print files, type(files[1])
tcount=0
for doc in files:
    f = open(path+doc,"r")
    string=f.read().decode('utf-8','ignore')
    wlist=string.lower().split()
    slist=sentdec.tokenize(string.strip())
    f.close()
    tf_idf=[0]*len(filtered_query)
    #tf-idf of query
    for x in range(0,(len(filtered_query))):
        tf=float(wlist.count(filtered_query[x]))/len(wlist)
        idf=len(slist)/presence_in(filtered_query[x],slist)
        tf_idf[x]=tf*idf
    #selecting sentences from each file
    for x in range(0,(len(slist))):
        tstr=slist[x].lower()
        s2list=nltk.word_tokenize(tstr)
        timp=0
        for i in range(0,len(filtered_query)):
            if(s2list.count(filtered_query[i])>0):
                timp=timp+tf_idf[i]
            if (timp>0):
                selectedsen.append(slist[x])
                imp.append(timp)
                ld.append((float(len(set(s2list)))/len(s2list)))
                counter[tcount]=counter[tcount]+1
    tcount=tcount+1
#print selectedsen, len(selectedsen)
topsen=[0]*len(selectedsen)
for i in range(0,len(selectedsen)):
    topsen[i]=i
for i in range( 0,len(ld) ):
   for k in range(0, len(ld)-1):
     if ( imp[k]<=imp[k+1] ):
        if(imp[k]==imp[k+1]):
           if(ld[k]<=ld[k+1]):
               if(ld[k]==ld[k+1]):
                   pass
               else:
                   temp=imp[k]
                   imp[k]=imp[k+1]
                   imp[k+1]=temp
                   temp=ld[k]
                   ld[k]=ld[k+1]
                   ld[k+1]=temp                         
                   temp=topsen[k]
                   topsen[k]=topsen[k+1]
                   topsen[k+1]=temp
        else:
            temp=imp[k]
            imp[k]=imp[k+1]
            imp[k+1]=temp
            temp=ld[k]
            ld[k]=ld[k+1]
            ld[k+1]=temp                         
            temp=topsen[k]
            topsen[k]=topsen[k+1]
            topsen[k+1]=temp
for i in range(0,len(selectedsen)):
    print selectedsen[topsen[i]]+'\n'
for i in range(0,len(counter)):
    print counter[i],' Sentences from ',files[i],'\n'
print len(selectedsen)

