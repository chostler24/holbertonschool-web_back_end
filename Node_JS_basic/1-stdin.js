// 1-stdin.js module

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('readable', () => {
  const input = process.stdin.read();

  if (input) {
    process.stdout.write(`Your name is: ${input}\n`);
  }
});

process.stdin.on('end', () => {
  process.stdin.write('This important software is now closing\n');
});
