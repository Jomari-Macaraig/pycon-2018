<template>
  <div class="schedules">
    <div class="schedules-title">
      {{ day }}
    </div>
    <topic v-for="schedule in schedules"
           v-bind:topic="schedule">
    </topic>
  </div>
</template>

<script>
import Topic from './Topic.vue'
export default {
  components: {
    Topic,
  },
  props: {
    schedules: [Object],
    day: [String]
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
</style>

