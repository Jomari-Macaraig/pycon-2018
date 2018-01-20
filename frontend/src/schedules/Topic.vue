<template>
  <div class="topic">
    <div class="row">
      <div class="col-sm-4 text-center">
        <avatar v-if="topic.speaker.name"
                :username="topic.speaker.name"
                :src="topic.speaker.image"
                :size="100"
                v-tooltip.right="{html: tooltipContent, offset: 30, delay: 0}">
        </avatar>
        <avatar v-if="!topic.speaker.name"
                username="PyCon"
                src="static/images/organizers/pythonph-logo.svg"
                :size="100"
                v-tooltip.right="{html: tooltipContent, offset: 30, delay: 0}">
        </avatar>
      </div>
      <div class="col-sm-8">
        <div class="topic-name">{{ topic.name }}</div>
        <div class="topic-time">
          {{ topic.start_time }} - {{ topic.end_time }}
        </div>
        <div v-if="topic.speaker.name">
          <div class="topic-speaker-name">{{ topic.speaker.name }}</div>
          <div class="topic-speaker-job-desc">
            {{ topic.speaker.job_title }}, {{ topic.speaker.company_name }}
          </div>
        </div>
      </div>
    </div>
    <div v-bind:id="tooltipContent">
      <h1>{{ topic.name }}</h1>
      <h4>{{ topic.start_time }} - {{ topic.end_time }}</h4>
      <h6 v-if="topic.speaker.name">{{ topic.speaker.name }}</h6>
      <p>{{ topic.description }}</p>
    </div>
  </div>
</template>

<script>
import Avatar from 'vue-avatar'
export default {
  components: {
    Avatar
  },
  props: {
    topic: [Object]
  },
  data () {
    return {
    }
  },
  computed: {
    tooltipContent() {
      return this.topic.id + '-description';
    }
  },
}

</script>


<style>
.topic {
  margin-top: 1.5vw;
  margin-bottom: 1.5vw;
}

.topic-name {
  font-family: "Circular-Pro-Book";
  color: #501cd7;
  font-size: 2vw;
}

.topic-time {
  font-family: "Circular-Pro-Book";
  font-size: 1vw;
}
.topic-speaker-name {
  font-size: 1.5vw;
}

.topic-speaker-job-desc {
  font-size: 1vw;
}

.topic-speaker-name,
.topic-speaker-job-desc {
  font-family: "Circular-Pro-Bold";
  color: #e96de3;
  font-weight: bold;
}
</style>
