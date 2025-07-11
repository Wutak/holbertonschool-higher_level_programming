#!/usr/bin/node
const lines = [
	'C is fun',
	'Python is cool',
	'JavaScript is amazing',
];
let nb = '';
let i = 0;
while (i < lines.length){
	nb += lines[i];
	if (i !== lines.length - 1){
		result += '\n';
	}
	i++;
}
console.log(nb);
