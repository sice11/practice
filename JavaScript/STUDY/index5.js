let state = true;
while(state){
    let random = Math.floor(Math.random()*10);
    if(random === 3) state = false;
    console.log(random);
}