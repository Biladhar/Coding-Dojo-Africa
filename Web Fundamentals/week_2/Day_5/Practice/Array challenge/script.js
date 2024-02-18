// 1.Always Hungry

function alwaysHungry(arr) {
    var foundFood = false
    for(var i = 0 ; i < arr.length ; i++){
        if (arr[i] == "food"){
            console.log("yummy")  ; 
            foundFood = true ;
        }
    }
        if (foundFood == false) {
            console.log("I'm hungry");
        }
}

alwaysHungry([3.14, "food", "pie", true, "food"]);
// this should console log "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]);
// this should console log "I'm hungry"


// 2.High Pass Filter

function highPass(arr, cutoff) {
    var filteredArr = [];
    for(var i = 0 ; i < arr.length ; i++){
        if (arr[i]>cutoff){
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // we expect back [6, 8, 10, 9]


// 3.Better than average

function betterThanAverage(arr) {
    var sum = 0;
    for ( var i = 0 ; i < arr.length ; i++){
        sum += arr[i];
    }
    var average = sum / arr.length ;
    var count = 0;
    for(var j = 0 ; j < arr.length; j++){
        if(arr[j] > average){
            count++
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4

// 4. Array Reverse

function reverse(arr) {
    var j = arr.length-1 ;
    for(var i = 0 ; i<j ; i++){
        var temp = 0 ;
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp ;
        j--;
    }
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]


// 5.Fibonacci Array

function fibonacciArray(n) {
    var fibArr = [0, 1];
    while(fibArr.length < n){
        var num = fibArr[fibArr.length - 1] + fibArr[fibArr.length - 2];
        fibArr.push(num)
    }
    return fibArr;
}

var result = fibonacciArray(10);
console.log(result);


