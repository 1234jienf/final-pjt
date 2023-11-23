<template>
    <div>
      <h2>투자 설문조사</h2>
  
      <!-- 질문 1 -->
      <div>
        <h3>1. 처음 투자는 어떻게 하게 됐나요?</h3>
        <div v-for="(answer, index) in firstInvestmentOptions" :key="index">
          <input type="radio" :value="answer.value" v-model="firstInvestmentAnswer" />
          <label>{{ answer.label }}</label>
        </div>
      </div>
  
      <!-- 질문 2 -->
      <div>
        <h3>2. 투자 후 3개월째에 5%의 손실이 났다면</h3>
        <!-- 라디오 버튼 사용 -->
        <div v-for="(answer, index) in lossOptions" :key="index">
          <input type="radio" :value="answer.value" v-model="lossSituation" />
          <label>{{ answer.label }}</label>
        </div>
      </div>
  
      <!-- 질문 3 -->
      <div>
        <h3>3. 투자 손실로 고민이 생겼을 때 어떤 친구가 옆에 있으면 좋겠을까?</h3>
        <!-- 체크박스 사용 -->
        <div v-for="(answer, index) in friendOptions" :key="index">
          <input type="radio" :value="answer.value" v-model="preferredFriends" />
          <label>{{ answer.label }}</label>
        </div>
      </div>
      <!-- 질문 4 -->

      <div>
        <h3>4. 예적금을 가입할 때 당신은 어떻게 행동하나요?</h3>
        <div v-for="(answer, index) in savingsAccountOptions" :key="index">
            <input type="radio" :value="answer.value" v-model="savingsAccountAnswer" />
            <label>{{ answer.label }}</label>
        </div>
        </div>

    <!-- 질문 5 -->
    <div>
    <h3>5. 투자 후 손실이 발생한다면 어떻게 대처하실 건가요?</h3>
    <div v-for="(answer, index) in lossHandlingOptions" :key="index">
        <input type="radio" :value="answer.value" v-model="lossHandlingAnswer" />
        <label>{{ answer.label }}</label>
    </div>
    </div>

    <!-- 질문 6 -->
    <div>
    <h3>6. 생각지 않은 큰 투자 수익이 발생한다면 어떻게 하실 건가요?</h3>
    <div v-for="(answer, index) in unexpectedProfitOptions" :key="index">
        <input type="radio" :value="answer.value" v-model="unexpectedProfitAnswer" />
        <label>{{ answer.label }}</label>
    </div>
    </div>

    <!-- 질문 7 -->
    <div>
    <h3>7. 다음 중 어떤 금융 투자 상품에 투자하실 건가요? (금액: 5000만원)</h3>
    <div v-for="(answer, index) in investmentProducts" :key="index">
        <input type="radio" :value="answer.value" v-model="investmentProductAnswer" />
        <label>{{ answer.label }}</label>
    </div>
    </div>
    <!-- 질문 8 -->
    <div>
    <h3>8. 투자 방식은 어떤 방향성을 가지고 있나요?</h3>
    <div v-for="(answer, index) in investmentApproachOptions" :key="index">
        <input type="radio" :value="answer.value" v-model="investmentApproach" />
        <label>{{ answer.label }}</label>
    </div>
    </div>
  
      <!-- 결과 제출 버튼 -->
      <button @click="submitSurvey">설문 조사 결과 제출</button>
    </div>
  </template>
  
