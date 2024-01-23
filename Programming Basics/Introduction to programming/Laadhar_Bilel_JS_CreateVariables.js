var riderAge;
// to have a ride must be >=10 
var riderHeight;
// to have a ride must be >=42

if (riderHeight >= 42) {
    console.log("Get on that ride, kiddo!")
}
else {
    console.log("Sorry kiddo. Maybe next year.")
}

//Stretch Feature 1
if (riderHeight >= 42 && riderAge >= 10) {
    console.log("Get on that ride, kiddo!")
}
else {
    console.log("Sorry kiddo. Maybe next year.")
}

//Stretch Feature 2
if (riderHeight >= 42 || riderAge >= 10) {
    console.log("Get on that ride, kiddo!")
}
else {
    console.log("Sorry kiddo. Maybe next year.")
}