<script>
  import Loader from "../components/Loader.svelte";
  import Editor from "../components/JSONEditor.svelte";
  import { selectStore } from "../utils/Store";
  let isFetching = false
  const dispatch = selectStore(
    ({ fetching: fetchingFromState }) => (isFetching = fetchingFromState),
    "fetching"
  );
  export let props;
  let prevLocation;
  let url = `${window.location.origin}${props.location}`;
  let selectedMethod;
  let params = "";
  let response;

  let jsonBody = {};

  function handleSubmit() {
    console.log("DISPATCHING")
    dispatch("update_fetching", true)

    fetch(`${props.location}${selectedMethod === "GET" ? params : ""}`, {
      method: selectedMethod,
      ...(selectedMethod !== "GET" && { body: JSON.stringify(jsonBody) }),
      headers: { "Content-Type": "application/json" }
    })
      .then(res => res.json())
      .then(res => {
        console.log("GOT RESPONSE >> ", {res})
        try {
          response = JSON.stringify(res);
        } catch (e) {
          response = e;
        }
      })
      .catch(err => {
        response = err.toString();
      })
      .finally(() => {
        dispatch("update_fetching", false)
      });
  }
  $: url = `${window.location.origin}${props.location}`
  $: {
    if (props.location != prevLocation) {
      prevLocation = props.location;
      params = "";
      response = undefined;
      dispatch("update_fetching", false)
    }
  }
</script>

<style>
  .pythondo-form-container {
    height: calc(100vh - 100px);
    padding: 0 15px;
  }

  .route-title {
    text-align: center;
    font-size: 2em;
    color: #222;
    margin-bottom: 0.2em;
    font-weight: lighter;
  }
  .pure-form {
    display: flex;
    justify-content: center;
  }
  fieldset {
    width: 400px;
  }
  .pure-form label {
    text-align: center;
  }
  textarea {
    height: 100px;
  }
  .invalid-json {
    border-color: var(--secondary-text);
  }
  .editor-container {
    background: var(--white);
  }
  .pure-button {
    color: var(--white);
    background-color: var(--terziary-text);
  }
  .pure-controls {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }
  .response-container {
    height: 200px;
    width: 400px;
    margin: auto;
  }
  .response-container textarea {
    height: 200px;
    width: 400px;
    background: #eaeaea;
  }
  .response-container textarea:focus {
    outline: none;
  }
</style>

<svelte:head>
  <title>Pythondo: {props.label}</title>
</svelte:head>
<div class="pure-u-1 pythondo-form-container">
  <h2 class="route-title">Welcome in •{props.label}•</h2>
  <p class="pythondo-form-description">{props.description}</p>
  <form
    class="pure-form pure-form-stacked"
    on:submit|preventDefault={handleSubmit}>
    <fieldset>
      <div class="pure-control-group">
        <label>Url</label>
        <input class="pure-input-1" readonly type="text" bind:value={url} />
      </div>
      <div class="pure-control-group">
        <label for="state">Method</label>
        <select class="pure-input-1" bind:value={selectedMethod}>
          {#each props.methods as method}
            <option value={method}>{method}</option>
          {/each}
        </select>
      </div>
      {#if ['POST', 'PUT', 'PATCH'].includes(selectedMethod)}
        <div class="pure-control-group editor-container">
          <Editor on:json-changed={ ({detail}) => jsonBody = detail } />
        </div>
      {/if}
      {#if ['GET'].includes(selectedMethod)}
        <div class="pure-control-group">
          <label for="params">URL Params</label>
          <input
            id="params"
            type="text"
            bind:value={params}
            class="pure-input-1"
            placeholder="?key=KEY" />
        </div>
      {/if}

      <div class="pure-controls">
        <button type="submit" class="pure-button">Submit</button>
      </div>
    </fieldset>
  </form>
  <div class="response-container">
      <Editor readOnlyValue={response} readOnly="true" />
  </div>
</div>
{#if isFetching}
  <Loader />
{/if}
