#!/usr/bin/node
const lines = [
	'C is fun',
	'Python is cool',
	'JavaScript is amazing',
];

let result = '';
let i = 0;
while (i < lines.length) {
	result += lines[i];
	if (i !== lines.length - 1){
		result += '\n';
	}
	i++;
}

console.log(result);
