export default class CardDetailPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `<div>CARD DETAIL PAGE</div>`;
    }
}

customElements.define('card-detail-page', CardDetailPage);