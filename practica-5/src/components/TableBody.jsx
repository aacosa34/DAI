const TableBody = () => {
  return (
    <tbody className="text-center dark:bg-gray-800" id="tbody" data-container>
        <template>
            <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                <td className="py-4 px-6" data-id></td>
                <td className="py-4 px-6">
                    <button data-modal-toggle="defaultModal" type="button" data-name>
                    </button>
                </td>
                <td className="py-4 px-6">
                    <button
                        data-edit
                        className="relative inline-flex items-center justify-center p-0.5 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-green-400 to-blue-600 group-hover:from-green-400 group-hover:to-blue-600 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-green-200 dark:focus:ring-green-800"><span
                            className="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-800 rounded-md group-hover:bg-opacity-0">Edit</span></button>
                    <button
                        data-delete
                        className="relative inline-flex items-center justify-center p-0.5 overflow-hidden text-sm font-medium text-gray-900 rounded-lg group bg-gradient-to-br from-pink-500 to-orange-400 group-hover:from-pink-500 group-hover:to-orange-400 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-pink-200 dark:focus:ring-pink-800"><span
                            className="relative px-5 py-2.5 transition-all ease-in duration-75 bg-white dark:bg-gray-800 rounded-md group-hover:bg-opacity-0">Delete</span></button>
                    <div hidden data-mongo-id></div>
                </td>
            </tr>
        </template>
    </tbody>
  )
}

export default TableBody
