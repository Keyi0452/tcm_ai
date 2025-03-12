import { fullQuestionnaireData } from './data/fullQuestionnaireData';
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Questionnaire from './pages/Questionnaire';
import ResultPage from './pages/ResultPage';

function App() {
  return (
    <div style={{ width: '100%', minHeight: '100vh', background: '#fff' }}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={
            <React.Suspense fallback={<div>Loading...</div>}>
              <Questionnaire />
            </React.Suspense>
          } />
          <Route path="/result" element={
            <React.Suspense fallback={<div>Loading...</div>}>
              <ResultPage />
            </React.Suspense>
          } />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;