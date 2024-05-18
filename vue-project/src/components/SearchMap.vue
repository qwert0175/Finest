<template>
    <div>
      <div id="map">
        <div id="menu_wrap" class="search-container bg_white">
            <form @submit.prevent="searchPlaces()">
                <label for="search-keyword">키워드: </label>
                <input type="text" class="search-input" name="search-keyword" v-model="keyword">
                <button type="submit">검색</button>
            </form>
            <hr>
            <ul id="placesList">
            </ul>
            <ul id="placesList"></ul>
            <div id="pagination"></div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useLocationStore } from '@/stores/location';
  
  // API 키 상수
  const API_KEY = '79ffb8aa8de81e90c809a960dbc3bb4e';
  
  // 상태 변수
  const locationStore = useLocationStore();
  const keyword = ref('');
  
  // 지도 관련 변수
  let map = null;
  let markers = [];
  let infowindow = null;
  
  // 컴포넌트가 마운트될 때 지도를 초기화하는 함수 호출
  onMounted(() => {
    if (window.kakao && window.kakao.maps) {
      initMap();
    } else {
      const script = document.createElement('script');
      script.onload = () => kakao.maps.load(initMap);
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}&libraries=services`;
      document.head.appendChild(script);
    }
  });
  
  // 지도 초기화 함수
  const initMap = () => {
    const container = document.getElementById('map');
    const options = {
      center: new kakao.maps.LatLng(locationStore.latitude, locationStore.longitude),
      level: 5,
    };
  
    // 지도 객체 생성
    map = new kakao.maps.Map(container, options);
  
    // 지도 타입 컨트롤 생성 및 추가
    const mapTypeControl = new kakao.maps.MapTypeControl();
    map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);
  
    // 줌 컨트롤 생성 및 추가
    const zoomControl = new kakao.maps.ZoomControl();
    map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
  
    // 검색 결과 인포윈도우 생성
    infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
  };
  
  // 장소 검색 함수
  const searchPlaces = () => {
    if (!keyword.value.trim()) {
      alert('키워드를 입력해주세요!');
      return false;
    }
  
    // 키워드로 장소 검색
    const ps = new kakao.maps.services.Places();
    ps.keywordSearch(keyword.value, (data, status, pagination) => {
      if (status === kakao.maps.services.Status.OK) {
        displayPlaces(data);
        displayPagination(pagination);
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert('검색 결과가 존재하지 않습니다.');
      } else if (status === kakao.maps.services.Status.ERROR) {
        alert('검색 결과 중 오류가 발생했습니다.');
      }
    });
  };
  
  // 검색 결과 목록과 마커를 표시하는 함수
  const displayPlaces = (places) => {
    const listEl = document.getElementById('placesList');
    const fragment = document.createDocumentFragment();
    const bounds = new kakao.maps.LatLngBounds();
  
    // 기존 검색 결과 제거
    removeAllChildNodes(listEl);
    removeMarkers();
  
    // 검색 결과를 기반으로 마커와 목록 생성
    places.forEach((place, i) => {
      const placePosition = new kakao.maps.LatLng(place.y, place.x);
      const marker = addMarker(placePosition, i);
      const itemEl = createListItem(i, place);
  
      bounds.extend(placePosition);
  
      kakao.maps.event.addListener(marker, 'mouseover', () => displayInfowindow(marker, place.place_name));
      kakao.maps.event.addListener(marker, 'mouseout', () => infowindow.close());
  
      itemEl.onmouseover = () => displayInfowindow(marker, place.place_name);
      itemEl.onmouseout = () => infowindow.close();
  
      fragment.appendChild(itemEl);
    });
  
    // 검색 결과 목록에 추가
    listEl.appendChild(fragment);
  
    // 지도 범위 재설정
    map.setBounds(bounds);
  };
  
  // 검색 결과 항목 생성 함수
  const createListItem = (index, place) => {
    const el = document.createElement('li');
    let itemStr = `
      <span class="markerbg marker_${index + 1}"></span>
      <div class="info">
        <h5>${place.place_name}</h5>
    `;
  
    if (place.road_address_name) {
      itemStr += `
        <span>${place.road_address_name}</span>
        <span class="jibun gray">${place.address_name}</span>
      `;
    } else {
      itemStr += `<span>${place.address_name}</span>`;
    }
  
    itemStr += `
      <span class="tel">${place.phone}</span></div>
      <hr>`;
    el.innerHTML = itemStr;
    el.className = 'item';
    return el;
  };
  
  // 마커 생성 함수
  const addMarker = (position, idx) => {
    const imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png';
    const imageSize = new kakao.maps.Size(36, 37);
    const imgOptions = {
      spriteSize: new kakao.maps.Size(36, 691),
      spriteOrigin: new kakao.maps.Point(0, (idx * 46) + 10),
      offset: new kakao.maps.Point(13, 37),
    };
    const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions);
    const marker = new kakao.maps.Marker({ position, image: markerImage });
    marker.setMap(map);
    markers.push(marker);
    return marker;
  };
  
  // 마커 제거 함수
  const removeMarkers = () => {
    markers.forEach(marker => marker.setMap(null));
    markers = [];
  };
  
  // 페이지네이션 표시 함수
  const displayPagination = (pagination) => {
    const paginationEl = document.getElementById('pagination');
    const fragment = document.createDocumentFragment();
    while (paginationEl.hasChildNodes()) {
      paginationEl.removeChild(paginationEl.lastChild);
    }
  
    for (let i = 1; i <= pagination.last; i++) {
      const el = document.createElement('a');
      el.href = '#';
      el.innerHTML = i;
      if (i === pagination.current) {
        el.className = 'on';
      } else {
        el.onclick = (function(i) {
          return () => pagination.gotoPage(i);
        })(i);
      }
      fragment.appendChild(el);
    }
    paginationEl.appendChild(fragment);
  };
  
  // 인포윈도우 표시 함수
  const displayInfowindow = (marker, title) => {
    const content = `<div style="padding:5px;z-index:1;">${title}</div>`;
    infowindow.setContent(content);
    infowindow.open(map, marker);
  };
  
  // 자식 요소 제거 함수
  const removeAllChildNodes = (el) => {
    while (el.hasChildNodes()) {
      el.removeChild(el.lastChild);
    }
  };

  </script>
  
<style scoped>
#map {
    position: relative;
    min-width: 400px;
    width: 80vw;
    min-height: 400px;
    height: 70vh;
}
  
.search-container {
    line-height: 1.6;
    color: rgb(51, 51, 51);
    word-wrap: break-word;
    position: absolute;
    left: 1%;
    top: 3%;
    width: 260px;
    height: 90%;
    margin: 10px 0 30px 10px;
    padding: 5px;
    overflow-y: auto;
    background: rgba(255, 255, 255, 0.7);
    z-index: 2;
    font-size: 12px;
    border-radius: 10px;
}
  
.search-input {
    width: 150px;
}

#placesList {
    line-height: 1.6;
    color: rgb(51, 51, 51);
    overflow-wrap: break-word;
    list-style: none;
    margin: 0;
    padding: 0;
    font-size: 12px;
}

#pagination {
    display: flex;
    justify-content: space-evenly;
    line-height: 1.6;
    color: rgb(51, 51, 51);
    overflow-wrap: break-word;
    padding: 0;
    font-size: 12px;
    margin: 10px auto;
    text-align: center;
}
</style>
  