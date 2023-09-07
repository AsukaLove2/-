// 基础环境 根据执行代码报错的地方来进行补充，如果没有具体的内容，就补空字典，否则就要将具体的内容放到console中找到对应的方法，在到此处补充。
function main1() {
  document = {}
  location = {
    reload: function () { }
  }

  var s = {},
    u, c, U, r, i, l = 0,
    a, e = eval,
    w = String.fromCharCode,
    sucuri_cloudproxy_js = '',
    S = 'az1TdHJpbmcuZnJvbUNoYXJDb2RlKDB4MzIpICsgICcnICsiMSIgKyAgJycgKycnKyJmc2VjIi5zdWJzdHIoMCwxKSArICI4c2VjIi5zdWJzdHIoMCwxKSArICIiICsiYnN1Ii5zbGljZSgwLDEpICsgIiIgK1N0cmluZy5mcm9tQ2hhckNvZGUoNTUpICsgICcnICsiYSIuc2xpY2UoMCwxKSArICJic2VjIi5zdWJzdHIoMCwxKSArICAnJyArIjAiICsgJ2cxNicuY2hhckF0KDIpKyc5JyArICAiYSIgKyAiM3N1Ii5zbGljZSgwLDEpICsgICcnICsnMnlEYScuc3Vic3RyKDMsIDEpICsgJycgKycnKydlJyArICAiMiIuc2xpY2UoMCwxKSArIFN0cmluZy5mcm9tQ2hhckNvZGUoNDgpICsgImJiIi5jaGFyQXQoMCkgKyAnWHFVNScuc3Vic3RyKDMsIDEpICsgJycgKyAKImEiICsgIiIgKyc3JyArICAiN3N1Ii5zbGljZSgwLDEpICsgICcnICsndTc4Jy5jaGFyQXQoMikrICcnICsgCidHb1Y2Jy5zdWJzdHIoMywgMSkgKyAnJyArJycrJzdmTDQnLnN1YnN0cigzLCAxKSArJzgnICsgICAnJyArImJ5Ii5jaGFyQXQoMCkgKyAiOSIgKyAiY3N1Y3VyIi5jaGFyQXQoMCkrIjlzdWN1ciIuY2hhckF0KDApKyAnJyArJycrJ2EnICsgICAnJyArIAoiOCIgKyAnJztkb2N1bWVudC5jb29raWU9J3N1Y3VycycuY2hhckF0KDUpICsgJ3N1Jy5jaGFyQXQoMSkrJ2MnKycnKyd1c3VjdScuY2hhckF0KDApICArJ3InLmNoYXJBdCgwKSsnaScuY2hhckF0KDApKydfc3VjdXInLmNoYXJBdCgwKSsgJ2NzdWN1cicuY2hhckF0KDApKyAnbHMnLmNoYXJBdCgwKSsnb3N1YycuY2hhckF0KDApKyAnc3VjdXJ1Jy5jaGFyQXQoNSkgKyAnc3VjdXJkJy5jaGFyQXQoNSkgKyAnc3VjdXJwJy5jaGFyQXQoNSkgKyAnc3VyJy5jaGFyQXQoMikrJ29zJy5jaGFyQXQoMCkrJ3gnKycnKyd5c3VjdScuY2hhckF0KDApICArJ18nKydzdXUnLmNoYXJBdCgyKSsndXMnLmNoYXJBdCgwKSsnc3VjdXJpaScuY2hhckF0KDYpKydzZCcuY2hhckF0KDEpKydfJysnYScrJ3N1Y3VyNCcuY2hhckF0KDUpICsgJzYnKycnKyc4JysnJysnYScuY2hhckF0KDApKydzdWEnLmNoYXJBdCgyKSsnYnMnLmNoYXJBdCgwKSsnNnN1YycuY2hhckF0KDApKyAnc3UzJy5jaGFyQXQoMikrIj0iICsgayArICc7cGF0aD0vO21heC1hZ2U9ODY0MDAnOyBsb2NhdGlvbi5yZWxvYWQoKTs=';
  L = S.length;
  U = 0;
  r = '';
  var A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
  for (u = 0; u < 64; u++) {
    s[A.charAt(u)] = u;
  }
  for (i = 0; i < L; i++) {
    c = s[S.charAt(i)];
    U = (U << 6) + c;
    l += 6;
    while (l >= 8) {
      ((a = (U >>> (l -= 8)) & 0xff) || (i < (L - 2))) && (r += w(a));
    }
  }
  e(r);

  return document.cookie
}