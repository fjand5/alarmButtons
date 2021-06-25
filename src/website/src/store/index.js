import Vue from 'vue'
import Vuex from 'vuex'
import Buttons from './modules/listButton'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    Buttons
  },
})