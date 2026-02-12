import { NavLink } from "react-router-dom";
import { FaHome, FaTachometerAlt, FaCog } from "react-icons/fa";
import "./Sidebar.css";

export default function Sidebar() {
  return (
    <div className="sidebar">
      <NavLink to="/" className="sidebar-link">
        <FaHome /> Home
      </NavLink>
      <NavLink to="/dashboard" className="sidebar-link">
        <FaTachometerAlt /> Dashboard
      </NavLink>
      <NavLink to="/settings" className="sidebar-link">
        <FaCog /> Settings
      </NavLink>
    </div>
  );
}
