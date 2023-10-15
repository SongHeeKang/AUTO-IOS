# 구조
- 테스트 프레임워크 : Appium
- BDD : behave
- 디자인패턴 : PageObject
- Report : allure

# 사전설치 1. Apppium
1. Appium 설치 및 실행
- http://appium.io/docs/en/2.1/quickstart/install/ 참고

2. Appium Driver 설치
```
#Install
npm i --location=global appium
appium driver install uiautomator2
appium driver install xcuitest
#Run
appium --base-path /wd/hub
```
# 사전설치 2 pip
```
pip install -r requirements.txt
```

# 실행
- behave를 통해서 실행해준다.

```
 sh run-behave.sh 
```


# 리포트 보기
- 리포트는 allure 리포트를 통해서 본다.
```
sh view-allure-report.sh
```

# 파일구조
├── apps : apk,ipa 파일위치
├── base : appium Element 관련 파일들
│   └── BasePage.py
├── features : bahave 관련 파일들 *.feature BDD 형식
│   ├── MainFormTest.feature
│   ├── environment.py : bahave 가 실행되기전과 후에 Appium 을 구동시켜주는 파일
│   └── steps
│       └── Livness.py
├── pages : 페이지별 화면기능에 대한 파일들 Appium 화면정의 들을 지정해논 파일
│   ├── IdCardPage.py : 신분증확인페이지
│   ├── LivenessPage.py 라이브니스 페이지
│   ├── MainPage.py  : 메인페이지
│   └── elements.py  : 각페이지의 Xpath, class, Accessbility id 값들을 모아놓은 파일
├── reports : 리포트 위치 allure, 및 실행레코딩파일워치(mp4), 실패시 png 파일 생성 된파일
    ├──allureReports
        ├──*.json
    ├──*.mp4
    ├──*.png
├── utilities : 유틸위치(로그)
    └── CustomLogger.py : 로그생성용 python 파일
├── requirements.txt : python pip 패키지
├── run-appium.sh : appium 실행 파일
├── run-behave.sh : behave 실행 파일
├── run-allure.sh : allure 생성 파일
