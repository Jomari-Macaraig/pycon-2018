<template>
  <div v-if="haveSponsor" class="sponsor-type">
    <div class="title">
      {{ type.name }}
    </div>
    <sponsor v-for="sponsor in sponsors"
             v-bind:sponsor="sponsor">
    </sponsor>
  </div>
</template>

<script>
import Sponsor from './Sponsor.vue'
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
export default {
  components: {
    Sponsor
  },
  props: {
    type: [Object]
  },
  data () {
    return {
      sponsors: [],
    }
  },
  computed: {
    haveSponsor () {
      return this.sponsors.length ? true : false;
    }
  },
  created () {
    let url = 'apiv1/sponsors/type/' + this.type.id + '/list/';
    axios.get(url)
      .then((response) => {
        this.sponsors = response.data;
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>
</style>
