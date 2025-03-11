import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Questionnaire from './pages/Questionnaire';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Questionnaire />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;