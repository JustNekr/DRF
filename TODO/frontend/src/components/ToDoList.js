import React from 'react'
import {Link, useParams} from 'react-router-dom'

const Todo1Item = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.text}</td>
            <td>{item.user}</td>
        </tr>
    )
}


const TodoList = ({items}) => {
    return (
        <div>
            <tr>
                <th>ID</th>
                <th>Text</th>
                <th>AUTHOR</th>
            </tr>
            {items.map((item) => <Todo1Item item={item} />)}
        </div>
    )
}

export default TodoList