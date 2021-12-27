import React from 'react'
import { useParams } from 'react-router-dom'

const TodoItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.text}</td>
            <td>{item.user}</td>
        </tr>
    )
}


const ProjectTodoList = ({items}) => {
    let { id } = useParams();
    let filtered_items = items.filter((item) => item.project === parseInt(id));
    return (

        <table>
            <tr>
                <th>ID</th>
                <th>Text</th>
                <th>AUTHOR</th>
            </tr>
            {filtered_items.map((item) => <TodoItem item={item} />)}
        </table>
    )
}

export default ProjectTodoList


