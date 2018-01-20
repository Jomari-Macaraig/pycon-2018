<template>
  <div class="other-speakers">
    <div class="container">
      <div class="row">
        <speaker v-for="speaker in speakers"
                 :id="speaker.id"
                 :name="speaker.name"
                 :company_name="speaker.company_name"
                 :job_title="speaker.job_title"
                 :description="speaker.description"
                 :image="speaker.image">
        </speaker>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Speaker from './Speaker.vue'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
export default {
  components: {
    Speaker,
  },
  data () {
    return {
      speakers: []
    }
  },
  created () {
    let url = 'apiv1/speakers/normal/list/';
    axios.get(url)
      .then((response) => {
        this.speakers = response.data;
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>


<style>
</style>


