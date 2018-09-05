<template>
  <div class="page-content">
    <div class="mdl-grid">
      <div class="mdl-cell mdl-cell--4-offset mdl-cell--4-col">
        <h1>GraphQL Demo</h1>
        <h4>The application which helps you play with GraphQL.</h4>
        <h4>Enjoy :)</h4>
      </div>
    </div>
    <div class="mdl-grid">
      <div class="mdl-cell mdl-cell--4-offset mdl-cell--4-col">
        <div class="description">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
          quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
          Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
          fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.</p>
          <br />
          <p>Hello PyconFr</p>
        </div>
        <div class="bottomText">
          <a
            href="//www.artstation.com/artist/mikeazevedo"
            target="_blank"
            rel="noopener noreferrer"
            >
            Mike Azevedo
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home',
};
</script>

<style>
  .my-layout {
    background: url("../../assets/home-background2.jpg") center / cover;
  }
  .mdl-layout__header .mdl-layout__drawer-button {
    color: white;
  }
</style>
