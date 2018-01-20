<template>
  <div v-if="havePartner" class="partner-type">
    <div class="partner-type-title">
      {{ type.name }}
    </div>
    <partner v-for="partner in partners"
             v-bind:partner="partner">
    </partner>
  </div>
</template>

<script>
import Partner from './Partner.vue'
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
export default {
  components: {
    Partner,
  },
  props: {
    type: [Object]
  },
  data () {
    return {
      partners: [],
    }
  },
  computed: {
    havePartner () {
      return this.partners.length ? true : false;
    }
  },
  created () {
    let url = 'apiv1/partners/type/' + this.type.id + '/list/';
    axios.get(url)
      .then((response) => {
        this.partners = response.data;
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>
.partner-type-title {
  font-family: "Circular-Pro-Bold";
  color: #501cd7;
  font-size: 2.7vw;
  font-weight: bold;
}
</style>
