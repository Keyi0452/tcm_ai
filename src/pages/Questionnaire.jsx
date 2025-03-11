import React, { useState } from 'react';
import { Card, Form, Radio, Button, Toast, NavBar } from 'antd-mobile';
import styled from 'styled-components';
import { questionnaireData } from '../data/questionnaireData';

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
  const [form] = Form.useForm();

  const onFinish = (values) => {
    // 这里添加问卷计算逻辑
    Toast.show({
      content: '问卷提交成功！',
      duration: 1000,
    });
  };

  return (
    <>
      <NavBar back={null}>中医体质辨识</NavBar>
      <PageContainer>
        <Title>中医体质辨识问卷</Title>
        <Disclaimer>
          声明：本问卷仅供参考，不作为医疗诊断依据。如有健康问题，请及时就医。
        </Disclaimer>
        
        <Form
          form={form}
          onFinish={onFinish}
          layout='vertical'
        >
          {questionnaireData.map((question, index) => (
            <QuestionCard key={index}>
              <Form.Item
                name={`q${index}`}
                label={question.text}
                rules={[{ required: true, message: '请选择答案' }]}
              >
                <Radio.Group>
                  {question.options.map((option, optIndex) => (
                    <Radio key={optIndex} value={optIndex}>
                      {option}
                    </Radio>
                  ))}
                </Radio.Group>
              </Form.Item>
            </QuestionCard>
          ))}
          
          <Button
            block
            color='primary'
            size='large'
            type='submit'
            style={{ marginTop: '20px' }}
          >
            提交问卷
          </Button>
        </Form>
      </PageContainer>
    </>
  );
};

export default Questionnaire;