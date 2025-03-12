import React from 'react';
import { Card, NavBar } from 'antd-mobile';
import { constitutionData } from '../data/constitutionInfo';  // 修改这行
import styled from 'styled-components';

const CardContainer = styled.div`
  display: flex;
  gap: 16px;
  padding: 16px 0;
  overflow-x: auto;
`;

export default () => {
  const result = constitutionData[localStorage.getItem('constitutionResult')];
  
  if (!result) {
    return (
      <div style={{ padding: 16 }}>
        <NavBar onBack={() => window.history.back()} />
        <Card style={{ marginTop: 24 }}>
          <Card.Body>
            <p style={{ textAlign: 'center' }}>未找到体质信息，请重新进行测试</p>
          </Card.Body>
        </Card>
      </div>
    );
  }

  return (
    <div style={{ padding: 16 }}>
      <NavBar onBack={() => window.history.back()} />
      <h1 style={{ textAlign: 'center', marginBottom: 24 }}>{result.name}体质调养建议</h1>

      {/* 日常起居建议 */}
      <h2 style={{ fontSize: 18, color: '#333', margin: '16px 0' }}>日常起居建议</h2>
      <CardContainer>
        {result.dailyAdvice.map((advice, index) => (
          <Card key={index} style={{ minWidth: 300 }}>
            <Card.Header title={`${advice.time}建议`} />
            <Card.Body>{advice.content}</Card.Body>
          </Card>
        ))}
      </CardContainer>

      {/* 运动建议 */}
      <h2 style={{ fontSize: 18, color: '#333', margin: '16px 0' }}>运动建议</h2>
      <p style={{ marginBottom: 12 }}>{result.exerciseGeneral}</p>
      <CardContainer>
        {result.exerciseSpecific.map((exercise, index) => (
          <Card key={index} style={{ minWidth: 280 }}>
            <Card.Header title={exercise.name} />
            <Card.Body>{exercise.description}</Card.Body>
          </Card>
        ))}
      </CardContainer>

      {/* 饮食建议 */}
      <h2 style={{ fontSize: 18, color: '#333', margin: '16px 0' }}>饮食建议</h2>
      <p style={{ marginBottom: 12 }}>{result.dietGeneral}</p>
      <CardContainer>
        {result.dietRecipes.map((recipe, index) => (
          <Card key={index} style={{ minWidth: 300 }}>
            <Card.Header title={recipe.name} />
            <Card.Body>
              <p><strong>材料：</strong>{recipe.ingredients}</p>
              <p><strong>做法：</strong>{recipe.method}</p>
            </Card.Body>
          </Card>
        ))}
      </CardContainer>

      {/* 茶饮建议 */}
      <h2 style={{ fontSize: 18, color: '#333', margin: '16px 0' }}>茶饮建议</h2>
      <p style={{ marginBottom: 12 }}>{result.teaGeneral}</p>
      <CardContainer>
        {result.teaRecipes.map((tea, index) => (
          <Card key={index} style={{ minWidth: 280 }}>
            <Card.Header title={tea.name} />
            <Card.Body>
              <p><strong>材料：</strong>{tea.ingredients}</p>
              <p><strong>做法：</strong>{tea.method}</p>
            </Card.Body>
          </Card>
        ))}
      </CardContainer>
    </div>
  );
};