// let myObj = {
//     name : "太郎",
//     age : 30 ,
//     area : "東京都"
// };

// alert(myObj.name);
// alert(myObj.age);
// alert(myObj.area);

// myObj.name = "花子";
// myObj.age = 20;
// //myObj.ageを削除
// delete myObj.age;
// alert(myObj.name);
// alert(myObj.age);

// myObj.speak = "こんにちは。";
// alert(myObj.speak);


// let myObj = {
//     name : "太郎",
//     getName : function(){
//         return this.name;
//         //thisは自分自身のことを表している。
//         //ここではmyObjをさしている。
//     }
// }
// alert(myObj.getName());

// let myObj = {
//     getThis1 : function() {return this},
//     getThis2 : () => this
// };
// alert(myObj.getThis1());
// alert(myObj.getThis2());

let myObj = {
    name : "太郎",
    age : 30,
    area : "Tokyo",
    tell : "090-1231-1234"
}
console.log(Object.keys(myObj));