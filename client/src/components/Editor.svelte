<script>
  import Quill from "quill";
  import Delta from "quill-delta";
  import { selectStore } from "../utils/Store";
  import { onMount, createEventDispatcher } from "svelte";
  let isFetching = false
  let deleted = false
  selectStore(
    ({ fetching: fetchingFromState }) => (isFetching = fetchingFromState),
    "fetching"
  );
  export let value = false;
  export let format = false;
  const dispatch = createEventDispatcher();
  export let options = {
    toolbar: [
      [{ header: [1, 2, false] }],
      ["bold", "italic", "underline"],
      ["code-block"]
    ]
  };
  let editor;
  onMount(() => {
    editor = new Quill("#editor", {
      ...options,
      theme: "snow"
    });
    if (format) {
      editor.format(format, true);
    }
    editor.on("editor-change", function(eventName, ...args) {
      if (eventName === "text-change") {
        dispatch("change", editor.getText().replace(/(\r\n|\n|\r)/gm, ""));
      }
    });
  });
  $: {
    if (editor && value) {
      console.log("UPDATING", {value})
      editor.updateContents(new Delta().insert(value));
    }
  }
  $: {
    if(isFetching && editor && !deleted) {
          console.log("DELETING", {
      isFetching,
      deleted
    })
      deleted = isFetching
      editor.setContents([])
      editor.format(format, true);
    }
    if(!isFetching) {
      deleted = isFetching
    }
  }
</script>

<style>
  #editor {
    height: 150px;
  }
</style>

<div id="editor" />
