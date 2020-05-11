from bs4 import BeautifulSoup
import requests

search=input("Enter what you want to search : ")
filename=input("Enter file name for saving (without extension): ")
filename=filename+".txt"
search=search.replace(" ","_").lower()

file_=open(filename,"w")
file_.write("")
file_.close()
file_=open(filename,"a")


url="https://en.m.wikipedia.org/wiki/"+search

r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")

def Content_Heading(i):

    if i!=0:
        content=soup.findAll("h2",{"class":"section-heading"})
        print((content[i-1].text).upper())
        txt=(content[i-1].text).upper()
        file_.write(txt)

    else:
        print("INTRODUCTION")
        file_.write("INTRODUCTION")


def Main_Content(i):

    phrase="mf-section-"+str(i)
    content=soup.find("section",{"class":phrase})
    section=content.children

    print("")
    file_.write("\n")
    Content_Heading(i)
    file_.write("\n")

    print("")
    
    for sec in section:

        if sec.name=="p":
            print(sec.text)
            file_.write(sec.text)

        elif sec.name=="h3":
            break
    
    
def SubHeading_and_SubContent(i,j):
    try:
        section="mf-section-"+str(i)
        content=soup.find("section",{"class":section})
        SubHeadings=content.findAll("h3",{"class":"in-block"}) 

        print((SubHeadings[j-1].text).upper())
        txt=(SubHeadings[j-1].text).upper()
        file_.write(txt)

        SubContents=SubHeadings[j-1].find_next_siblings()

        for SubContent in SubContents:

            if SubContent.name=="p":
                print(SubContent.text)
                file_.write(SubContent.text)

            elif SubContent.name=="h3":
                break 
    except:
        print("Subsection does not exist!")
    
    


def TOC():

    content=soup.findAll("li",{"class":"toclevel-1"})
    print("")

    if len(content)==0:
        print("Page doesnt exist!!")
        exit()

    else:
        print("TABLE OF CONTENTS")
        file_.write("\n")
        file_.write("\n")

        print("")
        print("0 Introduction")
        file_.write("TABLE OF CONTENTS")
        file_.write("\n")
        file_.write("0 Introduction")
        file_.write("\n")

        
        for item in content:

            ContentText=item.find("span",{"class":"tocnumber"}).text+" "+item.find("span",{"class":"toctext"}).text
            print(ContentText)
            file_.write(ContentText)
            file_.write("\n")
            #print("    "+item.find("span",{"class":"tocnumber"}).text+".0 Intro")
            txt="    "+item.find("span",{"class":"tocnumber"}).text+".0 Intro"
            print(txt)
            file_.write(txt)
            file_.write("\n")
            SubTopic=item.findAll("li",{"class":"toclevel-2"})

            if len(SubTopic)!=0: # if subtopic exists
                TOC_Looper(SubTopic,2)
    
        
        

def TOC_Looper(SubTopic,i):
    
        for subitem in SubTopic:

            SubContentText="    "+subitem.find("span",{"class":"tocnumber"}).text+" "+subitem.find("span",{"class":"toctext"}).text
            print(SubContentText)
            file_.write(SubContentText)    
            file_.write("\n")
            className="toclevel-"+str(i)
            Sub_sub_Topic=subitem.findAll("li",{"class":className})

            if len(SubTopic)!=0:
                TOC_Looper(Sub_sub_Topic,i+1)



def main():

    
    TOC()
    file_.write("\n")
    print("")
    while(True):
        num=float(input("Enter which part you want (eg. 4.3) : "))
        i=int(num)
        j=int(round(num%1,1)*10)

        if j==0:
            Main_Content(i)
        else:
            SubHeading_and_SubContent(i,j)
        print("\n")
        file_.write("\n")
        choice=input("type any character to continue or q to quit: ")
        print("\n")

        choice=(choice.lower())[0]

        if choice=="q":
            break
    print("\n")
    txt="File is saved as "+filename+" in the current directory"
    print(txt)
    print("See ya Later! :)")
    

main()

