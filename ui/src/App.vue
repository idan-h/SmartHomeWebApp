<script setup lang="ts">
</script>

<template>
  <router-view></router-view>
</template>

<style>
@import "vue-select/dist/vue-select.css";

:root {
  /* VueSelect Variables */

  --vs-controls-color: #646cff;
  /* Aligned to the link color in your style for consistency */
  --vs-border-color: #646cff;
  /* Same reason as above */

  --vs-dropdown-bg: #242424;
  /* Dark background in your default style */
  --vs-dropdown-color: rgba(255, 255, 255, 0.87);
  /* Default text color in your style */
  --vs-dropdown-option-color: rgba(255, 255, 255, 0.87);
  /* Default text color */

  --vs-selected-bg: #646cff;
  /* Link hover color for selected state */
  --vs-selected-color: #ffffff;
  /* White is generally a good contrasting color for a dark background */

  --vs-search-input-color: rgba(255, 255, 255, 0.87);
  /* Default text color */

  --vs-dropdown-option--active-bg: #535bf2;
  /* Link hover color for active/hover state in dropdown */
  --vs-dropdown-option--active-color: #ffffff;
  /* White for contrast against the active color */
}

@media (prefers-color-scheme: light) {
  :root {
    --vs-dropdown-bg: #ffffff;
    /* Light background color in light mode */
    --vs-dropdown-color: #213547;
    /* Default dark text color in light mode */
    --vs-dropdown-option-color: #213547;
    /* Same reason as above */
  }
}
</style>
