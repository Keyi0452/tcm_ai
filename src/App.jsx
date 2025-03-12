import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Questionnaire from './pages/Questionnaire';
import ResultPage from './pages/ResultPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Questionnaire />} />
        <Route path="/result" element={<ResultPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;