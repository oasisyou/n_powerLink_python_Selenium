from selenium import webdriver
import time


f = open('C:/Users/AE51/Desktop/바이너리큐브/pythonProject1/buk_crawling/검색키워드.txt', 'r', encoding='UTF8')

options = webdriver.ChromeOptions()
options.add_argument('headless')  # 웹 브라우저를 띄우지 않는 headlss chrome 옵션 적용
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')  # GPU 사용 안함
options.add_argument('lang=ko_KR')    # 언어 설정

lis=[]
while True:
    line = f.readline()
    if not line: break
    # print(line)
    lis.append(line.rstrip())
print(lis)
f.close()

# print(len(lis))

findList = []
test=[]
list = len(lis)
print("lis 길이 : ", list)

subs = input('찾은 단어를 정확히(대소문자) 입력하세요 : ')

for i in range(0, list):
    write_ranking = open('C:/Users/AE51/Desktop/바이너리큐브/pythonProject1/buk_crawling/검색키워드_결과.txt', 'a', encoding='UTF8')#r 읽기, w 쓰기, a 추가
    data = f"\n{lis[i]}\n"#해결하였음.
    write_ranking.write(str(data))
    print("지금 검색된 키워드에서 입력한 단어를 찾을 것입니다 : ", lis[i])
   
    driver = webdriver.Chrome('C:/Users/AE51/Downloads/chromedriver.exe', options=options)

    #M
    driver.get('https://m.ad.search.naver.com/search.naver?sm=&where=m_expd&query=')
    driver.implicitly_wait(2)

    driver.find_element_by_id("query").send_keys(lis[i])

    driver.find_element_by_xpath('//*[@id="search"]/button').click()
    driver.implicitly_wait(2)

    #파워링크 끝까지 롤
    roll = 15
    roll_txt = driver.find_element_by_xpath('//*[@id="_total_count"]')
    roll_txt_range = int(roll_txt.text)
    print("롤되기 전 보여지는 파워링크 갯수 : ", roll_txt_range)
    roll_list=[]
    if 15<=roll_txt_range:#페이지 롤할 크기가 15이상이면 밑에 실행
        for n in range(roll_txt_range):
            if n % roll == 0:
                # print(len(n))
                roll_list.append(n)#15번씩 페이지 몇번 로드 되는지 확인을 위해 배열에 append
        roll_count=len(roll_list)#배열의 길이만큼 for문 반복을 위해 변수 설정
        print('배열의 길이 roll_count : ', roll_count)

        for z in range(roll_count-1):#15개는 기본적으로 보여지기 때문에 -1을 해야 for문 roll되는 것이 같아짐
            r=driver.find_element_by_xpath('//*[@id="_get_more"]').click()
            # test.append(r).
            # print('롤 몇번 클릭하는지 click : ', roll_count)
            driver.implicitly_wait(0.3)#페이지 로드되는 시간 때문에 0.3초동안 대기
    # print(test)
    roll_end_txt = driver.find_element_by_xpath('//*[@id="_total_count"]')
    time.sleep(1)#페이지 로드되는 시간 때문에 1초동안 대기
    roll_end_txt_range = int(roll_end_txt.text)
    print("롤 끝까지 됐을 때 파워링크 길이 (roll_end_txt_range) : ", roll_end_txt_range)

    t=1
    for q in range(t,roll_end_txt_range+1):
        # print(q)
        goIn = driver.find_element_by_xpath(f'//*[@id="contentsList"]/li[{q}]')
        # print(goIn.text.split('\n'))
        t = str(goIn.text.split('\n'))#[0]제목만 긁어옴
        findList.append(t)
    print('findList : ', findList)

    for index, text in enumerate(findList):
        # print(index+1)
        # print(text)
        if subs in text:
            #순위 검색
            print("검색된 순위 : ", index + 1, text)
            data2 = f"{index+1}\t" + f"{text}\n"
            write_ranking.write(str(data2))

    #배열초기화
    write_ranking.close()
    del findList[:]
    del test[:]
