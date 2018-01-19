<template>
  <div class="col-sm-4 keynote-profile">
    <img class="keynote-image img-circle"
         v-bind:src="image"
         v-tooltip="{html: tooltipContent, offset: 30}"/>
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
      <p>{{ description }}</p>
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
</style>
