import "./Navbar.css";
import { FaUserCircle } from "react-icons/fa";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <h2>My App</h2>
      </div>
      <div className="navbar-right">
        <FaUserCircle className="profile-icon" />
      </div>
    </nav>
  );
}
