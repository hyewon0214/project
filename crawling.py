from bs4 import BeautifulSoup
import urllib.request
response=urllib.request.urlopen('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo&year=2020')
soup=BeautifulSoup(response,'html.parser')
data=[]
for tr_tag in soup.find(id='regularTeamRecordList_table').find_all('tr'):
    th_tag=tr_tag.find('th')
    strong_tag=th_tag.find('strong')
    lank=strong_tag.get_text()

    span_tag=tr_tag.findAll('span')
    team=span_tag[0].get_text()
    total=span_tag[1].get_text()
    win=span_tag[2].get_text()
    lose=span_tag[3].get_text()
    draw=span_tag[4].get_text()
    #data.append([team,lank,win,lose,draw])
    data.append([team,win,lose,draw])
print(data)

with open('baseball.csv','w') as file:
    file.write('team,win,lose,draw\n')
    for i in data:
        file.write('{0},{1},{2},{3}\n'.format(i[0],i[1],i[2],i[3]))
    file.close()
