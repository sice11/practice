//関数宣言
//function myFunc(){
    //処理内容
//}


function myFunc(){
    console.log("これは一番目の関数です。");
}
function myFunc(){
    console.log("これは二番目の関数です。");
}

myFunc();

//以下関数式
const myFunc2 = function(){
    console.log("これは1つ目の関数です。");
}
//以下の関数はエラーになる
//const myFunc2 = function(){
//    console.log("これは2つ目の関数です。");
//}

myFunc2();

//関数式を省略することができる
const myFunc3 = () => {
    console.log("アロー関数の実施")
}
myFunc3();


//myNumberを定義
const myNumber = 10;
//myNumberを二倍にするための式を記入
const getDouble = (number) => {
    console.log(number*2);
}
//結果（計算）
getDouble(myNumber);