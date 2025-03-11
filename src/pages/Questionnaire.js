import React, { useState } from 'react';
import { Layout, Card, Radio, Button, Progress, Result, Row, Col, Typography } from 'antd';
import { constitutionData } from '../data/constitutionInfo';
import { questions_data } from '../data/questions';

const { Header, Content, Footer } = Layout;
const { Title, Paragraph } = Typography;

const Questionnaire = () => {
    const [step, setStep] = useState('intro'); // intro, question, result
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [answers, setAnswers] = useState({});
    const [results, setResults] = useState(null);

    const renderIntro = () => (
        <Card>
            <Title level={2}>中医体质辨识问卷</Title>
            <Paragraph>
                本问卷基于《中医体质分类与判定》标准，旨在帮助您了解自己的体质特点。
            </Paragraph>
            <Paragraph type="secondary">
                免责声明：本测试结果仅供参考，不构成医疗建议。如有健康问题，请咨询专业医师。
            </Paragraph>
            <Button type="primary" onClick={() => setStep('question')}>
                开始测试
            </Button>
        </Card>
    );

    const renderQuestion = () => (
        <>
            <Progress percent={(currentQuestion / 60) * 100} />
            <Card style={{ marginTop: '20px' }}>
                <Title level={4}>问题 {currentQuestion + 1}/60</Title>
                <Paragraph>{questions_data.questions[currentQuestion].question}</Paragraph>
                <Radio.Group 
                    onChange={(e) => handleAnswer(e.target.value)}
                    value={answers[currentQuestion + 1]}
                    style={{ width: '100%' }}
                >
                    <Row justify="space-between">
                        {questions_data.questions[currentQuestion].options.map((option, index) => (
                            <Col span={4} key={index}>
                                <Radio value={index + 1}>{option}</Radio>
                            </Col>
                        ))}
                    </Row>
                </Radio.Group>
            </Card>
        </>
    );

    const renderResult = () => (
        <>
            <Title level={2}>体质辨识结果</Title>
            {results.map(constitution => (
                <div key={constitution.type}>
                    <Card title={constitution.name} style={{ marginBottom: '20px' }}>
                        <Paragraph>得分：{constitution.score}分</Paragraph>
                        <Paragraph>{constitution.description}</Paragraph>
                    </Card>

                    <Title level={3}>日常起居建议</Title>
                    <Row gutter={16}>
                        {constitution.dailyAdvice.map((advice, index) => (
                            <Col span={8} key={index}>
                                <Card title={advice.time}>
                                    {advice.content}
                                </Card>
                            </Col>
                        ))}
                    </Row>

                    <Title level={3}>运动建议</Title>
                    <Paragraph>{constitution.exerciseGeneral}</Paragraph>
                    <Row gutter={16}>
                        {constitution.exerciseSpecific.map((exercise, index) => (
                            <Col span={8} key={index}>
                                <Card title={exercise.name}>
                                    {exercise.description}
                                </Card>
                            </Col>
                        ))}
                    </Row>

                    <Title level={3}>饮食建议</Title>
                    <Paragraph>{constitution.dietGeneral}</Paragraph>
                    <Row gutter={16}>
                        {constitution.dietRecipes.map((recipe, index) => (
                            <Col span={8} key={index}>
                                <Card title={recipe.name}>
                                    <Paragraph>材料：{recipe.ingredients}</Paragraph>
                                    <Paragraph>做法：{recipe.method}</Paragraph>
                                </Card>
                            </Col>
                        ))}
                    </Row>

                    <Title level={3}>茶饮建议</Title>
                    <Paragraph>{constitution.teaGeneral}</Paragraph>
                    <Row gutter={16}>
                        {constitution.teaRecipes.map((tea, index) => (
                            <Col span={8} key={index}>
                                <Card title={tea.name}>
                                    <Paragraph>材料：{tea.ingredients}</Paragraph>
                                    <Paragraph>制法：{tea.method}</Paragraph>
                                </Card>
                            </Col>
                        ))}
                    </Row>
                </div>
            ))}
        </>
    );

    return (
        <Layout className="layout">
            <Header>
                <Title level={2} style={{ color: 'white', margin: '16px 0' }}>
                    中医体质辨识系统
                </Title>
            </Header>
            <Content style={{ padding: '50px' }}>
                {step === 'intro' && renderIntro()}
                {step === 'question' && renderQuestion()}
                {step === 'result' && renderResult()}
            </Content>
            <Footer style={{ textAlign: 'center' }}>
                中医体质辨识系统 ©2024
            </Footer>
        </Layout>
    );
};

export default Questionnaire;