<template>
<div>
  <CCardBody>
    <CDataTable
      :items="buttons"
      :fields="fields"
      column-filter
      hover
      sorter
    >      
      <template #received="{item, index}">
        <td class="py-1">
          <CButton
            v-if="item.status == false"
            color="primary"
            variant="outline"
            square
            size="sm"
            @click="recived(item, index)"
          >
            Tiếp nhận
          </CButton>
        </td>
      </template>
    </CDataTable>
  </CCardBody>
    <video ref="videoRef" 
    v-show="false"
    controls="" 
    ><source src="static/media/alarm.mp3" type="audio/mpeg"></video>

</div>
</template>

<script>

import {getButtonsData,clearButton} from '../connect/http/buttonApi'
import {addOnOpen, addOnMessages} from '../connect/ws/InitWebsocket'
const fields = [
  { key: 'macAddr', _style:'min-width:200px' },
  { key: 'buttonNum', _style:'min-width:100px;' },
  { key: 'status', _style:'min-width:100px;' },
  
  { key: 'received', _style:'min-width:100px;' }
]
export default {
  data () {
    return {
      buttons: [],
      fields,
      details: [],
      collapseDuration: 0,
    }
  },
  methods: {
    playSound: function(){
            this.$refs.videoRef.play();
        
        
    },
    recived: function(item){

      clearButton(item.id)
    },
    updateButtons: function(){
      getButtonsData()
      .then((data)=>{
        this.buttons = data.buttons
      })
      .catch(()=>{
        
      })
    },
  },
  mounted: function(){
        this.playSound()
  },
  created: function(){
    addOnOpen(()=>{
      this.updateButtons()
    })
    addOnMessages((mess)=>{
      if(mess.event == "ALARM"){
        this.$refs.videoRef.loop = true
         this.playSound();
      }else{
        this.$refs.videoRef.pause();
      }
      this.updateButtons()
    })
  }
}
</script>

<style>

</style>