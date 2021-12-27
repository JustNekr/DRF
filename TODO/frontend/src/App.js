import React from 'react';
import {BrowserRouter as Router, Routes, Route, Link, Navigate} from "react-router-dom";
import './App.css';
import axios from 'axios'

import UserList from './components/User.js'
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import ProjectList from './components/Project.js'
import NoMatch from "./components/NoMatch";



class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': []
       }
   }

   componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/users')
           .then(response => {
               const users = response.data.results
               this.setState(
                   {
                       'users': users
                   }
               )
           }).catch(error => console.log(error))

       axios.get('http://127.0.0.1:8000/api/projects')
           .then(response => {
               const projects = response.data.results
               this.setState(
                   {
                       'projects': projects
                   }
               )
           }).catch(error => console.log(error))
    }

   render () {
       return (
           <div>
               <Menu menu={'Menu'}/>
               <Router>
                    <nav>
                      <ul>
                        <li>
                          <Link to="/projects">Projects</Link>
                        </li>
                        <li>
                          <Link to="/">Users</Link>
                        </li>
                      </ul>
                    </nav>
                    <Routes>
                        <Route path="/" element={<UserList users={this.state.users} />} />
                        <Route path="/projects" element={<ProjectList projects={this.state.projects}/>} />
                        <Route path="*" element={<NoMatch />} />
                        <Route path="/users" element={<Navigate to ="/" />}/>
                    </Routes>
                </Router>

               <Footer text={'Footer'}/>
           </div>
       )
   }
}


export default App;