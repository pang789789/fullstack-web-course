# Chapter 08 학습 기록

## API Contract

### PATCH /members/{member_id}

- 전달한 필드만 부분 수정
- 필드 생략 허용
- 명시적 `null`은 허용하지 않음
- 빈 요청 `{}`: `400 Bad Request`
- 회원 없음: `404 Not Found`
- 이메일 중복: `409 Conflict`
- 입력값 오류 또는 명시적 `null`: `422 Unprocessable Entity`

## STEP 01. 실제 전달된 필드만 추출

- `member.model_dump(exclude_unset=True)` 사용
- 빈 변경 내용은 `400`으로 처리

## STEP 02. 이메일 중복 검사

- PATCH에 `email`이 포함된 경우에만 중복 확인
- 자기 자신의 ID는 중복 검사에서 제외
- 중복이면 `409 Conflict`

## STEP 03. 허용한 컬럼만 동적으로 UPDATE

- 컬럼명은 `allowed_fields`에서만 선택
- 사용자 입력값은 `%s` Parameter로 전달
- `RETURNING id, name, email, age`로 수정 결과 반환

## STEP 04. PATCH Endpoint

- `PATCH /members/{member_id}` 구현
- 회원 존재 여부 확인
- 전달된 필드만 수정
- 성공 후 `commit()` 실행

## STEP 05. 수정 결과 조회

- `GET /members/{member_id}` 구현
- PATCH 응답과 PostgreSQL 조회 결과가 같은지 확인
- 회원이 없으면 `404 Not Found` 반환
