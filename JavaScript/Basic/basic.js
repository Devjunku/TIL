// ; 사용안해도 된다고 js 창시자가 말했으니 이걸 따르는 걸로?
// const는 재선언, 재할당이 불가능함.
// let은 재선언은 불가능, 재할당은 가능
// var는 둘 다 가능하지만, 호이스팅 되는 성질 때문에
// 되도록 사용 X

// 템플릿 리터럴 파이썬의 f string과 같은 역할을 암

// js에서 boolean 타입의 문자는 모두 소문자로 표현됨.

// switch 예시
const numOne = 10
const numTwo = 100
const operator = '+'

switch (operator) {
  case '+': {
    console.log(numOne + numTwo)
    break
  }
  case '-': {
    console.log(numOne - numTwo)
    break
  }
  case '*': {
    console.log(numOne * numTwo)
    break
  }
  case '/': {
    console.log(numOne / numTwo)
    break
  }
  default: {
    console.log('유효하지 않은 연산자입니다.')
  }
}
// break가 없으면 default는 무조건 실행됨.

// while, for등 일반적으로 알고 있는 루핑 표현식이 있고
// 세부적으로

// for of, for in 이 있음,
// for of의 경우 배열을 순회하는데 좋고(대괄호로 시작하면 배열이고)
// for in의 경우 객체를 순회하는데 좋음(중괄호로 시작하면 객체임) 사실 파이썬의 딕셔너리가 더 알맞는듯..

// 서로의 역할을 잊지 말것..

// 함수의 경우 선언식과 표현식이 있는데,
// 선언식은 꼭 함수의 이름이 필요 그니까 이런식으로

// 1
function isValid (word) {
	if (word.length >= 8) {
		return true
	} else {
		return false
	}
}
// 위 함수는 =와 같이 할당을 하지 않았지만, isValid를 함수라고 선언한것
// 함수 표현식은 그렇지 않음

/*
	[화살표 함수 연습]
	
	- 아래 celsiusToFahrenheit 함수는 섭씨 온도를 화씨 온도로 바꾸는 함수를 작성해주세요.
  - 선언식으로 작성된 함수를 "화살표 함수"로 다시 작성바랍니다.
	
  function celsiusToFahrenheit (celsius) {
		const fahrenheit = celsius * 9/5 + 32
		return fahrenheit
	}

*/

// fahrenheit를 따로 선언하지 않아도 결과값 산출 가능
function celsiusToFahrenheit (celsius) {
	// const fahrenheit = celsius * 9/5 + 32
	return celsius * 9/5 + 32
}

// 1단계
// function 생략가능
const celsiusToFahrenheit = (celsius) => {
	const fahrenheit = celsius * 9/5 + 32
	return fahrenheit
}

// 2단계
// parameter가 하나인 경우 괄호 생략 가능
const celsiusToFahrenheit = celsius => {
	const fahrenheit = celsius * 9/5 + 32
	return fahrenheit
}

// 3단계
// 몽통이 표현식 하나면 {}도 생략가능
const celsiusToFahrenheit = celsius => celsius * 9/5 + 32


// null은 항상 거짓이기 때문에
// 이를 활용하여 새로운 배열을 만들 수 있음.

// 예를 들어서 주어진 배열의 요소 중 null 값을 제거한 새로운 배열을 만들어야할 경우
// 아래와 같이 작성하면 됨
const examples = ['david.zip', null, 'maria.zip', 'tom.zip', null]
const res = []

for (const example of examples) {
  if (example) {
    res.push(example)
  }
}

console.log(res)

// find 메서드 예시
//  주어진 accounts 배열에서 balance가 24,000인 사람을 찾으세요.

const accounts = [
	{ name: 'justin', balance: 1200 },
	{ name: 'harry', balance: 50000 },
	{ name: 'jason', balance: 24000 },
]

const result = accounts.find((account) => {
  return account.balance === 24000
})

// some 메서드 예시
// 주어진 requests 배열에서 status가 pending인 요청이 있는지 확인하세요.

const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' },
]

const isPending = requests.some((request) => {
  return request.status === 'pending'
})

console.log(isPending)


// evey 메서드 예시
// 주어진 users 배열을 통해 모든 유저의 상태가 submmited인지 여부를 확인하세요.

const users = [
  { name: 'Harry', submitted: true },
  { name: 'Eric', submitted: true },
  { name: 'Tony', submitted: false },
]

const isSubmmited = users.every((user) => {
  return user.submitted === true
})

console.log(isSubmmited)