import { defineStore } from 'pinia'

export const useModalStore = defineStore('modal', {
  state: () => ({
    isVisible: false,
    message: ''
  }),
  actions: {
    showModal(message) {
      this.isVisible = true
      this.message = message
    },
    hideModal() {
      this.isVisible = false
      this.message = ''
    }
  }
})