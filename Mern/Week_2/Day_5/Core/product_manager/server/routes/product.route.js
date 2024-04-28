const ProductController = require("../controllers/product.controller")


module.exports = (app) =>{
    //? create one
    app.post("/api/products", ProductController.createProduct)
}