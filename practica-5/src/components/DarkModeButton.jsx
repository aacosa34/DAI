import { useState, useEffect } from 'react'
import { CiDark, CiSun } from 'react-icons/ci'

const DarkModeButton = () => {
  const [darkMode, setDarkMode] = useState(false)

  useEffect(() => {
    const storedPreference = localStorage.getItem('darkModePreference')
    if (storedPreference) {
      setDarkMode(JSON.parse(storedPreference))
    } else {
      const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches
      setDarkMode(prefersDarkMode)
    }
  }, [])

  useEffect(() => {
    if (darkMode) {
      localStorage.setItem('darkModePreference', 'true')
      document.documentElement.classList.add('dark')
    } else {
      localStorage.setItem('darkModePreference', 'false')
      document.documentElement.classList.remove('dark')
    }
  }, [darkMode])

  return (
    <button id="theme-toggle" type="button" onClick={() => setDarkMode(!darkMode)}
        className="mx-4 text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-black text-xl rounded-full px-5 py-2.5 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700">
        {localStorage.getItem('darkMode') ? <CiSun /> : <CiDark />}
    </button>
  )
}

export default DarkModeButton
