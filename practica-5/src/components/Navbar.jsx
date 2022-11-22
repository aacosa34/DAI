import { FaCocktail } from 'react-icons/fa'
import { RiFontSize2 } from 'react-icons/ri'
import { ImFontSize } from 'react-icons/im'
import DarkModeButton from './DarkModeButton'

const Navbar = () => {
  return (
    <div>
      <input type="checkbox" name="hbr" id="hbr" className="hbr peer" hidden aria-hidden="true" />
      <nav className="fixed z-20 w-full bg-white/90 dark:bg-gray-900/80 backdrop-blur navbar shadow-2xl shadow-gray-600/5 border-b border-gray-100 dark:border-gray-800 peer-checked:navbar-active dark:shadow-none">
              <div className="xl:container m-auto px-6 md:px-12 lg:px-6">
                  <div className="flex flex-wrap items-center justify-between gap-6 md:py-3 md:gap-0 lg:py-5">
                      <div className="w-full items-center flex justify-between lg:w-auto">
                          <a className="font-bold text-5xl relative z-10 dark:text-white" href="#" aria-label="logo">
                            <FaCocktail />
                          </a>

                          <input className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-full focus:ring-sky-600 focus:border-sky-600 block w-full p-2.5 pl-4 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 ml-6' type="search" placeholder="Search..." name="" id="" />

                          <label htmlFor="hbr" className="peer-checked:hamburger block relative z-20 p-6 -mr-6 cursor-pointer lg:hidden">
                            <div aria-hidden="true" className="m-auto h-0.5 w-5 rounded bg-gray-900 dark:bg-gray-300 transition duration-300"></div>
                            <div aria-hidden="true" className="m-auto mt-2 h-0.5 w-5 rounded bg-gray-900 dark:bg-gray-300 transition duration-300"></div>
                          </label>
                      </div>
                      <div className="navmenu hidden w-full flex-wrap justify-end items-center mb-16 space-y-8 p-6 border border-gray-100 rounded-3xl shadow-2xl shadow-gray-300/20 bg-white dark:bg-gray-900 lg:space-y-0 lg:p-0 lg:m-0 lg:flex md:flex-nowrap lg:bg-transparent lg:w-7/12 lg:shadow-none dark:shadow-none dark:border-gray-900 lg:border-0">
                          <div className="w-full space-y-2 border-primary/10 dark:border-gray-600 flex flex-col -ml-1 sm:flex-row lg:space-y-0 md:w-max lg:border-l">
                            <DarkModeButton />
                            <span className='align-center mr-2 py-2 dark:text-white'>Font size: </span>
                            <button
                                id="plus-size"
                                className="py-2 px-4 font-medium text-blue-700 bg-white rounded-l-lg border border-gray-200 hover:bg-gray-100 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
                                <ImFontSize />
                            </button>
                            <button
                                id="minus-size"
                                className="py-2 px-4 font-bold text-blue-700 bg-white rounded-r-md border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-blue-500 dark:focus:text-white">
                                  <RiFontSize2 />
                            </button>
                          </div>
                      </div>
                  </div>
              </div>
          </nav>
      </div>
  )
}

export default Navbar
