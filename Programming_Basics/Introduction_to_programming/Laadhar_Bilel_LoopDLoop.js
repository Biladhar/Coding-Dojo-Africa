//1. we need a loop because we have a reccurent task "give 1 candy every 2 miles" and an end condition " 6 miles".
//2. the starting point of the loop is a runner reaches 2 miles
//3. the loop should stop when a runner reaches 6 miles
//4. the loop will know when to stop when we reaches 6 miles
//5. for each iteration of the loop we increment by 1 miles
//6. we nned a variable for Miles




for(var miles=0 ; miles<= 6 ; miles++){
    if (miles % 2 === 0){
        if (miles != 0)
        console.log(miles + " miles nice joob , Take a cookie")
    }
}

//-------------------------------------------------------------------
for(var miles=0 ; miles<= 6 ; miles++){
    if (miles % 2 === 0){
        if (miles != 0)
        console.log(miles + " miles nice joob , Take a cookie")
    }
}

//-------------------------ninja bonus----------------------------------------
var miles;
var time;
for(miles = 0 , time = 0 ; miles <=6 ; miles++ , time++){
    var speed = miles / time
    if(miles % 2 && speed >= 5,5 ){
        if ( miles != 0)
        console.log(miles + " miles nice job , take a cookie")
    }
} 