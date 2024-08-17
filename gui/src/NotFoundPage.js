export default class NotFoundPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `<div>404: NOT FOUND</div>`;
    }
}

customElements.define('not-found-page', NotFoundPage);