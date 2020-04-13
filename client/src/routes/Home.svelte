<script>
  export let props;
</script>

<style>
  .pythondo-home {
    height: calc(100vh - 100px);
    padding: 0 15px;
  }
  .home-title {
    text-align: center;
    font-size: 2em;
    color: #222;
    margin-bottom: 0.2em;
    font-weight: lighter;
  }
</style>


<div class="pure-u-1 pythondo-home">
  <h2 class="home-title">Welcome in •{props.label}•</h2>
</div>
