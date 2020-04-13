<script context="module">
import {readable} from 'svelte/store'

export function link(node) {
    const href = node.getAttribute('href')
    node.setAttribute('href', '#' + href)
}

function getLocation() {
    const hashPosition = window.location.href.indexOf('#/')
    let location = (hashPosition > -1) ? window.location.href.substr(hashPosition + 1) : '/'
    return location
}

export const location = readable(
    getLocation(),
    set => {
        const update = () => {
            set(
                getLocation()
            )
        }
        window.addEventListener('hashchange', update, false)
        return () => {
            window.removeEventListener('hashchange', update, false)
        }
    }
)

</script>

 <svelte:component this="{ component }" props="{componentProps}" on:routeEvent />

 <script>
 import { getRouteItem } from '../utils/getRouteItem'
 import {createEventDispatcher} from 'svelte'

const dispatch = createEventDispatcher()
export let routes = {}
const routesList = []
let component = null
let componentProps = null

routes.forEach((route, path) => {
    routesList.push(
        getRouteItem(
            path, route
        )
    )
})
$: {
    component = null
    let i = 0
    while (!component && i < routesList.length) {
        const matcher = routesList[i]($location)
        if (matcher) {
            const detail = {
                component: matcher.component,
                name: matcher.component.name,
                props: {
                    methods: ["GET"],
                    location: $location,
                    ...matcher.props
                }
            }
            component = matcher.component
            componentProps = detail.props

            setTimeout(() => dispatch('routeLoaded', detail), 0)
        }
        i++
    }
}
 </script>