//-------predict 1 --------------------
function myBirthYearFunc(){
    console.log("I was born in" + 1980);
}
myBirthYearFunc();
// I was born in 1980


//---------presict 2---------------------

function myBirthYearFunc(birthYearInput){
    console.log("I was born in" + birthYearInput);
}
myBirthYearFunc(1980);

// I was born in1980

//----------- predict 3----------------------

function add(num1, num2){
    console.log("Summing Numbers!");
    console.log("num1 is: " + num1);
    console.log("num2 is: " + num2);
    var sum = num1 + num2;
    console.log(sum);
}
add(10, 20);
// summing Numbers!
// num 1 is 10
// num 2 is 20
// 30