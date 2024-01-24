

function greetSomeone(name){
    console.log("good day " + name)
    return "good day " + name
}
greetSomeone("anakin")

//---------------level 1-----------------------------------
// with the help of walid Guetat

function greetSomeone(name,time){
    if(time >= 4 && time < 12){
        console.log("good morning " + name + " it's " + time + " o'clock" );
        return "good morning " + name + " it's " + time + " o'clock";
    }
    else if(time > 12 && time < 17){
        console.log("good afternoon " + name + " it's " + time + " o'clock" );
        return "good evening" + name + " it's " + time + " o'clock" 
    }
    else{
        console.log("good night " + name + " it's " + time + " o'clock" );
        return "good night" + name + " it's " + time + " o'clock" 
    }
}
greetSomeone("anakin",8)
greetSomeone("Obi one ",13)
greetSomeone("R2-D2 ",22)

//----------------- level 2--------------------------------

function greetSomeone(name,time){
    if(name === "count Dooku"){
        console.log("I'm coming for you, Dooku!");
        return "I'm coming for you, Dooku!"
    }
    else if(time >= 4 && time < 12){
        console.log("good morning " + name + " it's " + time + " o'clock" );
        return "good morning " + name + " it's " + time + " o'clock";
    }
    else if(time > 12 && time < 17){
        console.log("good afternoon " + name + " it's " + time + " o'clock" );
        return "good evening" + name + " it's " + time + " o'clock" 
    }
    else{
        console.log("good night " + name + " it's " + time + " o'clock" );
        return "good night" + name + " it's " + time + " o'clock" 
    }
}
// friends may the force be with them
greetSomeone("anakin",8)
greetSomeone("Obi one ",13)
greetSomeone("R2-D2 ",22)
// the dark side of the force
greetSomeone("count Dooku",5)