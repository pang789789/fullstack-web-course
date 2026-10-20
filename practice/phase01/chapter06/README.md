# Chapter 06 학습 기록

## Flexbox를 사용한 영역과 이유

Header의 제목과 메뉴, 검색·필터 영역, 카드 내부 버튼 영역에 Flexbox를 사용했다. 이 영역들은 요소를 한 방향으로 나란히 배치하고 간격 및 정렬을 조절하는 구조이기 때문이다.

## Grid를 사용한 영역과 이유

회원 카드와 Dashboard 과정 카드 목록에 Grid를 사용했다. 여러 카드를 행과 열로 배치하고 같은 너비와 일정한 간격을 유지하기에 적합하기 때문이다.

## 가장 이해하기 어려웠던 속성

`justify-content`와 `align-items`의 기준이 처음에는 어려웠다. 두 속성을 가로와 세로로 외우는 대신 Main Axis와 Cross Axis를 기준으로 이해해야 하며, `flex-direction`이 바뀌면 축도 함께 바뀐다는 점을 확인했다.

## LLM에게 질문한 내용

Flexbox와 Grid의 선택 기준, Header와 Toolbar 구성 방법, 회원 카드에 3열 Grid를 적용하는 방법을 질문했다.

## LLM 답변을 검증하거나 수정한 내용

브라우저와 DevTools에서 `.site-header`, `.toolbar`, `.member-grid`, `.card-actions`를 확인했다. 또한 `grid-template-columns`를 `repeat(3, 1fr)`, `repeat(2, 1fr)`, `1fr`로 바꾸어 3열, 2열, 1열 배치를 확인한 뒤 최종 코드는 3열로 복원했다.
