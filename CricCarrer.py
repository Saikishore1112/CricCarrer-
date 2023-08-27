from bs4 import BeautifulSoup
import requests
print("----------------------------------------------------------------------Hello!! Welcome to Cric Carrer-----------------------------------------------------------------------------------")
print("Enter the number indicated to particular cricketer to view his stats in cricket")
print("1. Rohit sharma\n2. Shikhar Dhawan\n3. Virat Kohli\n4. K L Rahul\n5. Suresh Raina\n6. Ravindra Jadeja\n7. M S Dhoni\n8. Hardik Pandya\n9. Jasprit Bumrah\n10. Sachin Tendulkar\n11. Yuzendra Chahal\n12. Bhuvaneshwar Kumar\n13. Yuvraj Singh\n14. Ravichandran Ashwin\n15. Kapil Dev\n16. Gautam Gambhir\n17. Harbhajan Singh\n18. Umesh Yadav\n19. Rishabh Pant\n20. Dinesh Karthik\nenter any other number to exit")

f=open("cricketer.txt","w")

choice=int(input("\nenter your choice:"))
if choice==1:
    print("you have choosen Rohit sharma, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/576/rohit-sharma"
    f.write("Rohit Sharma\n\n")
elif choice==2:
    print("you have choosen Shikhar Dhawan, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/1446/shikhar-dhawan"
    f.write("Shikhar Dhawan\n\n")
elif choice==3:
    print("you have choosen Virat Kohli, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/1413/virat-kohli"
    f.write("Virat Kohli\n\n")
elif choice==4:
    print("you have choosen K L Rahul, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/8733/lokesh-rahul"
    f.write("K L Rahul\n\n")
elif choice==5:
    print("you have choosen Suresh Raina, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/413/suresh-raina"
    f.write("Suresh Raina\n\n")
elif choice==6:
    print("you have choosen Ravindra Jadeja, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/587/ravindra-jadeja"
    f.write("Ravindra Jadeja\n\n")
elif choice==7:
    print("you have choosen M S Dhoni, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/265/ms-dhoni"
    f.write("M S Dhoni\n\n")
elif choice==8:
    print("you have choosen Hardik Pandya, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/9647/hardik-pandya"
    f.write("Hardik Pandya\n\n")
elif choice==9:
    print("you have choosen Jasprit Bumrah, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/9311/jasprit-bumrah"
    f.write("Jasprit Bumrah\n\n")
elif choice==10:
    print("you have choosen Sachin Tendulkar, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/25/sachin-tendulkar"
    f.write("Sachin Tendulkar\n\n")
elif choice==11:
    print("you have choosen Yuzendra Chahal, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/7910/yuzvendra-chahal"
    f.write("Yuzendra Chahal\n\n")
elif choice==12:
    print("you have choosen bhuvneshwar kumar, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/1726/bhuvneshwar-kumar"
    f.write("Bhuvaneshwar Kumar\n\n")
elif choice==13:
    print("you have choosen Yuvraj Singh, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/69/yuvraj-singh"
    f.write("Yuvraj Singh\n\n")
elif choice==14:
    print("you have choosen Ravichandran Ashwin, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/1593/ravichandran-ashwin"
    f.write("Ravichandran Ashwin\n\n")
elif choice==15:
    print("you have choosen Kapil Dev, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/3838/kapil-dev"
    f.write("Kapil Dev\n\n")
elif choice==16:
    print("you have choosen Gautam Gambhir, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/308/gautam-gambhir"
    f.write("Gautam Gambhir\n\n")
elif choice==17:
    print("you have choosen Harbhajan Singh, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/75/harbhajan-singh"
    f.write("Harbhajan Singh\n\n")
elif choice==18:
    print("you have choosen Umesh Yadav, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/1858/umesh-yadav"
    f.write("Umesh Yadav\n\n")
elif choice==19:
    print("you have choosen Rishabh Pant, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/10744/rishabh-pant"
    f.write("Rishabh Pant\n\n")
elif choice==20:
    print("you have choosen Dinesh Karthik, the following are the stats:\n\n")
    s="https://www.cricbuzz.com/profiles/145/dinesh-karthik"
    f.write("Dinesh Karthik\n\n")
else:
    print("thank you!!")
    exit(0)

try:
    source=requests.get(s)
    soup=BeautifulSoup(source.text,'html.parser')

    q=soup.findAll("div",class_="cb-col cb-col-40 text-bold cb-lst-itm-sm")
    a=soup.findAll("div",class_="cb-col cb-col-60 cb-lst-itm-sm")
    info=soup.find("div",class_="cb-font-16 text-bold").text.split(" ")

    for i in range(1,3):
        print(info[i],end=" ")
        f.write(info[i])
        f.write(" ")
    print(":\n")
    f.write(":\n\n")

    for i in range(5):
        print(q[i].text,end=":")
        print(a[i].text)
        f.write(q[i].text)
        f.write(":")
        f.write(a[i].text)
        f.write("\n")
    print("\n")
    f.write("\n\n")

    skill=soup.findAll("div",class_="cb-plyr-tbl")
    for i in range(2):
        bat_bowl=skill[i].find("div",class_="cb-font-16 text-bold cb-lst-dom").text
        print(bat_bowl,":\n")
        f.write(bat_bowl)
        f.write(":\n\n")
        
        headings=soup.findAll("table",class_="table cb-col-100 cb-plyr-thead")[i].find("thead").findAll("th",class_="text-right")
        print("\t",end="")
        f.write("\t\t")
        for col_head in headings:
            col=col_head.text
            print(col,end="\t")
            f.write(col)
            f.write("\t\t")
        print("\n")
        f.write("\n\n")

        rows=soup.findAll("table",class_="table cb-col-100 cb-plyr-thead")[i].find("tbody").findAll("tr")
        for row in rows:
            format=row.find("td",class_="cb-col-8").text
            print(format,end="\t")
            f.write(format)
            f.write("\t\t")
            score=row.findAll("td",class_="text-right")
            for s in score:
                print(s.text,end="\t")
                f.write(s.text)
                if(len(s.text)==6):
                    f.write("\t")
                else:
                    f.write("\t\t")
            print("\n")
            f.write("\n\n")
        
        print("\n")
        f.write("\n")

    f.close()    
except Exception as e:
    print(e)