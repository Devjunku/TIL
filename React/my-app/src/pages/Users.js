import React, { useEffect, useState } from 'react'
import axios from 'axios'
import UserList from './UsersComponents/UsersList'
import Spinner from './UsersComponents/Spinner'
const Users = () => {

  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    axios.get("https://jsonplaceholder.typicode.com/users")
    .then(response => {
      setUsers(response.data)
      setLoading(false)
    })
    .catch(error => {
      console.log(error)
    })
  }, [])

  useEffect(() => {
    console.log(users)
  }, [users])

  return (
    <>
      <h1>Users</h1>
      {
        loading ? <Spinner/> :
        <UserList
          users={users}
        />
      }
    </>
  )
}

export default Users