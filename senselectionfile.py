def findmatchlength(substr,string):
    rvalue=0
    if(string.count(substr)>0):
        return len(substr.split())
        
    elif(len(substr.split())>1):
        temp=len(substr.split())
        while(temp>0):
            substr=substr.rsplit(' ',1)[0]
            if(string.count(substr)>0):
                rvalue=len(substr.split())
                temp=0
            if(len(substr.split())==1):
                rvalue=0
                temp=0
        return rvalue
    else:
        return 0

import nltk
import nltk.data
import sys
sentdec=nltk.data.load('tokenizers/punkt/english.pickle')
f = open(sys.argv[1],"r")
string=f.read()
slist=sentdec.tokenize(string.strip())
score= [0] *len(slist)
occurence=[0]*len(slist)
length=[0]*len(slist)
impsen=[0]*len(slist)
query=raw_input("Enter query: ")
for x in range(0,(len(slist))):
    s2list=nltk.word_tokenize(slist[x])
    #s2list=slist[x].split()
    score[x]=float(len(set(s2list)))/len(s2list)
    occurence[x]=slist[x].count(query)
    length[x]=findmatchlength(query,slist[x])
    impsen[x]=x
#print score
#print len(score)
for i in range( 0,len(length) ):
   for k in range(0, len(length)-1):
     if ( length[k]<=length[k+1] ):
        if(length[k]==length[k+1]):
           if(occurence[k]<=occurence[k+1]):
               if(occurence[k]==occurence[k+1]):
                   if(score[k]<=score[k+1]):
                       if(score[k]==score[k+1]):
                           pass
                       else:
                          temp=length[k]
                          length[k]=length[k+1]
                          length[k+1]=temp
                          temp=score[k]
                          score[k]=score[k+1]
                          score[k+1]=temp
                          temp=occurence[k]
                          occurence[k]=occurence[k+1]
                          occurence[k+1]=temp                         
                          temp=impsen[k]
                          impsen[k]=impsen[k+1]
                          impsen[k+1]=temp
                   else:
                      temp=length[k]
                      length[k]=length[k+1]
                      length[k+1]=temp
                      temp=score[k]
                      score[k]=score[k+1]
                      score[k+1]=temp
                      temp=occurence[k]
                      occurence[k]=occurence[k+1]
                      occurence[k+1]=temp                         
                      temp=impsen[k]
                      impsen[k]=impsen[k+1]
                      impsen[k+1]=temp
        else:
          temp=length[k]
          length[k]=length[k+1]
          length[k+1]=temp
          temp=occurence[k]
          occurence[k]=occurence[k+1]
          occurence[k+1]=temp
          temp=score[k]
          score[k]=score[k+1]
          score[k+1]=temp                         
          temp=impsen[k]
          impsen[k]=impsen[k+1]
          impsen[k+1]=temp
       
print "Top 10 sentences in document are: \n"
for i in range(0,10):
    print slist[impsen[i]]+'\n'
print occurence,"\n\n",score,"\n\n",length,"\n\n",impsen
                
       
     
'''
temp=length[k]
       length[k]=length[k+1]
       length[k+1]=temp
       temp=impsen[k]
       impsen[k]=impsen[k+1]
       impsen[k+1]=temp
tokens=nltk.word_tokenize(raw)
text=nltk.Text(tokens)
type(text)
text.concordance("players")
text.collocations()
'''
