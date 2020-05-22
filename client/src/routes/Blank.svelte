<script>
  import { onMount } from "svelte";
  export let props;
  onMount(async () => {
    const data = await fetch(props.location);
    const { html } = await data.json();
    const targetNode = document.getElementById("pythondo-app-container");
    const config = { attributes: true, childList: true, subtree: true };
    const callback = function(mutationsList, observer) {
      // Use traditional 'for loops' for IE 11
      for (let mutation of mutationsList) {
        if (mutation.type === "childList") {
                   const script = targetNode.querySelector("script");
          eval(script.innerText);
        } else if (mutation.type === "attributes") {
          const script = targetNode.querySelector("script");
          eval(script.innerText);
        }
      }
    };
    // Create an observer instance linked to the callback function
    const observer = new MutationObserver(callback);

    // Start observing the target node for configured mutations
    observer.observe(targetNode, config);
    targetNode.innerHTML = html;
  });
</script>

<style>
  .pythondo-blank {
    height: calc(100vh - 100px);
    padding: 0 15px;
  }
  .blank-title {
    text-align: center;
    font-size: 2em;
    color: #222;
    margin-bottom: 0.2em;
    font-weight: lighter;
  }
</style>

<div class="pure-u-1 pythondo-blank">
  <h2 class="blank-title">Welcome in •{props.label}•</h2>
  <p class="pythondo-form-description">{props.description}</p>
  <div id="pythondo-app-container" />
</div>
