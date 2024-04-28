import React, { useState } from 'react'
import axios from "axios"

const Create = () => {
    const [title, setTitle] = useState("");
    const [price, setPrice] = useState(0);
    const [description, setDescription] = useState("")

    const SubmitHandler = (e) => {
        e.preventDefault()
        axios.post("http://localhost:5000/api/products",{
            title : title,
            price : price,
            description : description
        })
        .then((res)=>{
            console.log("done")
        })
        .catch((err)=>{
            console.log(err)
        })
    }


    return (
        <div className='container'>

            <div className='row'>
                <div className='col-md-6 offset-md-3 d-flex flex-column align-items-center'>
                    <h1>Products Manager</h1>
                    <form onSubmit={SubmitHandler} >
                        <div className='d-flex '>
                        <label>Title</label>
                        <input type="text" value={title} className='form-control mb-2' onChange={(e) => { setTitle(e.target.value) }} />
                        </div>
                        <div className='d-flex '>
                        <label>Price</label>
                        <input type="number" value={price} className='form-control mb-2' onChange={(e) => { setPrice(e.target.value) }} />
                        </div>
                        <div>
                        <label>Description</label>
                        <textarea type="text" value={description} className='form-control mb-2' onChange={(e) => { setDescription(e.target.value) }} />
                        </div>
                        <div  className='text-center'>
                        <button>create</button>
                        </div>
                            
                    </form>
                </div>
            </div>


        </div>
    )
}

export default Create