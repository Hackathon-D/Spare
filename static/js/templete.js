//textareaを定義
const chatarea = document.getElementById('message');

//ボタンの定義
const buttons = document.querySelectorAll('#templete1');

//ボタンのvalueを取得
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.value;
        chatarea.value = value;
        modal.style.display = 'none';
    });
});

//modalの表示
const modal = document.getElementById('demo-modal');
const btn = document.getElementById('open-modal');
const close = document.getElementsByClassName('close')[0];

//clickするとmodalを開く処理
btn.onclick = function() {
    modal.style.display = 'block';
};

//Xで閉じる処理
close.onclick = function() {
    modal.style.display = 'none';
};

//modalの外をクリックしたら閉じる処理
window.onclick = function(event) {
    if(event.target == modal) {
        modal.style.display = 'none';
    }
};