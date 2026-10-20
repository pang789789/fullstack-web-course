// 사칙연산 계산 함수 자동 테스트
// Console에서 각 항목이 PASS로 출력되는지 확인합니다.

function test(name, actual, expected) {
    if (actual === expected) {
        console.log(`PASS: ${name}`);
    } else {
        console.error(`FAIL: ${name} / 예상값: ${expected}, 실제값: ${actual}`);
    }
}

console.group('계산기 테스트 결과');

test('10 + 5 = 15', calculate(10, 5, '+'), 15);
test('10 - 5 = 5', calculate(10, 5, '-'), 5);
test('10 * 5 = 50', calculate(10, 5, '*'), 50);
test('10 / 5 = 2', calculate(10, 5, '/'), 2);
test('음수 계산', calculate(-3, 2, '+'), -1);
test('소수 계산', calculate(1.5, 2, '*'), 3);

// 0으로 나눌 때 오류가 발생하는지 확인합니다.
try {
    calculate(10, 0, '/');
    console.error('FAIL: 0으로 나누기 오류가 발생하지 않았습니다.');
} catch (error) {
    console.log(`PASS: ${error.message}`);
}

console.groupEnd();
