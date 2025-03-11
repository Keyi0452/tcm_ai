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

import React from 'react';
import { Card } from 'antd-mobile';

const Questionnaire = () => {
  return (
    <div style={{ padding: '16px' }}>
      <Card title="中医体质测试">
        <p>测试页面已成功加载</p>
      </Card>
    </div>
  );
};

export default Questionnaire;