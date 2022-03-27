import React from 'react'
import {
  NavLink,
  Link
} from 'react-router-dom'

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <Link className="navbar-brand m-4" to="/">Home</Link>
      <button className="navbar-toggler " type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item active">
            <NavLink 
              activeClassName="active"
              className="nav-link"
              to="/movies"
            >
              Movies
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink
              activeClassName="active"
              className="nav-link"
              to="/users"
            >
              Users
            </NavLink>
          </li>
        </ul>
      </div>
    </nav>
  )
}

export default Navbar