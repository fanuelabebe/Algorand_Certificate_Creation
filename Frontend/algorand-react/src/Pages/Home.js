import React from "react";
import Table from '../Components/Table'
import Trainee from './Trainee'
import {Routes, Route, useNavigate} from 'react-router-dom';
const Home = () => {
    const navigate = useNavigate();

    const navigateToContacts = () => {
      //  navigate to /Trainee
      console.log('clicked')
      navigate('/trainee', {replace: true});
    };
    return (
        <div>
        <Routes>
          <Route path="/trainee" element={<Trainee />} />
        </Routes>
            <nav className= 'navbar navbar-dark bg-primary'>
                <div className='container-fluid'>
                    <a className='navbar-brand' href='#'>
                        Accounts
                    </a>
                </div>
            </nav>
        <Table onClick={navigateToContacts} />
        </div>
    )
}

export default Home