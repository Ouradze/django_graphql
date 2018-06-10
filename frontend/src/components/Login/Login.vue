<template>
  <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Login</v-toolbar-title>
                <v-spacer></v-spacer>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field prepend-icon="person" name="login" label="Login" type="text" v-model="username"></v-text-field>
                  <v-text-field id="password" prepend-icon="lock" name="password" label="Password" type="password" v-model="password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" @click="login()">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
  </v-container>
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
    drawer: null,
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
      }).catch((error) => {
        console.log(error);
        this.username = username;
        this.password = password;
      });
    },
  },
};
</script>

<style lang="stylus" scoped>
</style>
