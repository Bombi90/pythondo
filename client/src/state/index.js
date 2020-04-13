import { createStore } from "../utils/Store";
import { routerModule } from './routerModule';
import { fetchModule } from "./fetchModule";

export default createStore([routerModule, fetchModule]);

