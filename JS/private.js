
const app = (function() {
	let privateValue = 'privateValue';
	return {
		props: privateValue,
	}
}());

console.log(app.props);

const app2 = function() {
	let privateValue = 'privateValue2';
	return {
		props: privateValue,
	}
};

console.log(app2().props);