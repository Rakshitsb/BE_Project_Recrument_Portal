import { Route, Routes, BrowserRouter } from "react-router-dom";
import MainLayout from "../Layout/MainLayout";
import Homepage from "../Pages/Homepage/Homepage";
import Dashboard from "../Pages/Dashboard/Dashboard";
import Settings from "../Pages/Settings/Settings";
import PageNotFound from "../Pages/PageNotFound/PageNotFound";


export default function AppRoutes() {
  return (
    <BrowserRouter>
      
      <Routes>
        {/* All pages that share Navbar + Sidebar */}
        <Route element={<MainLayout />}>
          <Route path="/" element={<Homepage />} />
          <Route path="/dashboard" element={<Dashboard/>} />
          <Route path="/settings" element={<Settings />} />
        </Route>

        {/* Catch all unmatched routes */}
        <Route path="*" element={<PageNotFound />} />
      </Routes>
   
    </BrowserRouter>

  );
}
