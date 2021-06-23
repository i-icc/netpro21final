$(function() {
	// 県名が変更されたら発動
	$('select[name="pref"]').change(function() {
		// 選択されている県のクラス名を取得
		var prefName = $('select[name="pref"] option:selected').attr("class");
		console.log(prefName);
		// 都市名の要素数を取得
		var count = $('select[name="city"]').children().length;
		// 都市名の要素数分、for文で回す
		for (var i=0; i<count; i++) {
			var city = $('select[name="city"] option:eq(' + i + ')');
			if(city.attr("class") === prefName) {
				// 選択した県と同じクラス名だった場合
				city.show();
			}else {
				// 選択した県とクラス名が違った場合
				if(city.attr("class") === "msg") {
					// 「選択して下さい」という要素だった場合
						city.show();  //「選択して下さい」を表示させる
						city.prop('selected',true);  //「選択して下さい」を強制的に選択されている状態にする
				} else {
					// 「選択して下さい」という要素でなかった場合
					city.hide();
				}
			}
		}
	})
})