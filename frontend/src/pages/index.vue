<!-- src/pages/index.vue -->
<template>
  <div class="container">
    <h1>Welcome to EduSync AI</h1>
    <Button />
  </div>
</template>

<script>
import Button from '@/components/Button.vue';

export default {
  components: {
    Button
  }
};
</script>

<style scoped>
h1 {
  font-size: 2em;
  color: #333;
}
</style>