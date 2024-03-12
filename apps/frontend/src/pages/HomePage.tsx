import React, {useState, useContext, useEffect} from "react";
import { AuthContext } from "../context/AuthContext";
import axios from "axios";

interface userinfoInterface {
  id: number;
  first_name: string;
  username: string;
  email: string;
 
}

const HomePage: React.FC = () => {
  const { authTokens, setLoading } = useContext(AuthContext);
  const { callLogout } = useContext(AuthContext);
  const [userInfos, setUserInfos] = useState<userinfoInterface>();

  useEffect(() => {
    axios.get<userinfoInterface>("http://0.0.0.0:8000/monsite-api/users/me", {
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + String(authTokens.access),
        },
      })
      .then((response) => {
        setUserInfos(response.data);
        setLoading(true);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div>
        <p>Name: <span>{userInfos?.first_name}</span></p>
        <p>Email: <span>{userInfos?.email}</span></p>
        <p>Username: <span>{userInfos?.username}</span></p>
         <button onClick={callLogout}>Log out</button>
    </div>
  );
};

export default HomePage;