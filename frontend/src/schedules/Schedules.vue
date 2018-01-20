<template>
  <div id="schedule-section">
    <div id="schedule-content">
      <div class="title">
        Schedule
      </div>
      <div class="container">
        <div class="row">
          <div class="col-sm-5">
            <schedule v-bind:schedules="scheduleDay1"
                      v-bind:day="'Feb 24'"></schedule>
          </div>
          <div class="col-sm-5">
            <schedule v-bind:schedules="scheduleDay2"
                      v-bind:day="'Feb 25'"></schedule>
          </div>
          </div>
          <div class="col-sm-2"></div>
        </div>
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
      scheduleDay1: [],
      scheduleDay2: [],
    }
  },
  created () {
    let day1 = 'apiv1/schedule/day/1/';
    axios.get(day1)
      .then((response) => {
        this.scheduleDay1 = response.data;
      })
      .catch((error) => {
        console.log(error)
      })
    let day2 = 'apiv1/schedule/day/2/';
    axios.get(day2)
      .then((response) => {
        this.scheduleDay2 = response.data;
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
