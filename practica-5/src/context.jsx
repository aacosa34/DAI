import React, { useContext, useEffect, useState } from 'react'

const AppContext = React.createContext()

const AppProvider = ({ children }) => {
  const [recipes, setRecipes] = useState([])

  // eslint-disable-next-line no-unused-vars
  const fetchRecipes = async () => {
    try {
      const response = await fetch('localhost:3000/api/recipes')
      const data = await response.json()
      setRecipes(data)
    } catch (error) {
      console.log(error)
    }

    useEffect(() => {
      fetchRecipes()
    }, [])
    return <AppContext.Provider value={{ recipes }}>
    {children}
  </AppContext.Provider>
  }
}

export const useGlobalContext = () => {
  return useContext(AppContext)
}

export { AppProvider, AppContext }
