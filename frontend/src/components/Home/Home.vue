<template>
  <v-container fluid >
    <v-layout column align-center justify-center>
      <h1>GraphQL Demo</h1>
      <h4>The application which helps you play with GraphQL.</h4>
      <h4>Enjoy :)</h4>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs6 offset-xs3 class="HeadContainer">
        <div class="headline">
            Lorem
        </div>
        <div class="description">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
          quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
          fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.</p>
          <br />
          <p>Hello DjangoCong</p>
        </div>
        <v-btn class="primary" to="/login">Login</v-btn>
        <div class="bottomText">
          <a
            href="//www.artstation.com/artist/mikeazevedo"
            target="_blank"
            rel="noopener noreferrer"
            >
            Mike Azevedo
          </a>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'home',
};
</script>

<style lang="stylus">
  .HomeBackground {
    background-image: url("../../assets/home-background2.jpg");
    background-position: center top 25%;
    background-repeat: no-repeat;
  }
</style>
