[🌏노션 링크](https://inky-marten-9ff.notion.site/Finest-2946ce6ba07942db88e13ac40a60de0f?pvs=4)

[🏷Figma 링크](https://www.figma.com/community/file/1375370963988360217/finest)

# Finest
SSAFY 11기 1학기 관통 프로젝트

<br>



## I. ✨ 프로젝트 개요

🗓️ 진행기간 : 2024.05.08(수) ~ 2024.05.23(목)

👑 서비스명 : Finest

🎯 주제 : 창업자들을 위한 커뮤니티 사이트

🌃 컨셉 및 기획의도

- 창업 커뮤니티로써 다양한 관련 정보들을 제공합니다.
- 회원 간 창업 관련 주요 정보 공유, 금융 관련 정보 공유를 권장합니다. 
- 창업지원 혹은 사업자지원 관련 주요 웹사이트는 10개 이상입니다. 이 모든 웹사이트들을 사업주가 일일이 찾아보기는 힘들것이라고 예상됩니다. 저희 Finest는 예비창업자 혹은 사업자분들이 발품파는 시간을 조금이라도 줄여주고자 합니다.
- ✅ 금융감독원 데이터를 활용한 예적금, 대출 금리 비교 조회 서비스 제공

- 💡 부동산 데이터를 활용한 임대료 및 권리금, 공실률 조회 서비스 제공

<br>
<hr style="border: 1px solid #ccc;">



## II. 👨‍👩‍👧‍👦 팀원 정보 및 업무 분담

<table>
  <tr>
    <td align="center" style="border: 1px solid #ccc;">
      <img src="https://github.com/qwert0175.png" width="100"><br>
      <hr style="width: 80%;">
      <a href="https://github.com/qwert0175">조성인</a>
    </td>
    <td align="center" style="border: 1px solid #ccc;">
      <img src="https://github.com/BigBeom.png" width="100" ><br>
      <hr style="width: 80%;">
      <a href="https://github.com/BigBeom" >박범준</a>
    </td>
  </tr>
</table>

<br>

👥 조성인
- Backend 
  - 환율 API 작성
    - 환율정보 DB 저장 및 조회
  - 금융상품 API 작성
    - 금융상품 정보 DB 저장 및 조회
  - 상품 추천 알고리즘 작성
    - 사용자의 동일 연령대, 성별의 사람들이 많이 가입한 상품 표시

- Frontend
  - 메인 페이지 작성
  - 프로필 페이지 작성
    - 사용자 기본 정보
    - 가입 상품 금리 그래프
  - 환율계산기 기능 구현
  - 예적금 금리비교 페이지
    - 은행, 기간별 필터링
    - 기간별 금리순 정렬
  - 금융상품 상세보기 페이지 작성
    - 예적금 가입/탈퇴 처리 구현
  - 카카오지도 페이지 작성
    - 주변은행 찾기
    - 은행검색 기능
  - 추천상품 페이지 제작

- ETC
  - 최종 발표 프레젠테이션 검토 및 발표
  - ERD 설계 / DB 스키마 생성 및 수정

<br>

👥 박범준
- Backend
  - User API 작성
    - 커스터마이징 회원 가입 / 로그인 / 로그아웃
  - Board API 작성 
    - CRUD / 댓글 등록

- Frontend
  - 메인페이지 수정 및 보완
  - 프로필 페이지 수정 및 보완
  - 게시판 관련 페이지 작성
    - CRUD 페이지 작성
    - 커뮤니티 페이지 작성

- ETC
  - Notion, Readme 문서 작성 총괄
  - Figma 디자인 총괄
  - DB 스키마 생성 및 수정
  - 최종 발표 프레젠테이션 제작 및 수정 보완

<br>
<hr style="border: 1px solid #ccc;">



## III. 👩‍💻 일별 진행내용
|일자|내용|
|---|---|
|05-08|프로젝트 아이디어 구상|
|05-09|아이디어 구체화(필요 데이터 정리, 화면 구상) 및 ERD 작성|
|05-13|카카오맵 api를 사용한 은행 찾기 기능 구현|
|05-14|화면 목업 작성 및 홈페이지 이벤트 배너 추가, 지도 페이지 기능 구현|
|05-15|목업 업데이트 및 환율 정보 DB 저장, 환율 계산기 기능 구현|
|05-16|환율 계산기 편의성, 환율정보 저장 기능 업데이트 및 회원가입 기능 구현|
|05-17|회원가입 기능 수정, 지도 검색 기능 추가|
|05-18|금융 상품 정보 가져오기, 게시판CRUD 구현|
|05-19|예적금 금리 비교 페이지 생성, models 및 serializer 수정, 회원가입 이슈해결|
|05-20|로그인, 로그아웃, 회원정보수정 화면 구현|
|05-21|게시판 CR 화면 구현, 회원탈퇴 기능 구현|
|05-22|게시글 CRUD 디자인 및 댓글 CRUD 구현 완료, 커뮤니티 및 메인페이지 디자인 수정 |
|05-23||

<br>
<hr style="border: 1px solid #ccc;">



## IV. 💎 설계 내용 및 실제 구현 정도
 <table>
  <thead>
    <tr>
      <th>기능</th>
      <th>아쉬운점</th>
      <th>구현정도</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>메인 페이지</td>
      <td>배너 바로가기 링크</td>
      <td>⭐⭐⭐⭐</td>
    </tr>
    <tr style="background-color: #999;">
      <td>회원 커스터마이징</td>
      <td>비밀번호 변경, username과 nickname 분리</td>
      <td>⭐⭐⭐⭐</td>
    </tr>
    <tr>
      <td>예적금 금리 비교</td>
      <td>디자인</td>
      <td>⭐⭐⭐⭐⭐</td>
    </tr>
    <tr style="background-color: #999;">
      <td>환율 계산기</td>
      <td>국기 이미지</td>
      <td>⭐⭐⭐⭐⭐</td>
    </tr>
    <tr>
      <td>근처 은행 검색 (카카오맵)</td>
      <td>내위치 표시, infowindow ui</td>
      <td>⭐⭐⭐⭐</td>
    </tr>
    <tr style="background-color: #999;">
      <td>커뮤니티(게시판)</td>
      <td>카테고리별 페이지, 특정 게시글 상단 고정, Pagination</td>
      <td>⭐⭐⭐</td>
    </tr>
    <tr>
      <td>프로필 페이지</td>
      <td>프로필 이미지, 디자인</td>
      <td>⭐⭐⭐⭐</td>
    </tr>
    <tr style="background-color: #999;">
      <td>금융 상품 추천 알고리즘</td>
      <td>창의성</td>
      <td>⭐⭐⭐⭐</td>
    </tr>
        <tr>
      <td>임대료, 권리금, 공실률 조회 서비스</td>
      <td></td>
      <td>미구현</td>
    </tr>
  </tbody>
</table>

<br>
<hr style="border: 1px solid #ccc;">



## V. 🔑 ERD

![ERD](./ERD/Finest_ERD.png)

<br>
<hr style="border: 1px solid #ccc;">



## VI. 📑 금융 상품 추천 알고리즘 설명
- 시연영상 찍은 후 기능별로 이미지 넣고 설명작성

<br>
<hr style="border: 1px solid #ccc;">



## VII. 📑 서비스 대표 기능들 설명
- 시연영상 찍은 후 기능별로 이미지 넣고 설명작성

<br>
<hr style="border: 1px solid #ccc;">



## 📝 느낀점

### 조성인
- 

### 박범준
- 

<br>
<hr style="border: 1px solid #ccc;">



## 🛠 기술 스택

### Backend
![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)

### Frontend
![Vue.js](https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)
![HTML](https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### Database
![SQLite](https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

### Commnunication
![Git](https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white)
![Mattermost](https://img.shields.io/badge/Mattermost-0072C6?style=for-the-badge&logo=mattermost&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)

<br>
<hr style="border: 1px solid #ccc;">

## 📁 폴더 구조

[ BACK-END ]

[ FRONT-END ]

<br>
<hr style="border: 1px solid #ccc;">