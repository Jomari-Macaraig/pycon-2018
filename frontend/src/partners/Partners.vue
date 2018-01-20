<template>
  <div class="partners-section">
    <div class="content">
      <div class="partner-title">
        Partner
      </div>
      <partner-type v-for="type in partnerTypes"
                    v-bind:type="type">
      </partner-type>
    </div>
  </div>
</template>

<script>
import PartnerType from './PartnerType.vue'
import axios from 'axios'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
export default {
  components: {
    PartnerType,
  },
  data () {
    return {
      partnerTypes: []
    }
  },
  created () {
    let url = 'apiv1/partners/type/list/';
    axios.get(url)
      .then((response) => {
        this.partnerTypes = response.data;
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>
.partners-section > .content {
  margin-top: 7vw;
  margin-left: 7vw;
}
.partner-title {
  font-family: "Circular-Pro-Bold";
  color: #501cd7;
  font-size: 6vw;
  font-weight: bold;
}
</style>
