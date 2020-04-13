import { builtInActions } from "../utils/Store";


export const fetchModule = (store) => {
    store.on(builtInActions.INIT, (state, data) => {
      return {
        fetching: false
      };
    });
    store.on("update_fetching", (_, data) => {
      return {
        fetching: data
      };
    });
};