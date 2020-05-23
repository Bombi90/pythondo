import Home from "../routes/Home.svelte";
import PostForm from "../routes/PostForm.svelte";
import Blank from "../routes/Blank.svelte";
import { builtInActions } from "../utils/Store";


export const routerModule = (store) => {
    store.on(builtInActions.INIT, (state, data) => {
      const urls = window.pythondo.urls;
      let routes = new Map();
      [{ link: "/", component: Home, isBlank: false, props: { label: "Home" } }, ...urls].forEach(
        ({ link, component, props, isBlank }) => {
          routes.set(link, { props, component: component ? component : isBlank ? Blank : PostForm });
        }
      );
      return {
        urls,
        routes,
      };
    });
};