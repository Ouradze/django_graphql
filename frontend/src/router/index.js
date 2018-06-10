import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home/Home.vue';
import Login from '../components/Login/Login.vue';
import Todo from '../components/Todo/Todo.vue';
import TodoList from '../components/TodoList/TodoList.vue';
import Users from '../components/Users/Users.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/todo',
      name: 'Todo',
      component: Todo,
    },
    {
      path: '/todolist',
      name: 'TodoList',
      component: TodoList,
    },
    {
      path: '/users',
      name: 'Users',
      component: Users,
    },
  ],
  mode: 'history',
});

