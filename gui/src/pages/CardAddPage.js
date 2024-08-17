export default class CardAddPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `<div>CARD ADD PAGE</div>`;
    }
}

customElements.define('card-add-page', CardAddPage);