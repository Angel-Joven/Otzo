import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Index } from './pages/Index';
import { Sales } from './pages/Sales';
import { Fidelizacion } from './pages/Fidelizacion';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Index />} />
        <Route path='/sales' element={<Sales />} />
        <Route path='/fidelizacion' element={<Fidelizacion />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
