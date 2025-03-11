import React, { useRef } from 'react';
import { Card, Grid, Tabs, Button, Dialog, Toast } from 'antd-mobile';
import { QRCode } from 'qrcode.react';
import styled from 'styled-components';
import { generatePDFReport, generatePoster } from '../utils/reportGenerator';
import { constitutionData } from '../data/constitutionInfo';

const PageContainer = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
`;

const ResultCard = styled(Card)`
  margin-bottom: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
`;

const Section = styled.div`
  margin: 16px 0;
`;

const SectionTitle = styled.h3`
  color: #333;
  margin-bottom: 12px;
`;

const ShareDialog = styled(Dialog)`
  .adm-dialog-body {
    padding: 24px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
`;
const PosterImage = styled.img`
  width: 100%;
  max-width: 300px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  margin: 16px 0;
`;

const ConstitutionResult = ({ constitution }) => {
  const reportRef = useRef(null);
  const constitutionInfo = constitutionData[constitution];

  if (!constitution || !constitutionInfo) {
    return (
      <PageContainer>
        <ResultCard>
          <Card.Body>
            <p>未找到体质信息，请重新进行测试</p>
          </Card.Body>
        </ResultCard>
      </PageContainer>
    );
  }

  const handleExportPDF = async () => {
    try {
      Toast.show({
        content: '正在生成报告...',
        duration: 1000,
      });
      await generatePDFReport(reportRef, constitutionInfo.name);
      Toast.show({
        content: '报告生成成功',
        duration: 1000,
      });
    } catch (error) {
      Toast.show({
        content: '报告生成失败，请重试',
        duration: 2000,
      });
    }
  };

  const handleShare = async () => {
    try {
      Toast.show({
        content: '正在生成海报...',
        duration: 1000,
      });
      
      const posterUrl = await generatePoster(reportRef, constitutionInfo.name);
      
      Dialog.show({
        content: (
          <div style={{ textAlign: 'center' }}>
            <p>长按图片保存分享</p>
            <PosterImage src={posterUrl} alt="分享海报" />
            <p>或扫描二维码分享结果</p>
            <QRCode 
              value={window.location.href}
              size={150}
              level="H"
            />
            <p style={{ fontSize: '14px', color: '#666', marginTop: '8px' }}>
              复制链接分享：{window.location.href}
            </p>
          </div>
        ),
        closeOnAction: true,
        actions: [
          {
            key: 'copy',
            text: '复制链接',
            onClick: () => {
              navigator.clipboard.writeText(window.location.href);
              Toast.show({
                content: '链接已复制',
                duration: 1000,
              });
            }
          },
          {
            key: 'close',
            text: '关闭',
          }
        ]
      });
    } catch (error) {
      Toast.show({
        content: '生成海报失败，请重试',
        duration: 2000,
      });
    }
  };

  return (
    <PageContainer>
      <div ref={reportRef}>
        <ResultCard>
          <Card.Header title={constitutionInfo.name} />
          <Card.Body>
            <p>{constitutionInfo.description}</p>
          </Card.Body>
        </ResultCard>

      <Tabs>
        <Tabs.Tab title="日常建议" key="daily">
          {constitutionInfo.dailyAdvice.map((advice, index) => (
            <Section key={index}>
              <SectionTitle>{advice.time}</SectionTitle>
              <p>{advice.content}</p>
            </Section>
          ))}
        </Tabs.Tab>

        <Tabs.Tab title="运动建议" key="exercise">
          <Section>
            <SectionTitle>运动原则</SectionTitle>
            <p>{constitutionInfo.exerciseGeneral}</p>
          </Section>
          <Grid columns={1} gap={8}>
            {constitutionInfo.exerciseSpecific.map((exercise, index) => (
              <Grid.Item key={index}>
                <ResultCard>
                  <Card.Header title={exercise.name} />
                  <Card.Body>{exercise.description}</Card.Body>
                </ResultCard>
              </Grid.Item>
            ))}
          </Grid>
        </Tabs.Tab>

        <Tabs.Tab title="饮食建议" key="diet">
          <Section>
            <SectionTitle>饮食原则</SectionTitle>
            <p>{constitutionInfo.dietGeneral}</p>
          </Section>
          <Grid columns={1} gap={8}>
            {constitutionInfo.dietRecipes.map((recipe, index) => (
              <Grid.Item key={index}>
                <ResultCard>
                  <Card.Header title={recipe.name} />
                  <Card.Body>
                    <p>食材：{recipe.ingredients}</p>
                    <p>做法：{recipe.method}</p>
                  </Card.Body>
                </ResultCard>
              </Grid.Item>
            ))}
          </Grid>
        </Tabs.Tab>

        <Tabs.Tab title="茶饮推荐" key="tea">
          <Section>
            <SectionTitle>茶饮原则</SectionTitle>
            <p>{constitutionInfo.teaGeneral}</p>
          </Section>
          <Grid columns={1} gap={8}>
            {constitutionInfo.teaRecipes.map((tea, index) => (
              <Grid.Item key={index}>
                <ResultCard>
                  <Card.Header title={tea.name} />
                  <Card.Body>
                    <p>材料：{tea.ingredients}</p>
                    <p>泡制方法：{tea.method}</p>
                  </Card.Body>
                </ResultCard>
              </Grid.Item>
            ))}
          </Grid>
        </Tabs.Tab>
      </Tabs>
      </div>

      <Grid columns={2} gap={8}>
        <Grid.Item>
          <Button
            block
            color='primary'
            onClick={handleExportPDF}
            style={{ marginTop: '20px' }}
          >
            导出PDF报告
          </Button>
        </Grid.Item>
        <Grid.Item>
          <Button
            block
            color='success'
            onClick={handleShare}
            style={{ marginTop: '20px' }}
          >
            分享结果
          </Button>
        </Grid.Item>
      </Grid>
    </PageContainer>
  );
};

export default ConstitutionResult;