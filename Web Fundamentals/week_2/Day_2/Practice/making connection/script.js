
console.log("hello")

var x = document.querySelector("#add");
var y = document.querySelector("#delete");
var one = document.querySelector("#one");
var two = document.querySelector("#two");

// change user name
var userName = document.querySelector("#name");
function changeUserName() {
    userName.innerText= "Cristiano Ronaldo";
}


function removeUser(element){
    x.innerText--;
    if(element.alt=="close1"){
        one.remove();
    }else{
        two.remove()
    }
}

var total = 500;

function acceptUsers(element){

    x.innerText--;
    total++;
    y.innerText = total + "+";
    console.log(total);
    if(element.alt=="accept1"){
        one.remove();
    }else{
        two.remove();
    }
    return total
}