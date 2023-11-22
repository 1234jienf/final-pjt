<template>
  <article class="search-page">
    <p class="search-page__title">은행 찾기</p>
    <div class="search-page__detail">
      <div class="search-page__detail__settings">
        <!-- <input type="text" v-model="keyWord"> -->
        <select name="city" id="" v-model="currentCity" class="search-page__detail__settings__input">
          <option value=""></option>
          <option v-for="city in citys" :key="city" :value="city">{{ city }}</option>
        </select>
        <select v-show="currentCity != ''" name="goo" id="" v-model="currentGoo"
          class="search-page__detail__settings__input">
          <option value=""></option>
          <option v-for="city in goo[currentCity]" :key="city" :value="city">{{ city }}</option>
        </select>
        <select name="bank" id="" v-model="currentBank" class="search-page__detail__settings__input">
          <option value=""></option>
          <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
        </select>
        <button @click="searchInfo" class="search-page__detail__settings__input">검색</button>
      </div>
      <div id="map" class="kakao-map" style="width: 1000px; height:500px;"></div>
    </div>
    <div v-show="listItem" id="menu_wrap" class="search-page__list">
      <ul id="placesList">
        <div class="search-page__list__items">
          <li class="search-page__list__items__item" v-for="item in listItem" @mouseenter="item.onMouse" @mouseleave="item.onMouseOut">
            <span :class="'markerbg marker_' + item.id">
              <div class="info">
                <p>{{ item.place_name }}</p>
                <p v-if="item.road_address_name">{{ item.road_address_name }}</p>
                <p v-if="item.address_name">{{ item.address_name }}</p>
                <p class="tel" v-if="item.phone">{{ item.phone }}</p>
              </div>
            </span>
          </li>
        </div>
      </ul>
      <div id="pagination">
        <div v-show="lastPage" class="pagination">
          <a v-for="i of lastPage" @click="goNext(i)">{{ i }}</a>
        </div>
      </div>
    </div>
  </article>
</template>


<script setup>
/* global kakao */
import { Fragment, onMounted, ref } from "vue"
const markers = ref([])
const currentCity = ref("")
const currentGoo = ref("")
const currentBank = ref("")
const citys = ref([
  '서울시', '부산시', '대구시', '인천시', '광주시', '대전시', '울산시', '세종시', '제주시', '경기도', '강원도', '충청북도', '층청남도', '전라북도', '전라남도', '경상북도', '경상남도'
])

