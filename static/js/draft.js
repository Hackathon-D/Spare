//textareaを定義
const chatarea_draft = document.getElementById('message');

//ボタンの定義
const buttons_draft = document.querySelectorAll('#draft1');

//ボタンのvalueを取得
buttons_draft.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.value;
        chatarea.value = value;
        modal.style.display = 'none';
    });
});

//modalの表示
const modal_draft = document.getElementById('demo-modal-draft');
const btn_draft = document.getElementById('open-modal-draft');
const close_draft = document.getElementsByClassName('close-draft')[0];

//clickするとmodalを開く処理
btn_draft.onclick = function() {
    modal_draft.style.display = 'block';
};

//Xで閉じる処理
close_draft.onclick = function() {
    modal_draft.style.display = 'none';
};

//modalの外をクリックしたら閉じる処理
window.onclick = function(event) {
    if(event.target == modal_draft) {
        modal_draft.style.display = 'none';
    }
};