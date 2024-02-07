function pizzaOven(crustType, sauceType, cheeses, toppings){
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}



var pizza1 = pizzaOven("deep dish", "traditional","mozzarella",["pepperoni", "sausage"]);
console.log(pizza1);

var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(pizza2)

var pizza2 = pizzaOven("Pizza Bagels", "Basil pesto","Cheddar",["Bacon", "Black olives"]);
console.log(pizza2);

var pizza3 = pizzaOven("Flatbread", "Bechamel",["Parmesan","Gruyere"],["Anchovies", "Mushrooms"]);
console.log(pizza3);




// Bonus challenge



function pizzaOven(crustType, sauceType, cheeses, toppings){
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

function getRandom(ingredient) {
    return ingredient[Math.floor(Math.random() * ingredient.length)];
}

    var crustType = ["deep dish", "hand tossed", "pizza bagels", "Flatbread"];
    var sauceType = ["traditional", "marinara", "Basil pesto", "Bechamel"];
    var cheeses = ["mozzarella", ["mozzarella", "feta"],"Cheddar" , ["Parmesan","Gruyere"]];
    var toppings = [["pepperoni", "sausage"],["mushrooms", "olives", "onions"],["Bacon", "Black olives"], ["Anchovies", "Mushrooms","egg"]];

var s1 = pizzaOven(getRandom(crustType), getRandom(sauceType), getRandom(cheeses), getRandom(toppings));
console.log(s1);