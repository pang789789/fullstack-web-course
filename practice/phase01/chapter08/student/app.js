// 1. HTML 요소 선택하기
// querySelector는 CSS 선택자에 해당하는 첫 번째 HTML 요소를 가져옵니다.
const firstNumberInput = document.querySelector('#firstNumber');
const secondNumberInput = document.querySelector('#secondNumber');
const operatorSelect = document.querySelector('#operator');
const calculateButton = document.querySelector('#calculateButton');

// 사칙연산만 담당하는 함수입니다.
// 화면 요소와 분리하면 같은 입력에 같은 결과가 나오는지 쉽게 테스트할 수 있습니다.
function calculate(firstNumber, secondNumber, operator) {
    if (operator === '+') {
        return firstNumber + secondNumber;
    }

    if (operator === '-') {
        return firstNumber - secondNumber;
    }

    if (operator === '*') {
        return firstNumber * secondNumber;
    }

    if (operator === '/') {
        if (secondNumber === 0) {
            throw new Error('0으로 나눌 수 없습니다.');
        }

        return firstNumber / secondNumber;
    }

    throw new Error('지원하지 않는 연산자입니다.');
}

// 2. 계산 버튼의 클릭 이벤트 처리하기
calculateButton.addEventListener('click', () => {
    // input.value는 항상 문자열입니다.
    // trim()으로 입력값 앞뒤의 불필요한 공백을 제거합니다.
    const firstValue = firstNumberInput.value.trim();
    const secondValue = secondNumberInput.value.trim();

    // 3. 빈 값 검사
    // 하나라도 비어 있으면 안내하고 return으로 함수를 즉시 종료합니다.
    if (firstValue === '' || secondValue === '') {
        alert('두 숫자를 모두 입력해 주세요.');
        return;
    }

    // 4. 문자열을 Number 자료형으로 변환
    const firstNumber = Number(firstValue);
    const secondNumber = Number(secondValue);

    // Number.isNaN()으로 숫자 변환에 실패했는지 확인합니다.
    if (Number.isNaN(firstNumber) || Number.isNaN(secondNumber)) {
        alert('숫자만 입력해 주세요.');
        return;
    }

    // 5. 사용자가 선택한 연산자 가져오기
    const operator = operatorSelect.value;

    try {
        // 6. 계산 함수를 실행하고 반환된 결과를 저장
        const result = calculate(firstNumber, secondNumber, operator);

        // 7. Template Literal을 사용해 계산 결과 출력
        alert(`계산 결과: ${result}`);
    } catch (error) {
        // 0으로 나누기처럼 계산할 수 없는 경우의 오류 메시지를 표시합니다.
        alert(error.message);
    }
});
