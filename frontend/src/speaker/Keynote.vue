<template>
  <div class="col-sm-4 keynote-profile">
    <avatar :src="image"
            :username="name"
            :size="250"
            v-tooltip="{html: tooltipContent, offset: 30, delay: 0}">
    </avatar>
    <div class="keynote-name">
      {{ name }}
    </div>
    <div class="keynote-company">
      <div v-if="showDetails">
        {{ job_title }}, {{ company_name }}
      </div>
    </div>
    <div v-bind:id="tooltipContent">
      <h1>{{ name }}</h1>
      <h4 v-if="showDetails">{{ job_title }}, {{ company_name }}</h4>
      <p>{{ description }}</p>
    </div>
  </div>
</template>

<script>
import Avatar from 'vue-avatar'

export default {
  components: {
    Avatar
  },
  props: ['id', 'name', 'company_name', 'job_title', 'description', 'image'],
  computed: {
    showDetails () {
      return this.job_title && this.company_name ? true : false;
    },
    tooltipContent() {
      return this.id + '-description';
    }
  },
  data () {
    return {
    }
  }
}

</script>


<style>
</style>
