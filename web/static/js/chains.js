// HTMLの読み込み直後に実行：
document.addEventListener('DOMContentLoaded', function() {

  // ▼とりあえずサブBOXを全て非表示にする（CSSで書けば早いが）
  var allSubBoxes = document.getElementsByClassName("subbox");
  for( var i=0 ; i<allSubBoxes.length ; i++) {
    allSubBoxes[i].style.display = 'none';
  }

  // ▼全てのプルダウンボックスごとに処理
  var mainBoxes = document.getElementsByClassName('pulldownset');
  for( var i=0 ; i<mainBoxes.length ; i++) {

    var mainSelect = mainBoxes[i].getElementsByClassName("mainselect");	// メインのプルダウンメニュー（※後でvalue属性値を参照するので、select要素である必要があります。）
    mainSelect[0].onchange = function () {
      // 同じ親要素に含まれている全サブBOXを消す
      var subBox = this.parentNode.getElementsByClassName("subbox");	// 同じ親要素に含まれる.subbox（※select要素に限らず、どんな要素でも構いません。）
      for( var j=0 ; j<subBox.length ; j++) {
        subBox[j].style.display = 'none';
      }

      // 指定されたサブBOXを表示する
      if( this.value ) {
        var targetSub = document.getElementById( this.value );	// 「メインのプルダウンメニューで選択されている項目のvalue属性値」と同じ文字列をid属性値に持つ要素を得る
        targetSub.style.display = 'inline';
      }
    }

  }

});