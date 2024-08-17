export default class TopPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `<div>TOP PAGE</div>`;
    }
}

customElements.define('top-page', TopPage);