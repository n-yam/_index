export default class QuestionPage extends HTMLElement {

    constructor() {
        super()
        this.innerHTML = `<div>QUESTION PAGE</div>`;
    }
}

customElements.define('question-page', QuestionPage);