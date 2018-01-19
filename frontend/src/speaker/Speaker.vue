<template>
  <div class="col-sm-3 keynote-profile">
    <img class="other-image img-circle"
         v-bind:src="image"
         v-tooltip="{html: tooltipContent, offset: 30}"/>
    <div class="other-name">
      {{ name }}
    </div>
    <div class="other-company">
      <div v-if="showDetails">
        {{ job_title }}, {{ company_name }}
      </div>
    </div>
    <div v-bind:id="tooltipContent">
      <h1>{{ name }}</h1>
      <h4 v-if="showDetails">{{ job_title }}, {{ company_name }}</h4>
      <p id="description">{{ description }}</p>
    </div>
  </div>
</template>

<script>

export default {
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
#description {
  word-wrap: break-word;
}
</style>

