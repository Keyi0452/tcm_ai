import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';

const createCover = (pdf, title, constitution) => {
  pdf.setFillColor(247, 247, 247);
  pdf.rect(0, 0, 210, 297, 'F');
  
  // 添加标题
  pdf.setFont('helvetica', 'bold');
  pdf.setFontSize(24);
  pdf.setTextColor(51, 51, 51);
  pdf.text('中医体质调养报告', 105, 100, { align: 'center' });
  
  // 添加体质类型
  pdf.setFontSize(18);
  pdf.text(`体质类型：${constitution}`, 105, 130, { align: 'center' });
  
  // 添加日期
  pdf.setFontSize(14);
  pdf.setTextColor(102, 102, 102);
  const date = new Date().toLocaleDateString('zh-CN');
  pdf.text(`生成日期：${date}`, 105, 150, { align: 'center' });
  
  // 添加装饰线
  pdf.setDrawColor(24, 144, 255);
  pdf.setLineWidth(0.5);
  pdf.line(40, 170, 170, 170);
  
  // 添加页脚
  pdf.setFontSize(10);
  pdf.text('本报告仅供参考，如有健康问题请及时就医', 105, 280, { align: 'center' });
};

export const generatePDFReport = async (contentRef, constitution) => {
  const canvas = await html2canvas(contentRef.current, {
    scale: 2,
    useCORS: true,
    logging: false
  });
  
  const imgData = canvas.toDataURL('image/jpeg', 1.0);
  const pdf = new jsPDF({
    orientation: 'portrait',
    unit: 'mm',
    format: 'a4'
  });
  
  // 添加封面
  createCover(pdf, '中医体质调养报告', constitution);
  
  // 添加内容页
  pdf.addPage();
  const pdfWidth = pdf.internal.pageSize.getWidth();
  const pdfHeight = (canvas.height * pdfWidth) / canvas.width;
  pdf.addImage(imgData, 'JPEG', 0, 0, pdfWidth, pdfHeight);
  
  // 生成PDF
  pdf.save('中医体质调养报告.pdf');
};

// 生成分享海报
export const generatePoster = async (contentRef, constitution) => {
  const canvas = await html2canvas(contentRef.current, {
    scale: 2,
    useCORS: true,
    logging: false,
    width: 375, // 移动端宽度
    height: 667 // 适合分享的高度
  });
  
  return canvas.toDataURL('image/jpeg', 0.8);
};