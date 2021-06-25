<template>
 <div>
    <CAlert
      color="info"
      :show.sync="openAlertCounter"
      closeButton
    >
      Đã kết nối với hệ thống
    </CAlert>

    <CAlert
      color="danger"
      :show.sync="closeAlertCounter"
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
      openAlertCounter:0,
      closeAlertCounter:0
    }
  },
  name: 'App',
  created: function(){
    addOnOpen(()=>{
      this.openAlertCounter = 10
      this.closeAlertCounter =0

    })
    addOnClose(()=>{
      this.openAlertCounter = 0
      this.closeAlertCounter = 10
      setTimeout(() => {
        init()
      }, 3000);
      
    })
    init()
  },
  mounted:function(){
         console.log("mounted");

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
