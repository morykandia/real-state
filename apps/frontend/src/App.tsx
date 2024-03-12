import { Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";
import Profile from "./pages/HomePage";
import RequireAuth from "./utils/RequireAuth";
import HomePage from "./pages/HomePage";
import AuthProvider from "./context/AuthContext";
import Category from "./pages/Category";
import Products from "./pages/Products";
import NavBar from "./components/NavBar";
import imagePath from "./assets/account.jpg";


function App()
 {
  let items = ["Products", "Categories", "Register", "Login"];
    return (
      <div className="App">
            <AuthProvider>
                <Routes>
                  <Route element={<RequireAuth/>}>
                    <Route path="/profile" element={<HomePage />} />
                  </Route>
                  <Route path="/categories" element={<Category/>}/>
                  <Route path="/products" element={<Products/>}/>
                  <Route path="/login" element={<LoginPage/>} />
                  <Route path="/register" element={<SignupPage/>} />
                  <Route path="/profile" element={<Profile />} />
                </Routes>
            
            </AuthProvider>
            <NavBar brandName="" imageSrcPath={imagePath} navItems={items} />
            
        </div>
    )
}

export default App;





