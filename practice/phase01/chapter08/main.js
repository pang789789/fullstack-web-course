// 2. JavaScript 콘솔 출력 실습
console.log('Hello JavaScript');

// 3. 변수 - 값에 이름을 붙이기
const memberName = '홍길동'; // 값을 다시 할당하지 않을 때 (상수)
let age = 25;               // 값이 이후 변경될 수 있을 때 (변수)

console.log(memberName);
console.log(age);

// let으로 선언된 변수 값 변경해보기
let memberCount = 3;
console.log('초기 회원 수:', memberCount);

memberCount = 4; // 값이 변경될 수 있으므로 재할당 가능
console.log('변경된 회원 수:', memberCount);

// 참고: const는 아래와 같이 다시 값을 넣으려고 하면 에러가 발생합니다.
// const courseName = 'Frontend Basic';
// courseName = 'Backend Basic'; // TypeError
