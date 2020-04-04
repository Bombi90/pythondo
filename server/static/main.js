const getHelloWithKey = (key) => fetch(`/hello?key=${key}`).then(res => res.text())
const postHelloWithJSON = (json) => fetch(`/hello`, {method: "POST", headers:{"Content-type": "application/json"}, body: JSON.stringify({data: json})}).then(res => res.json())

window.onload = document.onload = function() {
    const promiseA = () => getHelloWithKey("CANE").then(response => {
        const div = document.createElement("div")
        div.innerHTML = response
        document.body.appendChild(div)
    });
    const promiseB = () => postHelloWithJSON({foo: "bar"}).then(response => {
        const div = document.createElement("div")
        div.innerHTML = JSON.stringify(response)
        document.body.appendChild(div)
    })
    Promise.all([promiseA(), promiseB()]).then(() => {
        console.log("DONE")
    })
}