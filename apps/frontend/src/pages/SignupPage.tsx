import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const SignupPage: React.FC  = () => {
  const [username, setUsername] = useState<string>("");
  const [first_name, setFirst_name] = useState<string>("");
  const [last_name, setLast_name] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const navigateTo = useNavigate();

  const handleSignup = (e: React.FormEvent) => {
      e.preventDefault();

      axios.post("http://0.0.0.0:8000/monsite-api/users/register/", {
          first_name,
          last_name,
          username,
          email,
          password,
        })
        .then((response) => {
          console.log(response.data);
          navigateTo('/login')
        })
        .catch((error) => {
          console.log(error.message);
        })
}

    return (
        <div>
             <input type="text" value={first_name} placeholder="First Name" onChange={(e) => setFirst_name(e.target.value)} />
             <input type="text" value={last_name} placeholder="Last Name" onChange={(e) => setLast_name(e.target.value)} />
             <input type="text" value={username} placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
            <input type="email" value={email} placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
            <input type="password" value={password} placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
            <button type="submit" onClick={handleSignup}> Submit </button>
        </div>

    )
}

export default SignupPage;