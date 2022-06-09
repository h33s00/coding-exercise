function reverse(s) {
  if (s.length === 0) return s;
  return s.slice(-1) + reverse(s.slice(0, -1));
}

// reverse('awesome') // 'emosewa'
// reverse('rithmschool') // 'loohcsmhtir'

s = "awesome";
s = "rithmschool";
// console.log(s.slice(0, -1));

console.log(reverse(s));
