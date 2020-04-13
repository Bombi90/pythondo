<script>
  import Editor from "./Editor.svelte";
  import { createEventDispatcher } from "svelte";
  export let readOnly = false;
  export let readOnlyValue = false;
  let prevReadonly = null

  let options = {
    modules: {
      formula: false,
      toolbar: [["code-block"]],
      syntax: true
    },
    placeholder: "Please enter your JSON snippet...",
    readOnly
  };
  $:{
    if ( prevReadonly !== readOnlyValue ) {
      prevReadonly = readOnlyValue

    }
  }
  const dispatch = createEventDispatcher();
  let invalidJSON = false;
  let value;
  $: {
    if (!readOnly) {
      try {
        dispatch("json-changed", JSON.parse(value.detail));
        invalidJSON = false;
      } catch (e) {
        invalidJSON = true;
      }
    }
  }
</script>

<Editor {options} value={readOnlyValue} format="code-block" on:change={v => (value = v)} />