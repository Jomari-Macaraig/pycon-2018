<template>
  <div class="sponsor-container">
    <div class="row">
      <div class="col-sm-3 text-center">
        <avatar :src="sponsor.image"
                :username="sponsor.name"
                background-color="#e96de3"
                :size="250">
        </avatar>
      </div>
      <div class="col-sm-9">
        <div class="sponsor-name">
          <a v-bind:href="sponsor.link">{{ sponsor.name }}</a>
        </div>
        <div class="sponsor-description">
          {{ sponsor.description }}
        </div>
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
    sponsor: [Object]
  },
  data () {
    return {
    }
  }
}
</script>

<style>
.sponsor-container {
  margin-top: 2vw;
}
.sponsors-section > .content {
  margin-left: 7vw;
  margin-right: 7vw;
}
.sponsor-name {
  margin-bottom: 1vw;
}
.sponsor-name > a {
  text-decoration: none;
  font-family: "Circular-Pro-Bold";
  color: #501cd7;
  font-size: 3vw;
}
.sponsor-description {
  font-family: "Circular-Pro-Book";
  color: #501cd7;
  font-size: 1.2vw;
  min-height: 5vw;
}
</style>
