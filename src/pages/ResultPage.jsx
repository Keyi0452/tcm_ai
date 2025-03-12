import React from 'react';
import { Card, NavBar } from 'antd-mobile';
import { constitutionData } from '../data/constitutionInfo';
import styled from 'styled-components';

const PageContainer = styled.div`
  padding: 16px;
  max-width: 1200px;
  margin: 0 auto;
`;

const CardContainer = styled.div`
  display: flex;
  gap: 16px;
  padding: 16px 0;
  overflow-x: auto;
  
  @media (max-width: 768px) {
    flex-wrap: nowrap;
  }
`;

const IntroCard = styled(Card)`
  margin: 16px 0;
  background: #fff9e6;
`;

const SectionTitle = styled.h2`
  font-size: 20px;
  color: #333;
  margin: 24px 0 16px;
  padding-bottom: 8px;
  border-bottom: 2px solid #ffd966;
`;

const GeneralAdvice = styled.p`
  margin-bottom: 16px;
  line-height: 1.6;
  color: #666;
`;

export default () => {
  const result = constitutionData[localStorage.getItem('constitutionResult')];
  
  if (!result) {
    return (
      <PageContainer>
        <NavBar onBack={() => window.history.back()} />
        <Card style={{ marginTop: 24 }}>
          <Card.Body>
            <p style={{ textAlign: 'center' }}>未找到体质信息，请重新进行测试</p>
          </Card.Body>
        </Card>
      </PageContainer>
    );
  }

  return (
    <PageContainer>
      <NavBar onBack={() => window.history.back()} />
      <h1 style={{ textAlign: 'center', marginBottom: 24 }}>{result.name}体质调养建议</h1>

      {/* 体质介绍 */}
      <IntroCard>
        <Card.Header title="体质特征介绍" />
        <Card.Body>{result.introduction}</Card.Body>
      </IntroCard>

      {/* 日常起居建议 */}
      <SectionTitle>日常起居建议</SectionTitle>
      <CardContainer>
        {result.dailyAdvice.map((advice, index) => (
          <Card key={index} style={{ flex: 1, minWidth: '30%' }}>
            <Card.Header title={`${advice.time}建议`} />
            <Card.Body>{advice.content}</Card.Body>
          </Card>
        ))}
      </CardContainer>

      {/* 运动建议 */}
      <SectionTitle>运动建议</SectionTitle>
      <GeneralAdvice>{result.exerciseGeneral}</GeneralAdvice>
      <CardContainer>
        {result.exerciseSpecific.map((exercise, index) => (
          <Card key={index} style={{ flex: 1, minWidth: '30%' }}>
            <Card.Header title={exercise.name} />
            <Card.Body>{exercise.description}</Card.Body>
          </Card>
        ))}
      </CardContainer>

      {/* 饮食建议 */}
      <SectionTitle>饮食建议</SectionTitle>
      <GeneralAdvice>{result.dietGeneral}</GeneralAdvice>
      <CardContainer>
        {result.dietRecipes.map((recipe, index) => (
          <Card key={index} style={{ flex: 1, minWidth: '30%' }}>
            <Card.Header title={recipe.name} />
            <Card.Body>
              <p><strong>材料：</strong>{recipe.ingredients}</p>
              <p><strong>做法：</strong>{recipe.method}</p>
            </Card.Body>
          </Card>
        ))}
      </CardContainer>

      {/* 茶饮建议 */}
      <SectionTitle>茶饮建议</SectionTitle>
      <GeneralAdvice>{result.teaGeneral}</GeneralAdvice>
      <CardContainer>
        {result.teaRecipes.map((tea, index) => (
          <Card key={index} style={{ flex: 1, minWidth: '30%' }}>
            <Card.Header title={tea.name} />
            <Card.Body>
              <p><strong>材料：</strong>{tea.ingredients}</p>
              <p><strong>做法：</strong>{tea.method}</p>
            </Card.Body>
          </Card>
        ))}
      </CardContainer>
    </PageContainer>
  );
};