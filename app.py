from bs4 import BeautifulSoup
import requests

search=input("Enter what you want to search : ")
search=search.replace(" ","_").lower()

url="https://en.m.wikipedia.org/wiki/"+search

r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")

def Content_Heading(i):

    if i!=0:
        content=soup.findAll("h2",{"class":"section-heading"})
        print((content[i-1].text).upper())

    else:
        print("INTRODUCTION")


def Main_Content(i):

    phrase="mf-section-"+str(i)
    content=soup.find("section",{"class":phrase})
    section=content.children

    print("")
    Content_Heading(i)
    print("")
    
    for sec in section:

        if sec.name=="p":
            print(sec.text)

        elif sec.name=="h3":
            break
    
    
def SubHeading_and_SubContent(i,j):

    section="mf-section-"+str(i)
    content=soup.find("section",{"class":section})
    SubHeadings=content.findAll("h3",{"class":"in-block"}) 

    print((SubHeadings[j-1].text).upper())

    SubContents=SubHeadings[j-1].find_next_siblings()

    for SubContent in SubContents:

        if SubContent.name=="p":
            print(SubContent.text)

        elif SubContent.name=="h3":
            break


def TOC():

    content=soup.findAll("li",{"class":"toclevel-1"})
    print("")

    if len(content)==0:
        print("Page doesnt exist!!")
        exit()

    else:
        print("TABLE OF CONTENTS")
        print("")
        print("0 Introduction")

        
        for item in content:

            ContentText=item.find("span",{"class":"tocnumber"}).text+" "+item.find("span",{"class":"toctext"}).text
            print(ContentText)
            print("    "+item.find("span",{"class":"tocnumber"}).text+".0 Intro")
            SubTopic=item.findAll("li",{"class":"toclevel-2"})

            if len(SubTopic)!=0: # if subtopic exists
                TOC_Looper(SubTopic,2)
    
        
        

def TOC_Looper(SubTopic,i):
    
        for subitem in SubTopic:

            SubContentText="    "+subitem.find("span",{"class":"tocnumber"}).text+" "+subitem.find("span",{"class":"toctext"}).text
            print(SubContentText)    

            className="toclevel-"+str(i)
            Sub_sub_Topic=subitem.findAll("li",{"class":className})

            if len(SubTopic)!=0:
                TOC_Looper(Sub_sub_Topic,i+1)



def main():

    TOC()
    print("")

    num=float(input("Enter which part you want (eg. 4.3) : "))
    i=int(num)
    j=int(round(num%1,1)*10)

    if j==0:
        Main_Content(i)
    else:
        SubHeading_and_SubContent(i,j)
    

main()

