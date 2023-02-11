
const outputText = document.querySelector(".text-output");
const outputLabel = document.querySelector("#label-output");

const escape = {
  8: '\\b',
  9: '\\t',
  10: '\\n',
  12: '\\f',
  13: '\\r',
  34: '\\"',
  47: '\\/',
  92: '\\\\',
};

const unescape = {
  'b': 8,
  't': 9,
  'n': 10,
  'f': 12,
  'r': 13,
  '"': 34,
  '/': 47,
  '\\': 92,
};

const escapeJSON = () => {
  let res = [];
  let str = document.querySelector(".text-input").value;
  for(let i = 0; i < str.length; ++i) {
    let charCode = str.charCodeAt(i);
    if (charCode in escape) {
      res.push(escape[charCode]);
    } else {
      res.push(str[i]);
    }
  }
  outputLabel.innerText = "Escaped string:"; 
  outputText.value = res.join('');
}

const unescapeJSON = () => {
  let res = [];
  let str = document.querySelector(".text-input").value;
  for(let i = 0; i < str.length; ++i) {
    let nextChar = str[i + 1];
    if (str[i] === '\\' && nextChar in unescape) {
      res.push(String.fromCharCode(unescape[nextChar]));
      ++i;
    } else {
      res.push(str[i]);
    }
  }
  outputLabel.innerText = "Unescaped string:";
  outputText.value = res.join('');
}
