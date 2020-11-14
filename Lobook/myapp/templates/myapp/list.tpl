<!DOCTYPE HTML>
<html lang="ja">
<head></head>
<body>
<h2>会員一覧</h2>
%for d in data:
<p>{{d["name"]}}, {{d["gender"]}}, {{d["university"]}}, {{d["grade"]}}, {{d["phone"]}}</p>
%end
<p><a href="/">新規登録</a></p>
</body>
</html>