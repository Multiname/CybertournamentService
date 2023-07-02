import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Tournaments from './pages/Tournaments';
import Rating from './pages/Rating';
import Commands from './pages/Commands';
import MainPage from './pages/MainPage';

function App() {
  return (
    <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route  path='/' element={<MainPage/>}/>
        <Route  path='/tournaments' element={<Tournaments/>}/>
        <Route  path='/rating' element={<Rating/>}/>
        <Route  path='/commands' element={<Commands/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
