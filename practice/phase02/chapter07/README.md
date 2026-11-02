# Chapter 07 학습 기록

## STEP 01. Pydantic Model 준비

- `MemberCreate`: 클라이언트 입력 계약
- `MemberResponse`: DB가 생성한 `id`를 포함하는 출력 계약

## STEP 02. 중복 이메일 확인

- `find_member_by_email(cursor, email)`로 기존 회원을 조회
- 사용자 입력을 SQL 문자열에 직접 합치지 않고 `%s` parameter 사용
- `check_duplicate_email()`에서 DB 연결과 조회 수행
- `validate_duplicate_email()`에서 조회 결과가 있으면 `409 Conflict` 발생

## STEP 03. INSERT SQL 작성

- `insert_member(cursor, name, email, age)`에서 회원 추가 SQL 실행
- `%s` placeholder와 값 tuple을 분리한 parameterized query 사용
- `RETURNING id, name, email, age`로 생성된 row를 받을 준비
- `main.py`의 `create_member(member)`에서 모델 값을 INSERT 함수에 전달
- 생성된 row를 dict로 변환하여 반환

## STEP 04. 생성된 row 받기

- `RETURNING id, name, email, age`의 결과를 `cursor.fetchone()`으로 받음
- 반환 tuple을 `row` 변수에 저장
- `row[0]`부터 `row[3]`까지 응답용 dict로 변환
- 실제 확인 결과: `(3, '홍길동', 'hong@example.com', 27)`

## STEP 05. commit 하기

- INSERT와 `fetchone()` 성공 후 `conn.commit()` 실행
- 오류가 발생하면 `conn.rollback()` 실행
- `finally`에서 connection 종료

## STEP 06. FastAPI Endpoint 만들기

- `POST /members`
- `response_model=MemberResponse`
- 성공 상태 코드 `201 Created`

## STEP 07. 정상 요청 실행

- Swagger/TestClient에서 정상 회원 등록 요청 실행
- 상태 코드와 생성된 `id` 확인
- 검증 결과: `201 Created`, 생성된 `id=4`

## STEP 08. DB에서 직접 확인

- API 응답과 `members` 테이블의 실제 row 비교
- 확인된 row: `(4, 'Swagger Test', 'step07@example.com', 30)`

## STEP 09. 409 Conflict 테스트

- 같은 이메일로 다시 POST
- `409 Conflict`와 오류 메시지 확인
- 중복 요청 후 DB row 수가 증가하지 않는지 확인
- 검증 결과: 중복 요청 `409`, row 수 `4 → 4`

## STEP 10. 422 Validation 테스트

- 잘못된 이메일 `not-email`로 POST 요청
- Pydantic `EmailStr` 검증에서 `422 Unprocessable Entity` 확인
- 요청 전후 DB row 수를 비교하여 INSERT 미실행 확인
- 검증 결과: 상태 코드 `422`, row 수 `4 → 4`

## 다음 단계

rollback 직접 확인
