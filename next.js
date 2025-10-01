// login
import { login, onAuth, api, isAuthenticated, getUser } from "./auth";

await login({ email: "you@domain.com", password: "secret" });

// react to changes
onAuth("change", ({ authenticated, user }) => {
  console.log("Auth state:", authenticated, user);
});

// call protected API
const res = await api.get("/api/reflections");

```
const data = await res.json();  
  
