import { Routes, Route, Navigate } from 'react-router-dom'
import Create from "./components/Create";


import './App.css'


function App() {

  return (
    <div>
      <Routes>
        <Route path='/' element={<Navigate to={'/products'} />} />
        <Route path='/products' element={<Create />} />
      </Routes>
    </div>

  )
}

export default App
