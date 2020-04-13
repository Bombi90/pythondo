<script>
  import Link from "./Link.svelte";
  import Router from "../utils/Router.svelte";
  import { selectStore } from "../utils/Store";
  let routes;
  const dispatch = selectStore(
    ({ routes: routesFromState }) => (routes = routesFromState),
    "routes"
  );
  function routeLoaded(event) {}
</script>

<style>
  .pure-menu {
    height: 50px;
  }
  .pure-menu-heading {
    color: var(--terziary-text);
  }
  :global(.pure-menu-link:hover),
  :global(.pure-menu-link:focus) {
    background-color: var(--secondary-bg-color);
  }
</style>

<div class="pure-menu pure-menu-horizontal pure-menu-scrollable pure-u-1">
  <a href="javascript:void(0)" class="pure-menu-link pure-menu-heading">
    Pythondo
  </a>
  <ul class="pure-menu-list">
    {#each window.pythondo.urls as loc}
      <li class="pure-menu-item">
        <Link to={loc.link}>{loc.props.label}</Link>
      </li>
    {/each}
  </ul>
</div>

<Router {routes} on:routeLoaded={routeLoaded} />
