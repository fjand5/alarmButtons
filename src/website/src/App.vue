<template>
 <div>
    <CAlert
    v-if="isConnect"
      color="info"
      closeButton
    >
      Đã kết nối với hệ thống
    </CAlert>

    <CAlert
    v-else
      color="danger"
      closeButton
    >
      Mất kết nối
    </CAlert>
    <ListButton/>
  </div>
</template>

<script>

import { init, addOnClose, addOnOpen} from './connect/ws/InitWebsocket'
import ListButton from './components/ListButton.vue'
export default {
  data: function(){
    return {
      isConnect: false
    }
  },
  name: 'App',
  created: function(){
    addOnOpen(()=>{
      this.isConnect = true

    })
    addOnClose(()=>{
      this.isConnect = false
      
    })
    init()
  },
  mounted:function(){  

 
 },
  components: {
    ListButton
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
@import '~@coreui/coreui/dist/css/coreui.css';
</style>
