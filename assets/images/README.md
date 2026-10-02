# Course Image Assets

이 폴더는 `fullstack-web-course-instructor`의 강의안과 학생용 Public 교재에서 공통으로 사용하는 이미지 자산을 저장합니다.

## 폴더 구조

```text
assets/images/
├─ phase01/
│  └─ chapterXX/
├─ phase02/
│  └─ chapterXX/
└─ phase03/
   └─ chapterXX/
```

## 사용 규칙

- 이미지 파일명은 영문 소문자 kebab-case를 사용합니다.
- 강의별 이미지는 해당 phase/chapter 폴더에 저장합니다.
- Private instructor repository는 이 Public repository의 raw URL을 참조합니다.

예시:

```text
https://raw.githubusercontent.com/GilbertMoon/fullstack-web-course/main/assets/images/phase01/chapter12/http-request-response.png
```

강의안 Markdown 예시:

```md
![HTTP 요청/응답 흐름](https://raw.githubusercontent.com/GilbertMoon/fullstack-web-course/main/assets/images/phase01/chapter12/http-request-response.png)
```

이미지는 구조, 흐름, 상태 변화, 데이터 이동을 이해하기 위한 학습 자료로 사용합니다.

# Chapter 01 학습 기록

## Browser와 Web Server의 차이
Browser는 웹페이지를 실행하고 보여주는 곳이고,
Web Server는 HTML, CSS, JavaScript 파일을 제공한다.

## Web Server와 API Server의 차이
Web Server는 화면 파일을 제공하고,
API Server는 JSON 형태의 데이터와 기능을 제공한다.

## localhost를 내가 이해한 방식
localhost는 현재 내가 사용하고 있는 컴퓨터를 의미한다.

## Network 탭에서 확인한 GET 요청
Live Server로 index.html을 실행하고 브라우저 개발자 도구를 열었다.

## LLM에게 질문한 내용
Live Server와 Web Server의 역할에 대해 질문했다.

## 내가 직접 검증한 내용
127.0.0.1:5500 주소에서 index.html 페이지가 실행되는 것을 확인했다.