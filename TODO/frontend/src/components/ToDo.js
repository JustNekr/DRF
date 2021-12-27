import React from 'react'


const ToDoItem = ({todo}) => {
   return (
       <tr>
           <td>
               {todo.text}
           </td>
           <td>
               {todo.url}
           </td>
           <td>
               {todo.users.map((user) => <tr>{user} </tr>)}
           </td>
       </tr>
   )
}


const ProjectList = ({projects}) => {
   return (
       <table>
           <th>
               Name
           </th>
           <th>
               url
           </th>
           <th>
               Users
           </th>
           {projects.map((project) => <ProjectItem project={project} />)}
       </table>
   )
}


export default ProjectList