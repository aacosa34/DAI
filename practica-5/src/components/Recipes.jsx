import { useGlobalContext } from '../context'
// import TableBody from './TableBody'

const Recipes = () => {
  const { recipes } = useGlobalContext()

  return (<div className="flex flex-col items-center justify-center mt-10 overflow-x-auto relative">
            <button id="add-recipe" type="button" className="text-white bg-gradient-to-br from-green-400 to-blue-600 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-green-200 dark:focus:ring-green-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center">Add recipe</button>
            <table className="w-1/2 text-sm text-left text-gray-500 dark:text-gray-400 my-10 shadow-lg">
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
    <tbody>
      { recipes.map((recipe) => {
        const { _id, name } = recipe
        return (
          <tr key={_id}>
            <td>{_id}</td>
            <td>{name}</td>
            <td>
              <button type="button">edit</button>
              <button type="button">delete</button>
            </td>
          </tr>
        )
      }) }
    </tbody>
  </table>
  </div>
  )
}
export default Recipes
