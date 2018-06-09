<template>
  <v-app id="inspire" dark>
    <Header></Header>
    <v-content :class="home ? 'HomeBackground': ''">
      <v-container fluid>
        <router-view/>
      </v-container>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import Footer from '../Footer/Footer.vue';
import Header from '../Header/Header.vue';

export default {
  name: 'App',
  components: {
    Footer,
    Header,
  },
  computed: {
    home() {
      return this.$route.path === '/';
    },
  },
};
</script>

<style lang="stylus">
@import '../../../node_modules/vuetify/src/stylus/main.styl';

body
  background-color: primary
  color: white

a
  color: white
</style>
