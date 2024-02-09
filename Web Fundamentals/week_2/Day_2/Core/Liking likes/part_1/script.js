var count = 3;

function addLikes(){
    var likesNumber = document.querySelector(".likes")
    console.log(likesNumber);
    console.log(count)
    count++
    likesNumber.innerText = count + " like(s)"
    
}