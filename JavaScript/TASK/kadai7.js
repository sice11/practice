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

// for (let enemyHP = 10; enemyHP<0; enemyHP-atPoint){
//     console.log(enemyHP);
// }


//回答
// 自キャラのオブジェクト
const hero = {
    name: '太郎',
    hp: 30,
    attack: function() {
      return Math.floor(Math.random() * 10)
    }
  }
  
  // 敵キャラのオブジェクト
  const enemy = {
    name: 'スライム',
    hp: 15
  };
  
  
  while(true) {
    const command = prompt(enemy.name + 'が現れた！（【1】攻撃　【2】逃げる）');
    
    // [攻撃]を選択した場合
    if(command === '1') {
      const attack = hero.attack();
      
      enemy.hp = enemy.hp - attack;
      console.log(hero.name + 'は敵に' + attack + 'のダメージを与えた！');
      if(enemy.hp <=0) {
        console.log('敵を倒した！');
        break;
      }
      console.log('敵の体力は残り' + enemy.hp + 'です');
  
    // [逃げる]を選択した場合
    } else if(command === '2') {
      
      console.log('無事に逃げました');
      break;
      
    }
  }
  
  console.log('ゲーム終了');