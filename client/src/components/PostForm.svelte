<script>
  import Loader from "./Loader.svelte";
  export let props;
  let prevLocation;
  let url = `${window.location.origin}${props.location}`;
  let selectedMethod;
  let params = "";
  let jsonBody = "";
  let jsonBodyParsed = {};
  let invalidJSON = false;
  let response;
  let isFetching = false;
  function onParamsInput({ target: { value } }) {
    params = value;
  }
  function onJSONInput({ target: { value } }) {
    try {
      jsonBodyParsed = JSON.parse(value);
      jsonBody = value;
      invalidJSON = false;
    } catch (e) {
      invalidJSON = true;
    }
  }
  function handleSubmit() {
    isFetching = true;
    fetch(`${props.location}${selectedMethod === "GET" ? params : ""}`, {
      method: selectedMethod,
      ...(selectedMethod !== "GET" &&
        !invalidJSON && { body: JSON.stringify(jsonBodyParsed) }),
      headers: { "Content-Type": "application/json" }
    })
      .then(res => res.json())
      .then(res => {
        try {
          response = JSON.stringify(res);
        } catch (e) {
          response = "Invalid response from Server";
        }
      })
      .catch(err => {
        response = err.toString();
      })
      .finally(() => {
        isFetching = false;
      });
  }
  $: {
    if (props.location != prevLocation) {
      prevLocation = props.location;
      params = "";
      jsonBody = "";
      jsonBodyParsed = {};
      invalidJSON = false;
      response = undefined;
      isFetching = false;
    }
  }
  $: {
    if (selectedMethod === "GET") {
      jsonBody = "";
      jsonBodyParsed = {};
    } else {
      params = "";
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
    height: 320px;
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
    display: flex;
    justify-content: center;
    height: 200px;
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
        <input class="pure-input-1" readonly type="text" value={url} />
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
        <div class="pure-control-group">
          <label for="json-body">JSON Body</label>
          <textarea
            id="json-body"
            class="pure-input-1 {invalidJSON ? 'invalid-json' : ''}"
            value={jsonBody}
            on:input={onJSONInput}
            placeholder="Request Body goes here" />
        </div>
      {/if}
      {#if ['GET'].includes(selectedMethod)}
        <div class="pure-control-group">
          <label for="params">URL Params</label>
          <input
            id="params"
            type="text"
            value={params}
            on:input={onParamsInput}
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
    <textarea
      tabindex="-1"
      id="response"
      value={response || ''}
      class="pure-input-1"
      readonly
      placeholder="Response Body goes here" />
  </div>
</div>
{#if isFetching}
  <Loader />
{/if}
