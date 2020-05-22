//入力されるドルを定義
//const intoDollar;
//入力欄
//command = prompt("ここにドルを入力してください")

//1ドル108円で計算
//const getYen = (number) => {
//    return number/108;
//}
//console.log(getYen(intoDollar));

//以下回答
const Dollar = 108;
const getYenToDollar = (number) => {
    return number * Dollar;
}

while(true) {
  const money = prompt('ドルから円に換算します');

  if(money) {

    console.log(getYenToDollar(money) + '円です');

  } else break;
}