const goo = ref({
  서울시: ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구'],
  부산시: ['중구', '서구', '동구', '영도구', '부산진구', '동래구', '남구', '북구', '강서구', '해운대구', '사하구', '금정구', '연제구', '수영구', '사상구'],
  대구시: ['중구', '동구', '서구', '남구', '북구', '수성구', '달서구', '달성군', '군위군'],
  인천시: ['중구', '동구', '미추홀구', '연수구', '남동구', '부평구', '계양구', '서구', '강화군', '옹진군'],
  광주시: ['동구', '서구', '남구', '북구', '광산구'],
  대전시: ['동구', '중구', '서구', '유성구', '대덕구'],
  울산시: ['중구', '남구', '동구', '북구', '울주군'],
  세종시: ['조치원읍', '연기면', '연동면', '부강면', '금남면', '장군면', '연서면', '전의면', '전동면', '소정면', '한솔동', '새롬동', '나성동', '도담동', '어진동', '해밀동', '아름동', '종촌동', '고운동', '소담동', '반곡동', '보람동', '대평동', '다정동'],
  경기도: ['수원시 장안구', '수원시 권선구', '수원시 팔달구', '수원시 영통구', '성남시 수정구', '성남시 중원구', '성남시 분당구', '의정부시', '안양시 만안구', '안양시 동안구', '부천시', '광명시', '동두천시', '평택시', '안산시 상로구', '안산시 단원구', '고양시 덕양구', '고양시 일산동구', '고양시 일산서구', '과천시', '구리시', '남양주시', '오산시', '시흥시', '군포시', '의왕시', '하남시', '용인시 처인구', '용인시 기흥구', '용인시 수지구', '파주시', '이천시', '안성시', '김포시', '화성시', '광주시', '양주시', '포천시', '여주시', '연천군', '가평군', '양평군'],
  강원도: ['춘천시', '원주시', '강릉시', '동해시', '태백시', '속초시', '삼척시', '홍천군', '횡성군', '영월군', '평창군', '정선군', '철원군', '화천군', '양구군', '인제군', '고성군', '양양군'],
  충청북도: ['청주시 상당구', '청주시 흥덕구', '청주시 서원구', '청주시 청원구', '충주시', '제천시', '보은군', '옥천군', '영동군', '증평군', '진천군', '괴산군', '음성군', '단양군'],
  충청남도: ['천안시 동남구', '천안시 서북구', '공주시', '보령시', '아산시', '서산시', '논산시', '계룡시', '당진시', '금산군', '부여군', '서천군', '청양군', '홍성군', '예산군', '태안군'],
  전라북도: ['전주시 완산구', '전주시 덕진구', '군산시', '익산시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군', '장수군', '임실군', '순창군', '고창군', '부안군'],
  전라남도: ['목포시', '여수시', '순천시', '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군', '장흥군', '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군', '진도군', '신안군'],
  경상북도: ['포항시 남구', '포항시 북구', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시', '상주시', '문경시', '경산시', '의성군', '청송군', '영양군', '영덕군', '청도군', '고령군', '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군'],
  경상남도: ['창원시 의창구', '창원시 성산구', '창원시 마산합포구', '창원시 마산회원구', '창원시 진해구', '진주시', '통영시', '사천시', '김해시', '밀양시', '거제시', '양산시', '의령군', '함안군', '창녕군', '고성군', '남해군', '하동군', '산청군', '함양군', '거창군', '합천군'],
  제주시: ['행정시 제주시', '행정시 서귀포시']
})

const banks = ref([
  '한국은행', 'KB국민은행', '신한은행', '우리은행', '하나은행', 'SC제일은행', '한국씨티은행', '한국산업은행', '중소기업은행', '한국수출입은행', 'NH농협은행', '수협은행', '대구은행', '부산은행', '경남은행', '광주은행', '전북은행', '제주은행'
])
const answer_bank = ref(null)
const keyWord = ref("")
const searchInfo = ref(null)
const listItem = ref(null)
const lastPage = ref(null)
const pageInfo = ref(null)

function goNext(item) {
  pageInfo.value.gotoPage(item)
}
onMounted(() => {
  window.kakao.maps.load(() => {
    var infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
    function addMarker(position, idx, title) {
      var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
        imageSize = new kakao.maps.Size(36, 37),  // 마커 이미지의 크기
        imgOptions = {
          spriteSize: new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
          spriteOrigin: new kakao.maps.Point(0, (idx * 46) + 10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
          offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
        },
        markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
        marker = new kakao.maps.Marker({
          position: position, // 마커의 위치
          image: markerImage
        });
      marker.setMap(map); // 지도 위에 마커를 표출합니다
      markers.value.push(marker)

      return marker
    }
    const mapContainer = document.getElementById('map');
    const mapOption = {
      center: new window.kakao.maps.LatLng(37.50113609804342, 127.03956361067294),
      level: 3
    }
    const map = new kakao.maps.Map(mapContainer, mapOption)
    addMarker(new kakao.maps.LatLng(37.50113609804342, 127.03956361067294), 0)
    var ps = new kakao.maps.services.Places();

    searchInfo.value = () => {
      if (!currentCity.value.replace(/^\s+|\s+$/g, '')) {
        alert('시를 선택해주세요!');
        return false;
      }

      if (!currentGoo.value.replace(/^\s+|\s+$/g, '')) {
        alert("구를 선택해주세요!");
        return false;
      }
      keyWord.value = currentCity.value + " " + currentGoo.value + " " + currentBank.value
      ps.keywordSearch(keyWord.value, placesSearchCB, { page: 1 })
    }

    function placesSearchCB(data, status, pagination) {
      listItem.value = []
      if (status === kakao.maps.services.Status.OK) {
        displayPlaces(data)
        lastPage.value = pagination.last
        pageInfo.value = pagination
        // displayPage(pagination)
        keyWord.value = ""
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert('검색 결과가 존재하지 않습니다.');
        keyWord.value = ""
        return
      } else if (status === kakao.maps.services.Status.ERROR) {
        alert('검색 결과 중 오류가 발생했습니다.');
        keyWord.value = ""
        return;
      }
    }
    function removeMarker() {
      for (var i = 0; i < markers.value.length; i++) {
        markers.value[i].setMap(null);
      }
      markers.value = [];
    }

    function displayPlaces(places) {
      const menuEl = document.getElementById('menu_wrap'),
        bounds = new kakao.maps.LatLngBounds()
      // 지도에 표시되고 있는 마커를 제거합니다
      removeMarker();

      for (var i = 0; i < places.length; i++) {

        // 마커를 생성하고 지도에 표시합니다
        const placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
          marker = addMarker(placePosition, i),
          itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다
        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        bounds.extend(placePosition);

        // 마커와 검색결과 항목에 mouseover 했을때
        // 해당 장소에 인포윈도우에 장소명을 표시합니다
        // mouseout 했을 때는 인포윈도우를 닫습니다
        (function (marker, title) {
          kakao.maps.event.addListener(marker, 'mouseover', function () {
            displayInfowindow(marker, title);
          });

          kakao.maps.event.addListener(marker, 'mouseout', function () {
            infowindow.close();
          });

          itemEl[0].onMouse = function () {
            displayInfowindow(marker, title);
          };

          itemEl[0].onMouseOut = function () {
            infowindow.close();
          };
          listItem.value.push(itemEl[0])
        })(marker, places[i].place_name);
      }
      menuEl.scrollTop = 0;
      // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
      map.setBounds(bounds);
    }

    function displayInfowindow(marker, title) {
      var content = '<div style="padding:5px;z-index:1;">' + title + '</div>';

      infowindow.setContent(content);
      infowindow.open(map, marker);
    }

    function getListItem(index, places) {
      const listObject = []
      if (places.road_address_name) {
        listObject.push({
          id: index,
          place_name: places.place_name,
          road_address_name: places.road_address_name,
          address_name: places.address_name,
          phone: places.phone,
          onMouse: null,
          onMouseOut: null,
        })
      } else {
        listObject.push({
          id: index,
          place_name: places.place_name,
          address_name: places.address_name,
          phone: places.phone,
          onMouse: null,
          onMouseOut: null,
        })
      }
      return listObject
    }
  })
})
</script>


<style scoped>
.search-page {
  /* 배경색 */
  background-color: #EAEFFE;
}

/* 다양한 요소에 사용할 클래스들 */
.search-page__title {
    width: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    color: #000000;
}

.search-page__detail {
  background-color: #EAEFFE;
  /* 다른 스타일 지정 */
}

.search-page__detail__settings__input {
  margin: 5px;
  padding: 8px;
  border: 1px solid #526ADF;
  border-radius: 4px;
  font-size: 14px;
  color: #526ADF;
}

/* 검색 버튼 스타일 */
.search-page__detail__settings__input[type="button"] {
  background-color: #526ADF;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-page__detail__settings__input[type="button"]:hover {
  background-color: #4054B2;
}

/* 리스트 스타일 */
.search-page__list__items__item {
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #526ADF;
  border-radius: 4px;
  background-color: #ffffff;
  transition: transform 0.2s ease;
}

.search-page__list__items__item:hover {
  transform: translateY(-3px);
}

/* 페이지네이션 링크 스타일 */
.pagination a {
  display: inline-block;
  margin-right: 5px;
  padding: 5px 10px;
  color: #526ADF;
  border: 1px solid #526ADF;
  border-radius: 4px;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.pagination a:hover {
  background-color: #526ADF;
  color: white;
}
</style>