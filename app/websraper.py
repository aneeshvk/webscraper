import requests
from bs4 import BeautifulSoup


def webSraping(website_url,e1,a1,v1,e2,a2,v2):
#website_url='https://infopark.in/companies/jobs'
    out_file=open("results.txt","w")
    result=""
    #res=requests.get('https://infopark.in/companies/jobs', verify=False)
    res=requests.get(website_url, verify=False)
    soup=BeautifulSoup(res.text,'lxml')
    #jobs=soup.find_all('div',{"class":"row company-list joblist"})
    jobs=soup.find_all(e1,{a1:v1})
    for job in jobs:
        title_element=job.find("a")
        title=title_element.text
        link=title_element["href"]
        #job_company=job.find('div',{"class":"col-xs-6 col-md-4 mt5 jobs-comp-name text-center"}).text
        job_company = job.find(e2, {a2: v2}).text
        result+=job_company+" "
        #compny_name=job_company.find("a")
        out_file.write(title+"\n"+job_company+" ")
        #print( job_company)
    return(result)
