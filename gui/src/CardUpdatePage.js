export default class CardUpdatePage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `<div>CARD UPDATE PAGE</div>`;
    }
}

customElements.define('card-update-page', CardUpdatePage);