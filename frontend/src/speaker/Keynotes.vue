<template>
  <div class="keynote">
    <div class="title">
      Keynote
    </div>
    <br/>
    <div class="container">
      <div class="row">
        <keynote v-for="speaker in speakers"
                 :id="speaker.id"
                 :name="speaker.name"
                 :company_name="speaker.company_name"
                 :job_title="speaker.job_title"
                 :description="speaker.description"
                 :image="speaker.image"></keynote>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Keynote from './Keynote.vue'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
export default {
  components: {
    Keynote,
  },
  data () {
    return {
      speakers: []
    }
  },
  created () {
    let url = 'apiv1/speakers/keynote/list/';
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

