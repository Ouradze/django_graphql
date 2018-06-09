<template>
  <div>
    <v-navigation-drawer
        clipped
        app
        v-model="drawer"
        disable-route-watcher
        left
        temporary
      >
        <v-list dense>
            <v-list-tile to="/">
              <v-list-tile-action>
                <v-icon>dashboard</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>TodoList</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile to="/">
              <v-list-tile-action>
                <v-icon>settings</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>Todo</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile to="/">
              <v-list-tile-action>
                <v-icon>bug_report</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>Users</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
        </v-list>
      </v-navigation-drawer>
    <v-toolbar  app fixed clipped-left>
      <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title class="menuTitle">
        <router-link :to="{name:'Home'}">
          <app-logo></app-logo>
          GraphQL Demo
        </router-link>
      </v-toolbar-title>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat to="/todolist">TodoList</v-btn>
        <v-btn flat to="/todo">Todo</v-btn>
        <v-btn flat to="/users">Users</v-btn>
      </v-toolbar-items>
      <v-spacer></v-spacer>
    </v-toolbar>
  </div>
</template>

<script>
import AppLogo from '../Logo/AppLogo.vue';

export default {
  name: 'd-header',
  components: {
    AppLogo,
  },
  data: () => ({
    drawer: false,
  }),
};
</script>

<style lang="stylus">
.menuTitle a
  color white
  text-decoration none
  vertical-align middle

.toolbar
    opacity: 0.8
</style>

