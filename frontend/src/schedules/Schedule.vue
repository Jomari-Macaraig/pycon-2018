<template>
  <div class="schedules">
    <div class="schedules-title">
      {{ day_title }}
    </div>
    <div class="container">
      <div class="row">
        <div v-for="track in tracks"
             class="col-sm-4">
          <span class="track-name">
            {{ track.name }}
          </span>
          <tracks v-bind:day="day"
                 v-bind:track="track.id">
          </tracks>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Tracks from './Tracks.vue'
export default {
  components: {
    Tracks,
  },
  props: {
    tracks: [Object],
    day: [String],
    day_title: [String],
  },
  data () {
    return {
    }
  }
}

</script>


<style>
.schedules {
  margin-top: 2vw;
}
.schedules > .schedules-title {
  font-family: "Circular-Pro-Bold";
  color: #501cd7;
  font-size: 4vw;
  font-weight: bold;
}

.track-name {
  font-family: "Circular-Pro-Bold";
  color: #501cd7;
  font-size: 2.5vw;
  font-weight: bold;
}
</style>

