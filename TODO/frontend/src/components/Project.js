import React from 'react'
import {Link} from "react-router-dom";


const ProjectItem = ({project}) => {
   return (
       <tr>
           <td>
               <Link to={`${project.id}`}>{project.name}</Link>
           </td>
           <td>
               {project.url}
           </td>
           <td>
               {project.users.map((user) => <tr>{user} </tr>)}
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