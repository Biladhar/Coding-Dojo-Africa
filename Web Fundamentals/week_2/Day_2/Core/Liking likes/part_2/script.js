var countlikes = [3,12,9]

function addLikes(element){
    if(element == document.querySelector(".btn1")){
        var likesNumber = document.querySelector(".likes1");
        var i= 0;
        countlikes[i]++;
        likesNumber.innerText = countlikes[i] + " like(s)";
    }else if(element == document.querySelector(".btn2")){
        var likesNumber = document.querySelector(".likes2");
        var i = 1
        countlikes[i]++
        likesNumber.innerText = countlikes[i] + " like(s)";
    }else{
        var likesNumber = document.querySelector(".likes3");
        var i = 2
        countlikes[i]++
        likesNumber.innerText = countlikes[i] + " like(s)";
    }
    
}

