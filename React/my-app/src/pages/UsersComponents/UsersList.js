import React from "react"
import { Link } from 'react-router-dom'

const UsersList = ({ users }) => {
  console.log(users)
  return (
    <div>
      {users.map(user => {
        return (
          <div 
            className="card mb-4"
            key={user.id}>
            <div className="card-body p-3">
              <Link
                to={`/user/${user.id}`}
                >
                {user.name}
              </Link>
            </div>
          </div>
        )
      })}
    </div>
  )
}

export default UsersList