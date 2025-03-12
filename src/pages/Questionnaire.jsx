import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, Form, Radio, Button, Toast, NavBar } from 'antd-mobile';
import styled from 'styled-components';
import { fullQuestionnaireData } from '../data/fullQuestionnaireData';

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

const SubmitButton = styled(Button)`
  width: 100%;
  margin-top: 20px;
`;

const Questionnaire = () => {
  const navigate = useNavigate();
  const [form] = Form.useForm();

  const handleSubmit = () => {
    form.validateFields().then(values => {
      // 检查是否所有题目都已回答
      const unansweredQuestions = questionnaireData.filter(
        (_, index) => !values[`question_${index}`]
      );

      if (unansweredQuestions.length > 0) {
        Toast.show({
          content: '请回答所有问题',
          position: 'bottom',
        });
        return;
      }

      // 计算分数
      const scores = calculateScores(values);
      const constitution = determineConstitution(scores);
      
      // 存储结果并跳转
      localStorage.setItem('constitutionResult', constitution);
      navigate('/result');
    });
  };

  // 计分逻辑函数
  const calculateScores = (answers) => {
    const scores = {};
    constitutionTypes.forEach(type => scores[type] = 0);
    
    Object.entries(answers).forEach(([key, choice]) => {
      const questionId = parseInt(key.split('_')[1]);
      const question = questionnaireData[questionId];
      const score = question.options.indexOf(choice) + 1; // 选项分数从1到5
      scores[question.category] += score;
    });

    // 计算百分比分数
    Object.keys(scores).forEach(type => {
      const totalQuestions = questionnaireData.filter(q => q.category === type).length;
      if (totalQuestions > 0) {
        scores[type] = (scores[type] / (totalQuestions * 5)) * 100;
      }
    });

    return scores;
  };

  // 体质判断函数
  const determineConstitution = (scores) => {
    // 判断是否为平和质
    if (scores["平和质"] >= 60 && 
        Object.entries(scores).every(([type, score]) => 
          type === "平和质" || score < 30
        )) {
      return "平和质";
    }

    // 判断其他体质
    let maxScore = 0;
    let constitution = "平和质";
    Object.entries(scores).forEach(([type, score]) => {
      if (type !== "平和质" && score >= 40 && score > maxScore) {
        maxScore = score;
        constitution = type;
      }
    });

    return constitution;
  };

  return (
    <PageContainer>
      <NavBar onBack={() => window.history.back()} />
      <Title>中医体质测试</Title>
      <Disclaimer>本测试仅供参考，不作为医疗诊断依据。</Disclaimer>
      
      <Form form={form}>
        {questionnaireData.map((question, index) => (
          <QuestionCard key={index}>
            <Card.Body>
              <h3>{question.question}</h3>
              <Form.Item name={`question_${index}`} rules={[{ required: true, message: '请选择一个选项' }]}>
                <Radio.Group>
                  {question.options.map((option, optionIndex) => (
                    <Radio key={optionIndex} value={option}>{option}</Radio>
                  ))}
                </Radio.Group>
              </Form.Item>
            </Card.Body>
          </QuestionCard>
        ))}
      </Form>

      <SubmitButton color='primary' onClick={handleSubmit}>
        提交问卷
      </SubmitButton>
    </PageContainer>
  );
};

export default Questionnaire;