// Print odds 1-20

var i = 1;
while(i<=20){
    if (i % 2 !=0){
        console.log(i)
        i++;
    }
    else{
        i++;
    }
}

// Decreasing Multiples of 3

var i = 100;
while(i >= 0){
    if (i % 2 ==0 && i % 3 == 0){
        console.log(i)
        i--;
    }else{
        i--;
    }
}

// Print the sequence

var arr=[4, 2.5, 1, -0.5, -2, -3.5];
var i=0;
while(i<arr.length){
    console.log(arr[i])
    i++
}

//Sigma

var sum = 0;
var i = 1 ;
while(i <= 100){
    sum = sum + i;
    i++
}
console.log(sum);


// Factorial

var product = 1;
var i = 1 ;
while(i <= 12){
    product = product * i;
    i++
}
console.log(product);
