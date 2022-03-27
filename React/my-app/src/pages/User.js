import React, { useEffect, useState } from 'react'
import axios from 'axios'
import Spinner from './UsersComponents/Spinner'
import {useParams} from 'react-router-dom'
const User = () => {

  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)
  const { id } = useParams()

  useEffect(() => {
    axios.get("https://jsonplaceholder.typicode.com/users/"+id)
    .then(response => {
      console.log(response)
      setUser(response.data)
      setLoading(false)
    })
    .catch(error => {
      console.log(error)
    })
  }, [])

  const userDetail = loading ? <Spinner /> : (
    <div>
      <div>{user.name}</div>
      <div>{user.email}</div>
      <div>{user.phone}</div>
    </div>
  )

  return (
    <>
      <h1>User Information</h1>
      {
        loading ? <Spinner/> :
        userDetail
      }
    </>
  )
}

export default User