<template>
  <div class="page-content">
    <div class="mdl-grid">
      <div class="mdl-cell mdl-cell--4-offset mdl-cell--4-col">
        <div class="demo-card-wide mdl-card mdl-shadow--2dp">
          <div class="mdl-card__title">
            <h2 class="mdl-card__title-text">Login</h2>
          </div>
          <div class="mdl-card__supporting-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Mauris sagittis pellentesque lacus eleifend lacinia...
          </div>
          <div class="mdl-card__actions mdl-card--border">
            <form action="#">
              <div class="mdl-textfield mdl-js-textfield">
                <input class="mdl-textfield__input" type="text" id="login" v-model="username">
                <label class="mdl-textfield__label" for="sample1">Login...</label>
              </div>
              <div class="mdl-textfield mdl-js-textfield">
                <input class="mdl-textfield__input" type="password" id="pswd" v-model="password">
                <label class="mdl-textfield__label" for="sample1">Password...</label>
              </div>
            </form>
            <a
              class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect"
              @click="login()">
                Login
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag';
import { onLogin } from '../../vue-apollo';

const loginMutation = gql`
mutation($username:String!, $password:String!){
  tokenAuth(username:$username, password:$password){
    token
  }
}
`;

export default {
  name: 'login',
  data: () => ({
    username: '',
    password: '',
  }),
  methods: {
    login() {
      const { username } = this;
      const { password } = this;
      this.username = '';
      this.password = '';

      this.$apollo.mutate({
        mutation: loginMutation,
        variables: {
          username,
          password,
        },
      }).then((result) => {
        onLogin(this.$apolloProvider.defaultClient, result.data.tokenAuth.token);
        localStorage.setItem('username', username);
        this.$router.push(this.$route.query.redirect || '/');
      }).catch((error) => {
        console.log(error);
      });
    },
  },
};
</script>

<style scoped>
</style>
