var settings = {
  url: "http://localhost:8081/api/refresh-tokens",
  method: "POST",
  timeout: 0,
  headers: {
    Authorization: "YELLOWFIN ts=1636486721017, nonce=random",
    "Content-Type": "application/json",
    Accept: "application/vnd.yellowfin.api-v1+json",
  },
  data: JSON.stringify({
    userName: "",
    password: "",
    clientOrgRef: "default_org",
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
