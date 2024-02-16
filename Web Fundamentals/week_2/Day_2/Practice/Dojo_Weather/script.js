function removeCookies() {
    var x = document.querySelector(".footer");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function celToFar(cel){
    return Math.round (9 / 5 * cel + 32);
}

function farToCel(far){
    return Math.round (5 / 9 * (far-32)) ;
}

function convert(element){
    for(var i=1; i<9 ; i++){
        var temp = document.querySelector("#temp" + i);
        var tempVal = parseInt(temp.innerText);
        if(element.value== "°F"){
            temp.innerText = celToFar(tempVal);
        }
        else{
            temp.innerText = farToCel(tempVal);
        }
    }
}




