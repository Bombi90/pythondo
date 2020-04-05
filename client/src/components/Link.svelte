<script>
export let to
import { link } from '../utils/Router.svelte'
</script>

<a class="pure-menu-link" href={to} use:link><slot /></a>

<style>
.pure-menu-link {
    color: var(--secondary-text)
}
</style>