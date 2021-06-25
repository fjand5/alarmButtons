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
      collapseDuration: 0
    }
  },
  methods: {
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
  created: function(){
    addOnOpen(()=>{
      this.updateButtons()
    })
    addOnMessages(()=>{
      this.updateButtons()
    })
  }
}
</script>

<style>

</style>