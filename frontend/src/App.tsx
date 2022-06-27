import React from 'react';
import './App.css';
import {Routes, Route} from "react-router-dom";
import AppLayout from './layout/AppLayout';
function App() {
  return (
    <Routes>
        <Route path="/" element={<AppLayout/>}>

        </Route>
    </Routes>
  );
}

export default App;
