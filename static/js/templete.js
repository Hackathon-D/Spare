//textareaを定義
const chatarea = document.getElementById('message');
//感謝buttonのidを指定
const thank = document.getElementById('templete1');
//怒りbuttonのidを指定
const angry = document.getElementById('templete2');

//buttonを押すとtextareaに代入
thank.addEventListener('click', () => {
    chatarea.value = 'お世話になっております、よろしくお願いいたします。';
    modal.style.display = 'none';
}
)

//buttonを押すとtextareaに代入
angry.addEventListener('click', () => {
    chatarea.value = '早く納品してください！';
    modal.style.display = 'none';
}
)

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