<script>
  export default {
    data() {
      return {
        firstInvestmentAnswer: [],
        lossSituation: '',
        savingsAccountAnswer: '',
        lossHandlingAnswer: '',
        unexpectedProfitAnswer: '',
        preferredFriends: '',
        investmentProductAnswer: '', // 이 변수를 추가
        investmentApproach: '',
        firstInvestmentOptions: [
          { label: '스스로 찾아보고 판단', value: 'TJ' },
          { label: '투자를 통해 남들보다 높은 수익을 내고 싶어서', value: 'ES' },
          { label: '주변 사람들의 이야기를 듣고 따라하게 됨', value: 'SFP' },
          { label: '투자에 대한 호기심', value: 'NT' },
          { label: '검증된 투자 수익률 정보를 보고', value: 'STJ' },
        ],
        lossOptions: [
          { label: '바로 계약 해지', value: 'J' },
          { label: '한 두 달 더 지켜본다', value: 'TJ' },
          { label: '6개월 더 지켜본다', value: 'P' },
          { label: '장기적으로 투자하는 거라 큰 걱정하지 않는다', value: 'SP' },
          { label: '수익률이 하락했을때보다 조금씩 더 투자', value: 'SJ' },
          // 다른 선택지들을 추가해주세요
        ],
        friendOptions: [
          { label: '내 투자에 어떤 문제가 있는지 명확하게 설명해줄 수 있는 친구', value: 'STJ' },
          { label: '내 불만과 투정을 다 받아주는 친구', value: 'EF' },
          { label: '본인도 손해를 본 적 있다며 위로 해주는 친구', value: 'F' },
          { label: '손실을 만회할 방법을 같이 찾아봐주는 친구', value: 'ET' },
          { label: '바로 기분 전환을 시켜주는 친구', value: 'EP' },
          // 다른 선택지들을 추가해주세요
        ],
        savingsAccountOptions :[
            { label: '동아리나 모임을 통해서 정보를 얻는다', value: 'ET' },
            { label: '인터넷 검색 및 여러책을 보면서 나에게 알맞은 상품을 고려하고 가입한다', value: 'INT' },
            { label: '귀찮은건 질색! 대충 내 눈에 좋아보이는거 가입한다', value: 'IP' },
            { label: '은행원이나 친구에게 추천받아서 가입한다.', value: 'EP' },
        ],
        investmentProducts: [
            { label: '60퍼 확률로 연 6퍼 수익 또는 40퍼 확률로 -2퍼 손실이 가능한 상품', value: 'SFJ' },
            { label: '60퍼 확률로 연 11퍼 수익 또는 40퍼 확률로 -5퍼 손실이 가능한 상품', value: 'ES' },
            { label: '60퍼 확률로 연 16퍼 수익 또는 40퍼 확률로 -8퍼 손실이 가능한 상품', value: 'F' },
            { label: '60퍼 확률로 연 21퍼 수익 또는 40퍼 확률로 -11퍼 손실이 가능한 상품', value: 'TP' },
            { label: '60퍼 확률로 연 26퍼 수익 또는 40퍼 확률로 -14퍼 손실이 가능한 상품', value: 'ESP' },
        ],
        unexpectedProfitOptions: [
            { label: '이미 쓰기로 한곳에 먼저 지출', value: 'ST' },
            { label: '그 날 기분에 따라 즉흥적으로 결정', value: 'P' },
            { label: '주변사람들에게 한턱 쏘면서 함께 즐김', value: 'E' },
            { label: '집이나 차, 명품 등 남들이 부러워할만한 걸 삼', value: 'EP' },
            { label: '재투자할지 아니면 필요한데 쓸지 일단 고민부터 할듯', value: 'TJ' },

        ],
        investmentApproachOptions: [
            { label: '목돈만 투자하고 오랫동안 지켜보기', value: 'IJ' },
            { label: '목돈 먼저 투자 후, 매달 꾸준히 투자', value: 'SJ' },
            { label: '목돈 먼저 투자후, 여유 생길때 마다', value: 'P' },
            { label: '목돈은 없지만 매달 꾸준히', value: 'J' },
            { label: '목돈은 없지만, 여유가 생길때마다 조금씩 투자', value: 'EJ' },

        ],
        lossHandlingOptions: [
            { label: '손실을 원하지 않아요(무조건 원금 보전)', value: 'SJ' },
            { label: '원금의 5 퍼 까지 손실 ㄱㅊ', value: 'J' },
            { label: '원금의 10퍼까지 손실 ㄱㅊ', value: 'TJ' },
            { label: '원금의 15퍼까지 손실 ㄱㅊ', value: 'TFP' },
            { label: '원금의 25퍼까지 손실 ㄱㅊ', value: 'TP' },

        ]
      };
    },
    methods: {
    submitSurvey() {
        const mbtiCount = {
      E: 0,
      I: 0,
      S: 0,
      N: 0,
      T: 0,
      F: 0,
      P: 0,
      J: 0,
    };
    // 설문 결과를 서버로 보내는 로직 추가
        const surveyResult = {
            firstInvestmentAnswer: this.firstInvestmentAnswer || '',
            lossSituation: this.lossSituation || '',
            savingsAccountAnswer: this.savingsAccountAnswer || '',
            lossHandlingAnswer: this.lossHandlingAnswer || '',
            unexpectedProfitAnswer: this.unexpectedProfitAnswer || '',
            preferredFriends: this.preferredFriends || '',
            investmentProductAnswer: this.investmentProductAnswer || '',
            investmentApproach: this.investmentApproach || '',
        };
            // MBTI 유형에 해당하는 선택된 항목들의 개수 카운트
            for (const answer in surveyResult) {

            if (surveyResult.hasOwnProperty(answer)) {
            const value = surveyResult[answer];
            if (value && value.includes) {
                // includes 메서드 사용 가능한지 확인 후 로직 실행;
                if (value.includes('E')) mbtiCount['E']++;
                if (value.includes('I')) mbtiCount['I']++;
                if (value.includes('S')) mbtiCount['S']++;
                if (value.includes('N')) mbtiCount['N']++;
                if (value.includes('T')) mbtiCount['T']++;
                if (value.includes('F')) mbtiCount['F']++;
                if (value.includes('P')) mbtiCount['P']++;
                if (value.includes('J')) mbtiCount['J']++;
            }
        }
            }
    // MBTI 유형과 선택된 항목들의 개수 콘솔에 출력
    console.log('MBTI 결과:');
    console.log(mbtiCount);

    
    // 여기에 서버로 데이터 전송하는 코드를 추가하세요

    let mbtiResult = '';
    const pairs = [['E', 'I'], ['S', 'N'], ['T', 'F'], ['P', 'J']];
    pairs.forEach(pair => {
      const first = pair[0];
      const second = pair[1];
      if (mbtiCount[first] > mbtiCount[second]) {
        mbtiResult += first;
      } else if (mbtiCount[first] < mbtiCount[second]) {
        mbtiResult += second;
      } else {
        // 만약 두 값이 같으면 랜덤으로 선택
        mbtiResult += Math.random() < 0.5 ? first : second;
      }
    });

    console.log('최종 MBTI 결과:', mbtiResult);

      },
    },
  };

/*
ISTP,ENTP,ESFP,ESTP:
인생을 거는 한방형
- 단기간에 큰 수익원함
- 고위험 고수익
- 일확천금을 노리고 리스크를 감수함

ENTJ, ISTJ, ESTJ, ISFJ:
데이터로 증명하는 분석형
- 열심히 공부하며 투자함
- 재무제표, 시장트렌드, 관련 뉴스를 따져 투자함

ENFP, INFP, ISFP, ESFJ,
친구따라 강남가는 손민수형
- 친구가 사는 종목 따라함
- 친구와 함께 물리고 떡상기원

ENFJ, INTJ, INFJ, INTP:
미래를 내다보는 예언자형
- 차트를 예측하며 주변에 알려줌
- 주로 손민수형이 많이 의지하는 스타일

*/
</script>



<style scoped>
/* 필요한 스타일을 추가하세요 */
</style>
  