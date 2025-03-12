export const optionScores = {
  "没有": 1,
  "很少": 2,
  "有时": 3,
  "经常": 4,
  "总是": 5
};

export const calculateConstitution = (scores) => {
  const results = {};
  const rawScores = {};
  
  // 计算原始分
  constitutionTypes.forEach(type => {
    const typeQuestions = questionnaireData.filter(q => q.category === type);
    const totalScore = typeQuestions.reduce((sum, q) => sum + scores[q.id], 0);
    const originalScore = (totalScore / (typeQuestions.length * 5)) * 100;
    rawScores[type] = originalScore;
  });

  // 转换分数
  Object.keys(rawScores).forEach(type => {
    if (rawScores[type] >= 60) {
      results[type] = "是";
    } else if (rawScores[type] >= 40) {
      results[type] = "倾向是";
    } else if (rawScores[type] >= 30) {
      results[type] = "倾向否";
    } else {
      results[type] = "否";
    }
  });

  return {
    rawScores,
    results
  };
};