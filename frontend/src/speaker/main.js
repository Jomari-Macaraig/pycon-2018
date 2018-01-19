import Vue from 'vue'
import Keynotes from './Keynotes.vue'
import Speakers from './Speakers.vue'
import Tooltip from 'vue-directive-tooltip';
import 'vue-directive-tooltip/css/index.css';
Vue.use(Tooltip);

new Vue({
  el: '#keynotes',
  render: h => h(Keynotes)
})

new Vue({
  el: '#speakers',
  render: h => h(Speakers)
})

