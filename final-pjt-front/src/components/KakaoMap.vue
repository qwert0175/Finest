<template>
    <div>
      <div id="map"></div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  const API_KEY = '79ffb8aa8de81e90c809a960dbc3bb4e'
  import { useLocationStore } from '@/stores/location';
  const locationStore = useLocationStore();

  let map = null;
  
  // 마운트 되었을 때
  onMounted(() => {
    if (window.kakao && window.kakao.maps) {
      initMap();
    } else {
      const script = document.createElement('script');
      /* global kakao */
      script.onload = () => kakao.maps.load(initMap);
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${API_KEY}&libraries=services`;
      document.head.appendChild(script);
    }
  });

  // 지도 그리기
  const initMap = () => {
    const infowindow = new kakao.maps.InfoWindow({zIndex:1});
    const container = document.getElementById('map');
    const options = {
      // center: new kakao.maps.LatLng(35.20916389, 128.9829083),
      center: new kakao.maps.LatLng(locationStore.latitude, locationStore.longitude),
      level: 5,
    };
  
    // 지도 객체를 등록합니다.
    // 지도 객체는 반응형 관리 대상이 아니므로 initMap에서 선언합니다.
    map = new kakao.maps.Map(container, options);

    // 일반 지도와 스카이뷰로 지도 타입을 전환할 수 있는 지도타입 컨트롤을 생성합니다
    var mapTypeControl = new kakao.maps.MapTypeControl();

    // 지도에 컨트롤을 추가해야 지도위에 표시됩니다
    // kakao.maps.ControlPosition은 컨트롤이 표시될 위치를 정의하는데 TOPRIGHT는 오른쪽 위를 의미합니다
    map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT)

    // 줌 컨트롤
    var zoomControl = new kakao.maps.ZoomControl();
    map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
    
    // 장소 검색 객체를 생성합니다
    var ps = new kakao.maps.services.Places(map);

    // 카테고리로 은행을 검색합니다
    ps.categorySearch('BK9', placesSearchCB, {useMapBounds:true});

    function placesSearchCB (data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {
            for (var i=0; i<data.length; i++) {
                displayMarker(data[i]);    
            }       
        }
    }

    // 지도에 마커를 표시하는 함수입니다
    function displayMarker(place) {
        // 마커를 생성하고 지도에 표시합니다
        var marker = new kakao.maps.Marker({
            map: map,
            position: new kakao.maps.LatLng(place.y, place.x) 
        });

        // 마커에 클릭이벤트를 등록합니다
        kakao.maps.event.addListener(marker, 'click', function() {
            // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
            infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
            infowindow.open(map, marker);
        });
    }

    // 지도 드래그 이벤트 발생시
    kakao.maps.event.addListener(map, 'dragend', function() {
      // 은행 재검색
      ps.categorySearch('BK9', placesSearchCB, {useMapBounds:true});
    });

    // 지도 확대/축소 이벤트 발생시
    kakao.maps.event.addListener(map, 'zoom_changed', function() {     
      // 은행 재검색
      ps.categorySearch('BK9', placesSearchCB, {useMapBounds:true});
    });
  };
  
  </script>

  <style scoped>
  #map {
    min-width: 400px;
    width: 80vw;
    min-height: 400px;
    height: 70vh;
  }
  </style>