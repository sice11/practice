//7章の課題の復習

let hero = {
    name:"Tarou",
    HP:30,
    attack:function atPoint(){
        return Math.floor(Math.random()*10);
    }
}

let enemy = {
    name:"スライム",
    HP:15
}


let command = prompt(enemy.name + "が現れた！　【1】攻撃　【2】逃げる")
if (command == String(1)|| command == "1"){
    console.log(hero.name + "が" + enemy.name + "に" + hero.attack() +　"の攻撃");
}else if(command == String(2)||command == "2"){
    console.log(hero.name + "は逃げた。");
}
