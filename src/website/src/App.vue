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
  </div>
</template>

<script>
import { init, setOnClose, setOnOpen} from './connect/ws/InitWebsocket'
export default {
  data: function(){
    return {
      openAlertCounter:0,
      closeAlertCounter:0
    }
  },
  name: 'App',
  created: function(){
    setOnOpen(()=>{
      this.openAlertCounter = 10,
      this.closeAlertCounter =0
    })
    setOnClose(()=>{
      this.openAlertCounter = 0,
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
