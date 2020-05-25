class Animal{
    //ここに処理を記載
    constructor(name,age,type){
        //ここにプロパティを定義する
        this.name = name;
        this.age = age;
        this.type = type;
    }
    getName(){
        return this.name;
    }
}

// let dog = new Animal("犬",8,"チワワ");
// console.log(dog);

let dog = new Animal("犬");
alert(dog.getName());