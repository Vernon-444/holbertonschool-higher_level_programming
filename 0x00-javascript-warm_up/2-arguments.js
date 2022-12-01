#!/usr/bin/node
const args = process.args.length;

if (args === 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument founed');
} else {
  console.log('Arguments found');
}
