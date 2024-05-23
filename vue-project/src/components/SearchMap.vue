<template>
  <div>
    <div id="map">
      <div id="menu_wrap" class="search-container bg_white">
        <form class="pb-3" @submit.prevent="searchPlaces()">
          <label for="search-keyword">키워드: </label>
          <input type="text" class="search-input" name="search-keyword" v-model="keyword">
          <button type="submit">검색</button>
        </form>
        <ul id="placesList">
          <li v-for="(place, index) in places" :key="index" :class="{ 'selected': selectedPlaceIndex === index }" @click="selectPlace(index)">
            <span class="markerbg" :style="{ backgroundPosition: getMarkerImagePosition(index) }"></span>
            <div class="info">
              <h5>{{ place.place_name }}</h5>
              <span v-if="place.road_address_name">{{ place.road_address_name }}</span>
              <span v-if="!place.road_address_name">{{ place.address_name }}</span>
              <span class="jibun gray" v-if="place.road_address_name">{{ place.address_name }}</span>
              <span class="tel">{{ place.phone }}</span>
            </div>
          </li>
        </ul>
        <div id="pagination"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useLocationStore } from '@/stores/location';

const API_KEY = '79ffb8aa8de81e90c809a960dbc3bb4e';

const locationStore = useLocationStore();
const keyword = ref('');
const places = ref([]);
const selectedPlaceIndex = ref(null);

let map = null;
let markers = [];
let infowindow = null;

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

const initMap = () => {
  const container = document.getElementById('map');
  const options = {
    center: new kakao.maps.LatLng(locationStore.latitude, locationStore.longitude),
    level: 5,
  };

  map = new kakao.maps.Map(container, options);

  const mapTypeControl = new kakao.maps.MapTypeControl();
  map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

  const zoomControl = new kakao.maps.ZoomControl();
  map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

  infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
};

const searchPlaces = () => {
  if (!keyword.value.trim()) {
    alert('키워드를 입력해주세요!');
    return false;
  }

  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(keyword.value, (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
      places.value = data;
      displayPlaces(data);
      displayPagination(pagination);
    } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
      alert('검색 결과가 존재하지 않습니다.');
    } else if (status === kakao.maps.services.Status.ERROR) {
      alert('검색 결과 중 오류가 발생했습니다.');
    }
  });
};

const displayPlaces = (places) => {
  const bounds = new kakao.maps.LatLngBounds();
  removeMarkers();

  places.forEach((place, i) => {
    const placePosition = new kakao.maps.LatLng(place.y, place.x);
    const marker = addMarker(placePosition, i);
    
    bounds.extend(placePosition);

    kakao.maps.event.addListener(marker, 'click', () => {
      selectPlace(i);
    });
  });

  map.setBounds(bounds);
};

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

const removeMarkers = () => {
  markers.forEach(marker => marker.setMap(null));
  markers = [];
};

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

const displayInfowindow = (marker, title) => {
  const content = `<div style="padding:5px;z-index:1;font-size:12px;width:200px;white-space:normal;">${title}</div>`;
  infowindow.setContent(content);
  infowindow.open(map, marker);
};

const selectPlace = (index) => {
  selectedPlaceIndex.value = index;
  const place = places.value[index];
  const marker = markers[index];
  displayInfowindow(marker, place.place_name);
  map.setCenter(new kakao.maps.LatLng(place.y, place.x));
};

const getMarkerImagePosition = (index) => {
  return `0px ${(index * -46)-10}px`; // 마커 이미지의 위치를 조정합니다.
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

.search-container > form {
  border-bottom: 1px solid #C2C4C1;
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

#placesList > li {
  padding: 10px 0px;
  border-bottom: 1px solid #C2C4C1;
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

.selected {
  background-color: #f0f0f0;
}

.markerbg {
  display: inline-block;
  width: 36px;
  height: 37px;
  background: url('https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png') no-repeat;
  background-size: 36px 691px;
}
</style>
