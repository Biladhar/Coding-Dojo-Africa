// we need fuction called howMuchleftOverCake.
// variable for number of pieces
// variable for numbers of people 
// to know how many pieces of cake remain we can use modulo 


// =============== Feature 1 ===================
function howMuchLeftOverCake(numberOfPieces,numberOfPeople){
    console.log("Number of pieces left " +numberOfPieces % numberOfPeople);
    return numberOfPieces % numberOfPeople;
}
howMuchLeftOverCake(12,5)

//================= Feature 2===================
function howMuchLeftOverCake2(numberOfPieces,numberOfPeople){
    var rest = numberOfPieces % numberOfPeople
    if(rest === 0){
        console.log("No leftovers for you!");
        return "No leftovers for you!";
    }
    else if(rest <=2 && rest !=0){
        console.log("You have some leftovers");
        return "You have some leftovers";
    }
    else if(rest >= 3 && rest <= 5){
        console.log("You have leftovers to share");
        return "You have leftovers to share";
    }
    else{
        console.log("Hold another party!");
        return "Hold another party!";
    }
}
howMuchLeftOverCake2(12,12)
howMuchLeftOverCake2(11,5)
howMuchLeftOverCake2(12,9)
howMuchLeftOverCake2(15,9)