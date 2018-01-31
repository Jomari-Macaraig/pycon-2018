<template>
  <div id="schedule-section">
    <div id="schedule-content">
      <div class="title" v-if="hasSchedule">
        Schedule
      </div>
      <div class="title" v-if="!hasSchedule">
        Schedule (Coming soon)
      </div>
      <schedule v-bind:tracks="tracksDay1"
                v-bind:day="'1'"
                v-bind:day_title="'Feb 24'">
      </schedule>
      <schedule v-bind:tracks="tracksDay2"
                v-bind:day="'2'"
                v-bind:day_title="'Feb 25'">
      </schedule>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Schedule from './Schedule.vue'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  components: {
    Schedule,
  },
  data () {
    return {
      tracksDay1: [],
      tracksDay2: [],
    }
  },
  computed: {
    hasSchedule () {
      let hasSchedule = this.tracksDay1.length || this.tracksDay2.length ? true : false;
      return hasSchedule;
    }
  },
  created () {
    let day1 = 'apiv1/schedule/day/1/tracks/';
    axios.get(day1)
      .then((response) => {
        this.tracksDay1 = response.data;
      })
      .catch((error) => {
        console.log(error)
      })
    let day2 = 'apiv1/schedule/day/2/tracks/';
    axios.get(day2)
      .then((response) => {
        this.tracksDay2 = response.data;
      })
      .catch((error) => {
        console.log(error)
      })
  }
}

</script>


<style>
#schedule-section {
  background-color: #e1e1e1;
  min-height: 120vw;
  background-image: url(../assets/schedules/schedule-bottom.png),
                    url(../assets/schedules/schedule-3.png),
                    url(../assets/schedules/schedule-2.png),
                    url(../assets/schedules/schedule-1.png);
  background-repeat: no-repeat;
  background-position: bottom, right, left 25%, 95% 5%;
  background-size: contain, 20vw, 15vw, 20vw;
  display: flex;
  flex-wrap: wrap;
}

#schedule-content {
  padding-top: 7vw;
  padding-left: 7vw;
}

#schedule-content > .title {
  font-family: "Circular-Pro-Bold";
  color: #501cd7;
  font-size: 6vw;
  font-weight: bold;
}
</style>
