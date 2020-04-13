import Home from "../routes/Home.svelte";
import PostForm from "../routes/PostForm.svelte";
import { builtInActions } from "../utils/Store";


export const routerModule = (store) => {
    store.on(builtInActions.INIT, (state, data) => {
      const urls = window.pythondo.urls;
      let routes = new Map();
      [{ link: "/", component: Home, props: { label: "Home" } }, ...urls].forEach(
        ({ link, component, props }) => {
          routes.set(link, { props, component: component || PostForm });
        }
      );
      return {
        urls,
        routes,
      };
    });
};