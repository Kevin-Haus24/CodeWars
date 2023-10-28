function maxLenWithCondition(s) {
  s = s.replace(/O/g, 'N').replace(/P/g, 'N').replace(/ /g, '');
  if (s.length === 0) return 0;
  if (s === ' ') return 0;
  if (!s.match(/^[a-zA-Z]+$/)) return -1;
  while (s.includes('NN')) {
    s = s.replace('NN', 'N N');
  }
  const words = s.split(' ');
  const maxLength = Math.max(...words.map((c) => c.length));
  return maxLength;
}

function generateRandomString(fl = true, digit = true, space = false, length = 30, uppercase = true, specialChars = true) {
  let chars = '';
  if (uppercase) {
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  }
  if (specialChars) {
    chars += ' ';
  }
  if (digit) {
    chars += '0123456789';
  }
  if (space) {
    chars = ' ';
    length = 1;
  }
  let randomString = '';
  for (let i = 0; i < length; i++) {
    randomString += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return randomString;
}

for (let i = 0; i < 100; i++) {
  const digitFalse = new Array(10).fill(false);
  const digitTrue = [true];
  const spFalse = new Array(100).fill(false);
  const spTrue = [true];

  let digitiss = [...digitTrue, ...digitFalse];
  let sp = [...spFalse, ...spTrue];
  digitiss = digitiss[Math.floor(Math.random() * digitiss.length)];
  sp = sp[Math.floor(Math.random() * sp.length)];

  let random_string = generateRandomString(true, digitiss, sp);
  random_string = 'NOPN OPNO';
  console.log(random_string, maxLenWithCondition(random_string));
}