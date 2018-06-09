<template>
  <v-footer app>
    <v-container grid-list-md text-xs class="footer" fluid>
      <v-layout row wrap>
        <v-flex xs6>
          <div class="links">
            <div class="logoNsocial">
              <router-link :to="{name:'Home'}">
                <AppLogo></AppLogo>
              </router-link>
            </div>
            <br />
            <div class="aboutSite">
              <p>
                MOBA data plateform for dota2
                -
                Application powered by
                <a href="http://steampowered.com" target="_blank" rel="noopener noreferrer">
                </a>
              </p>
            </div>
            <hr />
          </div>
        </v-flex>
        <v-flex xs6 class="copyright">
          <p>Raddadi Mehdi DjangoCong 2018</p>
          <p>Dota 2 is a registered trademark of Valve Corporation.</p>
          <p><a href="mailto:me.raddadi@gmail.com">Contact Me</a></p>
        </v-flex>
      </v-layout>
    </v-container>
  </v-footer>
</template>

<script>
import AppLogo from '../Logo/AppLogo.vue';

export default {
  name: 'd-footer',
  components: {
    AppLogo,
  },
};
</script>

<style>
.copyright {
  text-align: right;
}
</style>
