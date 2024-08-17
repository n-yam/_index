export default class CardListPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `<div>CARD LIST PAGE</div>`;
    }
}

customElements.define('card-list-page', CardListPage);