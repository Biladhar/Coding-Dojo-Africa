// ! 1
// * given
console.log(hello);                                   
var hello = 'world';        
// * AFTER HOISTING BY THE INTERPRETER
var hello ;
console.log(hello);
hello = 'world';
// * outpout = undefined


// ! 2 
// * given
var needle = 'haystack';
test();
function test(){
    var needle = 'magnet';
    console.log(needle);
}
// * AFTER HOISTING BY THE INTERPRETER
var needle;
function test() {
var needle;
needle = 'magnet';
console.log(needle);
}
needle = 'haystack';
test();
// * Predicted Output:
// magnet


// ! 3 
// * given
var brendan = 'super cool';
function print(){
    brendan = 'only okay';
    console.log(brendan);
}
console.log(brendan);
// * AFTER HOISTING BY THE INTERPRETER
var brendan;
function print() {
    brendan = 'only okay';
    console.log(brendan);
}
brendan = 'super cool';
console.log(brendan);
// * Predicted Output:
//super cool


// ! 4 
// * given
var food = 'chicken';
console.log(food);
eat();
function eat(){
    food = 'half-chicken';
    console.log(food);
    var food = 'gone';
}
//* AFTER HOISTING BY THE INTERPRETER
var food;
function eat() {
var food;
food = 'half-chicken';
console.log(food);
food = 'gone';
}
food = 'chicken';
console.log(food);
eat();
// *Predicted Output:
// chicken
// half-chicken



// ! 5 
// * given
mean();
console.log(food);
var mean = function() {
    food = "chicken";
    console.log(food);
    var food = "fish";
    console.log(food);
}
console.log(food);
//* AFTER HOISTING BY THE INTERPRETER
var mean;
mean();
console.log(food);
console.log(food);
var food;
mean = function() {
var food;
food = "chicken";
console.log(food);
food = "fish";
console.log(food);
}
console.log(food);
// *Predicted Output:
// Error



//! 6
// *given
console.log(genre);
var genre = "disco";
rewind();
function rewind() {
    genre = "rock";
    console.log(genre);
    var genre = "r&b";
    console.log(genre);
}
console.log(genre);
//* AFTER HOISTING BY THE INTERPRETER
var genre;
console.log('genre');
genre = disco;
rewind();
function rewind(){
    var genre ;
    genre = "rock"
    console.log('genre')
    genre = "r&b";
    console.log("genre")
}
console.log('genre')
// *Predicted Output:
// undefined
// rock
// r&b
// disco


// ! 7 
// *given
dojo = "san jose";
console.log(dojo);
learn();
function learn() {
    dojo = "seattle";
    console.log(dojo);
    var dojo = "burbank";
    console.log(dojo);
}
console.log(dojo);
//* AFTER HOISTING BY THE INTERPRETER
var dojo; 
dojo = "san jose";
console.log(dojo);
learn(); 
function learn() {
    var dojo; 
    dojo = "seattle";
    console.log(dojo);
    dojo = "burbank";
    console.log(dojo);
}
console.log(dojo);
// *Predicted Output:
// san jose
// seattle
// burbank
// san jose


// ! 8
// *given
console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));
function makeDojo(name, students){
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    if(dojo.students > 50){
        dojo.hiring = true;
    }
    else if(dojo.students <= 0){
        dojo = "closed for now";
    }
    return dojo;
}
//* AFTER HOISTING BY THE INTERPRETER
function makeDojo(name, students) {
    const dojo = {};
    dojo.name = name;
    dojo.students = students;
    if (dojo.students > 50) {
        dojo.hiring = true;
    } 
    else if (dojo.students <= 0) {
        dojo = "closed for now";
    }
    return dojo;
}
console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));
// *Predicted Output:
// ERROR
