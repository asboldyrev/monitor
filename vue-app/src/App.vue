<template>
    <div class="container my-2">
        <div class="columns">
            <div class="column col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-4 col-3 my-2"><app-system></app-system></div>
            <div class="column col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-4 col-3 my-2"><app-processor></app-processor></div>
            <div class="column col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-4 col-3 my-2"><app-average></app-average></div>
            <div class="column col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-4 col-3 my-2"><app-memory></app-memory></div>
            <div class="column col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-8 col-6 my-2"><app-filesystem></app-filesystem></div>
            <div class="column col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-8 col-6 my-2"><app-docker></app-docker></div>
        </div>
    </div>
</template>

<script>
import AppSystem from './components/AppSystem.vue'
import AppProcessor from './components/AppProcessor.vue'
import AppMemory from './components/AppMemory.vue'
import AppAverage from './components/AppAverage.vue'
import AppFilesystem from './components/AppFilesystem.vue'
import AppDocker from './components/AppDocker.vue'

export default {
  name: 'App',
  components: {
        appSystem: AppSystem,
        appProcessor: AppProcessor,
        appAverage: AppMemory,
        appMemory: AppAverage,
        appFilesystem: AppFilesystem,
        appDocker: AppDocker,
  }
}
</script>

<style lang="scss">
    @import "../node_modules/spectre.css/src/spectre";
</style>
