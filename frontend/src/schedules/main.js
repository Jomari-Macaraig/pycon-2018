import Vue from 'vue'
import Schedules from './Schedules.vue'
import Tooltip from 'vue-directive-tooltip';
import 'vue-directive-tooltip/css/index.css';
Vue.use(Tooltip);

new Vue({
  el: '#schedules',
  render: h => h(Schedules)
})
