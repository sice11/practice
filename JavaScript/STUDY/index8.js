// class Animal{
//     //ここに処理を記載
//     constructor(name,age,type){
//         //ここにプロパティを定義する
//         this.name = name;
//         this.age = age;
//         this.type = type;
//     }
//     getName(){
//         return this.name;
//     }
// }

// let dog = new Animal("犬",8,"チワワ");
// console.log(dog);

// let dog = new Animal("犬");
// alert(dog.getName());


//継承 extendsを付与することでできる。
class Character {
    constructor(name,hp){
        this.name = name,
        this.hp = hp;
    }
    attack(){
        console.log(this.name + "の攻撃！");
    }
}

class Hero extends Character{
    // control(){}
    // superAttach(){}
    // speak(){}
    constructor(name,hp,exp){
        //superで継承元のプロパティを呼び出している
        super(name,hp);
        this.exp = exp;
    }
}

class Enemy extends Character{
    dropItem(){}
    getPoint(){}
}

let hero = new Hero("主人公",100,10);
console.log(hero);
// let enemy = new Enemy("敵",10);

// hero.attack();
// enemy.attack();