import TopPage from "./pages/TopPage";
import CardAddPage from "./pages/CardAddPage";
import CardListPage from "./pages/CardListPage"
import CardUpdatePage from "./pages/CardUpdatePage";
import CardDetailPage from "./pages/CardDetailPage";
import QuestionPage from "./pages/QuestionPage";
import NotFoundPage from "./pages/NotFoundPage"

document.body.innerHTML = `
    <a href="/">TOP</a>
    <a href="/cards/add">CARD_ADD</a>
    <a href="/cards/list">CARD_LIST</a>
    <a href="/cards/update">CARD_UPDATE</a> 
    <a href="/cards/detail">CARD_DETAIL</a>
    <a href="/question">QUESTION</a>
    <div id="app"></div>
`

document.querySelectorAll("a").forEach(a => {
    a.onclick = event => {
        event.preventDefault();
        window.history.pushState(null, "", a.href);
    };
});

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

document.querySelectorAll("a").forEach(a => {
    a.onclick = event => {
        event.preventDefault();
        window.history.pushState(null, "", a.href);
        updateView();
    };
});

// 初期表示時の処理
updateView();

// ブラウザバック時の処理
window.addEventListener("popstate", () => {
    updateView();
});