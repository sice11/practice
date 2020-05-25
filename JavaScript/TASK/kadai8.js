//課題1
class Animal {
    constructor(name,age){
        this.name = name;
        this.age = age;
    }
}

class Cats extends Animal {
    constructor(name,age,type){
        super(name,age);
        this.type = type;
    }
}
// let cats = new Cats("シャム",2,"猫");
// console.log(cats);

//課題2
class Cats2 extends Cats {
    constructor(name,age,type,speak){
        super(name,age,type);
        this.speak = speak;
    }
}
let cats2 = new Cats2("シャム",2,"猫","にゃーん！");
console.log(cats2.name + "が" + cats2.speak + "と鳴きました。");


//以下実験
// class Animal {
//     constructor(name,age){
//         this.name = name;
//         this.age = age;
//     }
// }

// class Cats extends Animal {
//     constructor(name,age,type){
//         super(name,age);
//         this.type = type;
//         this.speak = speak;
//     }
// }
// let cats2 = new Cats("シャム",2,"猫","にゃーん！");
// console.log(cats2.name + "が" + cats2.speak + "と鳴きました。");
