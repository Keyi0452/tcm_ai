import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Questionnaire from './pages/Questionnaire';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Questionnaire />} />
      </Routes>
    </Router>
  );
}

export default App;