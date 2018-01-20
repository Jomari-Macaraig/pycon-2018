<template>
  <div class="partner-container">
    <div class="row">
      <div class="col-sm-9 text-justify">
        <div class="partner-name text-right">
          <a v-bind:href="partner.link">{{ partner.name }}</a>
        </div>
        <div class="partner-description">
          {{ partner.description }}
        </div>
      </div>
      <div class="col-sm-3 text-center">
        <avatar :src="partner.image"
                :username="partner.name"
                background-color="#e96de3"
                :size="250">
        </avatar>
      </div>
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
    partner: [Object]
  },
  data () {
    return {
    }
  }
}
</script>

<style>
.partner-container {
  margin-top: 2vw;
}

.partners-section > .content {
  margin-left: 7vw;
  margin-right: 7vw;
}

.partner-name {
  margin-bottom: 1vw;
}

.partner-name > a {
  text-decoration: none;
  font-family: "Circular-Pro-Bold";
  color: #501cd7;
  font-size: 3vw;
}

.partner-description {
  font-family: "Circular-Pro-Book";
  color: #501cd7;
  font-size: 1.2vw;
  min-height: 5vw;
}
</style>

