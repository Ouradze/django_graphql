<template>
  <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header my-layout">
  <!-- Always shows a header, even in smaller screens. -->
    <header class="mdl-layout__header mdl-layout__header--transparent">
      <div class="mdl-layout__header-row">
        <!-- Title -->
        <span class="mdl-layout-title"><a href="/">GraphQL Demo</a></span>
        <!-- Add spacer, to align navigation to the right -->
        <div class="mdl-layout-spacer"></div>
        <!-- Navigation. We hide it in small screens. -->
        <nav class="mdl-navigation mdl-layout--large-screen-only">
          <a class="mdl-navigation__link" href="/todolist">Todo Lists</a>
          <a class="mdl-navigation__link" href="/todo">Todos</a>
          <a class="mdl-navigation__link" href="/users">Users</a>
          <a class="mdl-navigation__link" href="#" v-if="username">{{ username }}</a>
          <!-- Left aligned menu below button -->
          <button id="demo-menu-lower-right"
                  class="mdl-button mdl-js-button mdl-button--icon">
            <i class="material-icons">more_vert</i>
          </button>
          <ul class="mdl-menu mdl-menu--bottom-right mdl-js-menu mdl-js-ripple-effect"
              for="demo-menu-lower-right">
            <template v-if="username">
              <li class="mdl-menu__item">{{ username }}</li>
              <li class="mdl-menu__item"><a @click="logout()">Logout</a></li>
            </template>
            <template v-else>
              <li class="mdl-menu__item"><a href="/login">Login</a></li>
            </template>
            <li class="mdl-menu__item mdl-menu__item--full-bleed-divider">Another Action</li>
            <li disabled class="mdl-menu__item">Disabled Action</li>
            <li class="mdl-menu__item">Yet Another Action</li>
          </ul>
        </nav>
      </div>
    </header>
    <div class="mdl-layout__drawer">
      <span class="mdl-layout-title">GraphQL Demo</span>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="/todolist">Todo Lists</a>
        <a class="mdl-navigation__link" href="/todo">Todos</a>
        <a class="mdl-navigation__link" href="/users">Users</a>
      </nav>
    </div>
    <main class="mdl-layout__content">
      <router-view/>
    </main>
    <footer class="mdl-mini-footer">
      <div class="mdl-mini-footer__left-section">
        <div class="mdl-logo">GraphQL Demo</div>
        <ul class="mdl-mini-footer__link-list">
          <li><a href="#">Help</a></li>
          <li><a href="#">Privacy & Terms</a></li>
        </ul>
      </div>
    </footer>
  </div>
</template>

<script>
import { onLogout } from '../../vue-apollo';

export default {
  name: 'App',
  data: () => ({
    username: '',
  }),
  // no invalidation from server side at the moment
  methods: {
    logout() {
      onLogout(this.$apolloProvider.defaultClient);
      this.username = '';
    },
  },
  mounted() {
    if (localStorage.username) {
      this.username = localStorage.username;
    }
  },
  computed: {
    home() {
      return this.$route.path === '/';
    },
  },
};
</script>

<style>

body{
  background-color: primary;
  color: black;
}

a {
  color: black;
}
</style>
