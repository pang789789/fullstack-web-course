// Chapter 08 과제: 회원 이용 가능 여부 판별하기

// 회원 이름과 나이를 같은 순서로 저장합니다.
const memberNames = ['홍길동', '김영희', '이철수', '박민지', '최준호'];
const memberAges = [25, 19, 32, 17, 21];

// 모든 회원을 순서대로 반복합니다.
for (let i = 0; i < memberNames.length; i++) {
    const name = memberNames[i];
    const age = memberAges[i];

    // 나이가 20세 이상인지 조건문으로 판단합니다.
    const ageGroup = age >= 20 ? '성인' : '미성년';

    // Template Literal로 번호, 이름, 나이, 판별 결과를 한 문장으로 출력합니다.
    console.log(`${i + 1}. ${name} - ${age}세 - ${ageGroup}`);
}

// 배열의 length 속성으로 전체 회원 수를 출력합니다.
console.log(`전체 회원 수: ${memberNames.length}`);
