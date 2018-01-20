<template>
  <section class="sponsors-section">
    <div class="content">
      <div class="title">
        Sponsors
      </div>
      <sponsor-type v-for="type in sponsorTypes"
                    v-bind:type="type">
      </sponsor-type>
    </div>
  </section>
</template>

<script>
import SponsorType from './SponsorType.vue'
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
export default {
  components: {
    SponsorType,
  },
  data () {
    return {
      sponsorTypes: []
    }
  },
  created () {
    let url = 'apiv1/sponsors/type/list/';
    axios.get(url)
      .then((response) => {
        this.sponsorTypes = response.data;
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>
</style>
