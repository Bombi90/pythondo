import App from "./components/App.svelte";
import store from './state'

const app = new App({
  target: document.body,
});

export default app;
