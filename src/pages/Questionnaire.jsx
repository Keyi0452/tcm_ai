import React, { useState } from 'react';
import { Card, Form, Radio, Button, Toast, NavBar } from 'antd-mobile';
import styled from 'styled-components';
import { questionnaireData } from '../data/questionnaireData';  // 确保这个路径正确

const PageContainer = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  background: #f5f5f5;
`;

const QuestionCard = styled(Card)`
  margin-bottom: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
`;

const Title = styled.h1`
  text-align: center;
  color: #333;
  margin: 20px 0;
  font-size: 24px;
`;

const Disclaimer = styled.div`
  padding: 16px;
  background: #fff7e6;
  border-radius: 8px;
  margin-bottom: 20px;
  font-size: 14px;
  line-height: 1.5;
`;

const Questionnaire = () => {
  const [currentQuestion, setCurrentQuestion] = useState(0);

  return (
    <PageContainer>
      <Title>中医体质测试</Title>
      <Disclaimer>
        本测试仅供参考，不作为医疗诊断依据。
      </Disclaimer>
      <QuestionCard>
        {questionnaireData && questionnaireData[currentQuestion] && (
          <div>
            <h3>{questionnaireData[currentQuestion].text}</h3>
            <Form layout='vertical'>
              {questionnaireData[currentQuestion].options.map((option, index) => (
                <Form.Item key={index}>
                  <Radio>{option}</Radio>
                </Form.Item>
              ))}
            </Form>
          </div>
        )}
      </QuestionCard>
    </PageContainer>
  );
};

export default Questionnaire;