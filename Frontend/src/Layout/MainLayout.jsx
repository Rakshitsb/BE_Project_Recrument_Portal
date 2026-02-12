import React from 'react'
import './MainLayout.css'
import Navbar from '../Components/Navbar/Navbar'
import Sidebar from '../Components/SideBar/SideBar'
import { Outlet } from 'react-router-dom'

const MainLayout = () => {
  return (
       <div className="layout">
      <Navbar/>
      <div className="main-content">
        <Sidebar/>
        <div className="page-container">
          <Outlet/>
        </div>
      </div>
    </div>
  )
}

export default MainLayout