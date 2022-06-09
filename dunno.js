url =
  "https://wr4a6p937i.execute-api.ap-northeast-2.amazonaws.com/dev/languages?keyword=";
query_parameter = "java";
async function request() {
  const response = await fetch(url + query_parameter, {
    method: "GET",
  });
  const data = await response.json();
  console.log(data);
}
request();
