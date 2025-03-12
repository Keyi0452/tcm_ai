import { fullQuestionnaireData } from './data/fullQuestionnaireData';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Questionnaire from './pages/Questionnaire';
import ResultPage from './pages/ResultPage'; // 确保路径正确

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Questionnaire />} />
        <Route path="/result" element={<ResultPage />} /> // 确保 '/result' 路由指向 ResultPage
      </Routes>
    </Router>
  );
}

export default App;
