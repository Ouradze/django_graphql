<template>
  <div class="page-content">
    <template v-if="$apollo.loading">
      <div class="mdl-spinner mdl-spinner--single-color mdl-js-spinner is-active"></div>
    </template>
    <template v-else>
      <div class="mdl-grid" v-for="list in $apolloData.queries.todoLists" :key="list.id">
        <div class="mdl-cell mdl-cell--4-offset mdl-cell--4-col">
          <div class="demo-card-wide mdl-card mdl-shadow--2dp">
            <div class="mdl-card__title">
              <h2 class="mdl-card__title-text">{{ list.title }}</h2>
            </div>
            <div class="mdl-card__supporting-text">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit.
              Mauris sagittis pellentesque lacus eleifend lacinia...
            </div>
            <div class="mdl-card__actions mdl-card--border">
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>

</template>

<script>
import gql from 'graphql-tag';

const allTodoLists = gql`
  query{
    allTodoLists {
      id
      title
      creator {
        id
        username
      }
      createdAt
    }
  }
`;

export default {
  name: 'todo-list',
  apollo: {
    todoLists: {
      query: allTodoLists,
    },
  },
  data() {
    return {
      todoLists: '',
    };
  },
};
</script>

<style scoped>
</style>
