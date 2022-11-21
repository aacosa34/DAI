import TableBody from './TableBody'

const Table = () => {
  return (
    <div className='flex flex-col items-center justify-center overflow-x-auto relative'>
      <table className="flex items-center justify-center h-screen w-1/2">
        <thead className="text-xs text-center text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 rounded-lg dark:text-gray-400">
          <tr>
            <th scope="col" className="py-3 px-6">
                N
            </th>
            <th scope="col" className="py-3 px-6">
                Name
            </th>
            <th scope="col" className="py-3 px-6">
                Actions
            </th>
          </tr>
        </thead>
        <TableBody />
      </table>
    </div>
  )
}

export default Table
