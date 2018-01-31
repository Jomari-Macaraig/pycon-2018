<template>
  <div class="tracks">
    <topic v-for="schedule in schedules"
           v-bind:topic="schedule">
    </topic>
  </div>
</template>

<script>
import Topic from './Topic.vue'
import axios from 'axios'
export default {
  components: {
    Topic,
  },
  props: {
    track: [String],
    day: [String]
  },
  data () {
    return {
      schedules: []
    }
  },
  created () {
    let url = 'apiv1/schedule/day/' + this.day + '/track/' + this.track + '/';
    axios.get(url)
      .then((response) => {
        this.schedules = response.data;
      })
      .catch((error) => {
        console.log(error)
      })
  }
}

</script>


<style>
.tracks {
  min-height: 30vw;
}
</style>
