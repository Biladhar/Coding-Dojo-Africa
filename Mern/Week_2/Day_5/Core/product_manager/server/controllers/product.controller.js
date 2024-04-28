const Product = require("../models/product.model")


module.exports = {
    createProduct : (req,res) =>{
        Product.create(req.body)
        .then(newCreatedProduct => {
            console.log(`New Product created with success`);
            res.json({ data: newCreatedProduct, message: 'New Product created with success' })
        })
        .catch(error => {
            console.log(error)
            res.json(error)
        })

    }
}