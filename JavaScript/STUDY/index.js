const myString = ["リンゴ","メロン"]
myString.push('イチゴ');    // ['リンゴ', 'メロン', 'イチゴ']
myString.pop();            // ['リンゴ', 'メロン']
myString.unshift('イチゴ'); // ['イチゴ', 'リンゴ', 'メロン']
myString.shift();          // ['リンゴ', 'メロン']
console.log(myString)