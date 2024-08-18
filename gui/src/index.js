import "./css/global.css";

import TopPage from "./pages/TopPage";
import CardEditPage from "./pages/CardEditPage";
import CardListPage from "./pages/CardListPage"
import CardDetailPage from "./pages/CardDetailPage";
import QuestionPage from "./pages/QuestionPage";
import NotFoundPage from "./pages/NotFoundPage"
import SpaAnchor from "./components/SpaAnchor";

document.body.innerHTML = `
    <header>
        <spa-anchor href="/">TOP</spa-anchor> |
        <spa-anchor href="/cards/add">ADD</spa-anchor> |
        <spa-anchor href="/cards/list">LIST</spa-anchor> |
        <spa-anchor href="/question">QUESTION</spa-anchor>
        <hr>
    </header>

    <div id="app"></div>
    
    <footer>
    </footer>
`

const updateView = () => {
    const pages = {
        "/": new TopPage(),
        "/cards/add": new CardEditPage(),
        "/cards/list": new CardListPage(),
        "/cards/update": new CardEditPage(),
        "/cards/detail": new CardDetailPage(),
        "/question": new QuestionPage(),
    };

    const page = pages[window.location.pathname] || new NotFoundPage();

    const app = document.getElementById("app");
    const previousPage = app.lastElementChild;

    previousPage ? app.replaceChild(page, previousPage) : app.appendChild(page);
};

// 初期表示時の処理
updateView();

// ブラウザバック時の処理
window.addEventListener("popstate", () => {
    updateView();
});

// View更新イベント発生時の処理
window.addEventListener("updateView", event => {
    const href = event.detail;
    window.history.pushState(null, "", href);
    updateView();
})