import React, { useContext, useState } from "react";
import axios from "axios";
import { AuthContext } from "../context/AuthContext"
import { jwtDecode } from "jwt-decode";
import { useNavigate } from "react-router-dom";
import "../styles/LoginPage.css"

const LoginPage: React.FC = () => {

  const [email, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const { setAuthTokens, setLoading, setUser } = useContext(AuthContext);
  
  let navigate = useNavigate();

    const handleLogin = (e: React.FormEvent) => {
          e.preventDefault();
          axios.post("http://0.0.0.0:8000/monsite-api/users/login/", {
               email, password })
            .then ((response) => {
              console.log(response.data)
              setAuthTokens(response.data);
              localStorage.setItem("authTokens", JSON.stringify(response.data));setUser(jwtDecode(response.data.access));
              setLoading(true);
              navigate("/profile");
            })
            
            .catch((error) => {
              console.log(error.message);
            }
        )
    }


   return (
       <div className="main">
         <form>
            <input type="text"  value={email} placeholder="Email" onChange={(e) => setUsername(e.target.value)} />
            <input type="password" value={password} placeholder="Password"  onChange={(e) => setPassword(e.target.value)} />
            <button type="submit" onClick={handleLogin}> Submit</button>
        </form>
        </div>
    )
};

export default LoginPage;

