import React, { useState } from 'react';
import { Card, Form, Radio, Button, Toast, NavBar, Space } from 'antd-mobile';
import styled from 'styled-components';
import { questionnaireData, constitutionTypes } from '../data/questionnaireData';

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

const NavigationButtons = styled.div`
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
`;

const ProgressText = styled.div`
  text-align: center;
  color: #666;
  margin: 10px 0;
`;

const Questionnaire = () => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const [form] = Form.useForm();

  const handleNext = () => {
    const value = form.getFieldValue(`question_${currentQuestion}`);
    if (!value) {
      Toast.show({
        content: '请选择一个选项',
        position: 'bottom',
      });
      return;
    }
    
    setAnswers(prev => ({
      ...prev,
      [currentQuestion]: value
    }));

    if (currentQuestion < questionnaireData.length - 1) {
      setCurrentQuestion(prev => prev + 1);
      form.resetFields();
    } else {
      // TODO: 处理问卷完成逻辑
      Toast.show({
        content: '问卷已完成！',
        position: 'bottom',
      });
    }
  };

  const handlePrev = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(prev => prev - 1);
      form.setFieldsValue({
        [`question_${currentQuestion - 1}`]: answers[currentQuestion - 1]
      });
    }
  };

  return (
    <PageContainer>
      <NavBar onBack={handlePrev}>
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