//必要な関数を設定
//敵の体力
// let enemyHP = 10;
//アタックポイント
let atPoint = Math.floor(Math.random()*10);

//攻撃するか、逃げるかを選択
// let command = prompt("[1]攻撃　[2]逃げる");
// if(command == String(1)||1){
//     let enemyHP1 = enemyHP - atPoint;
//     alert("敵の体力は残り" + enemyHP1 + "です。");
// }else{
//     alert("無事に逃げました。");
// }


//攻撃するか、逃げるかを選択
// let command = prompt("[1]攻撃　[2]逃げる");
// if(command == String(1)||1){
//     function enemyHP1(){
//         for (enemyHP - atPoint; enemyHP < 0;){
//             alert("敵の体力は残り" + enemyHP1() + "です。");
//         }
//     }
// }else{
//     alert("無事に逃げました。");
// }

for (let enemyHP = 10; enemyHP<0; enemyHP-atPoint){
    console.log(enemyHP);
}