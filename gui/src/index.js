import TopPage from "./pages/TopPage";
import CardAddPage from "./pages/CardAddPage";
import CardListPage from "./pages/CardListPage"
import CardUpdatePage from "./pages/CardUpdatePage";
import CardDetailPage from "./pages/CardDetailPage";
import QuestionPage from "./pages/QuestionPage";
import NotFoundPage from "./pages/NotFoundPage"
import SpaAnchor from "./components/SpaAnchor";

document.body.innerHTML = `
    <spa-anchor href="/">TOP</spa-anchor> |
    <spa-anchor href="/cards/add">CARD_ADD</spa-anchor> |
    <spa-anchor href="/cards/list">CARD_LIST</spa-anchor> |
    <spa-anchor href="/cards/update">CARD_UPDATE</spa-anchor> |
    <spa-anchor href="/cards/detail">CARD_DETAIL</spa-anchor> |
    <spa-anchor href="/question">QUESTION</spa-anchor>
    <div id="app"></div>
`

const updateView = () => {
    const pages = {
        "/": new TopPage(),
        "/cards/add": new CardAddPage(),
        "/cards/list": new CardListPage(),
        "/cards/update": new CardUpdatePage(),
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