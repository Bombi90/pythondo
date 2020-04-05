
import regexparam from 'regexparam';

export function getRouteItem(path, route) {
    const { pattern } = regexparam(path)
    const component = route.component
    const props = route.props || {}
    return function matcher(toPath) {
        const matches = pattern.exec(toPath)
        if (matches === null) {
            return null
        }
        return {
            component,
            props
        }
    }
}