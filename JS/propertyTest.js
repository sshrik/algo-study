let a = 3;
function foo() {
    console.log(this);
	console.log(this.a);
}

const obj = {
	a: 2,
	foo: foo
}

obj.foo();

// 암시적 bind 는 이렇게 실행 주체가 바뀌면서 소실 될 수 있다.
const bar = obj.foo; 
bar(); // undefined가 출력됨
foo(); // 위와 동일한 결과

