import { writable, derived, get } from 'svelte/store';

let stores = {};

class Store {
    constructor(modules = []) {
        this.events = {}
        this.state = writable({})
        this.modules = modules
        this.dispatch = this.dispatch.bind(this)
        modules.forEach(m => m(this));
    }
    dispatch(event, payload) {
        console.log("DISPATCHING >> ", {event, payload})
        const storeHandlers = this.events[event];
        if (storeHandlers) {
            let changes = { }
            let changed
            let state = get( this.state );
            storeHandlers.forEach(i => {
              let diff = i(state, payload)
              if (diff && typeof diff.then !== 'function') {
                changed = state = { ...state, ...diff }
                changes = { ...changes, ...diff }
              }
            })
            if (changed) {
                this.state.set(changed)
                // this.changed(changes)
            }
          }
    }
    getStore() {
        return this.state;
    }
    init() {
        this.dispatch(builtInActions.INIT)
    }
    changed(payload) {
        this.dispatch(builtInActions.CHANGED, payload)
    }
    on(event, handler) {
       let storeHandlers = this.events[event];
        if ( !storeHandlers ) {
            storeHandlers = this.events[event] = []
        }
        storeHandlers.push(handler)
        return () => {
          storeHandlers = storeHandlers.filter(i => i !== cb)
        }
    }
}

export const builtInActions = {
    INIT: Symbol.for("INIT"),
    DISPATCH: Symbol.for("DISPATCH"),
    CHANGED: Symbol.for("CHANGED"),
};
export const builtInTypes = {
    DEFAULT: Symbol.for("DEFAULT"),
    PLACEHOLDER: Symbol.for("PLACEHOLDER")
}

export const createStore = (args) => {
    if ( Array.isArray(args) ) {
        const store = new Store(args);
        stores[builtInTypes.DEFAULT] = store;
        store.init()
        return store
    } else if ( 'modules' in args ) {
        const modules = args.modules
        const key = args.key || builtInTypes.DEFAULT
        const store = new Store(modules);
        stores[key] = store;
        store.init()
        return store
    }
}
const noop = () => {};

export const selectStore = (first, ...k) => {
    let store;
    let accessors;
    let handler = undefined
    if ( 'storeKey' in first ) {
        handler = first.handler || noop;
        store = stores[first.storeKey]
        accessors = k
    } else if (typeof first === 'function') {
        accessors = k
        handler = first
        store = stores[builtInTypes.DEFAULT]
    } else {
        accessors = [storeKey, ... k]
        store = stores[builtInTypes.DEFAULT]
    }
    derived(store.getStore(), $store => 
        accessors.reduce((acc, val) => {
            acc[val] = $store[val]
            return acc;
        }, {}), {})
    .subscribe(handler)

    if (store) {
        return store.dispatch
    }
}