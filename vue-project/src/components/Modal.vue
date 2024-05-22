<template>
  <div class="modal-overlay" v-if="isVisible">
    <div class="modal-content">
      <p>{{ message }}</p>
      <button class="confirm-button" @click="closeModal">확인</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useModalStore } from '@/stores/modal'

const modalStore = useModalStore()
const isVisible = ref(false)
const message = ref('')

modalStore.$subscribe((mutation, state) => {
  isVisible.value = state.isVisible
  message.value = state.message
})

const closeModal = () => {
  modalStore.hideModal()
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 30%; /* Adjust this value to fit your needs */
  width: 100%;
  margin: 0 auto;
}

.confirm-button {
  background-color: #007bff;
  color: white;
  padding: 5px 10px; /* Adjust padding for a better size */
  border: none;
  border-radius: 5px; /* Slightly rounded corners */
  cursor: pointer;
  font-size: 0.8em; /* Standard font size */
  width: fit-content; /* Fit the button to the content */
  margin: 0 auto; /* Center the button */
}

.confirm-button:hover {
  background-color: #0056b3;
}
</style>