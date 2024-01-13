import React, {useState, useEffect} from 'react'
import api from './api/api'
import 'bootstrap/dist/css/bootstrap.css'
import {Routes, Route, useNavigate} from 'react-router-dom';
import AdminPage from './Pages/Admin';
import HomePage from './Pages/Home';
import Trainee from './Pages/Trainee'

const App = () => {

 

  const [accounts, setAccounts] = useState([]);
  const [formData, setFormData] = useState({
    user_name: '',
    password: ''
  });

const fetchAccounts = async () => {
  const response = await api.get('/accounts/')
  setAccounts(response.data)
};

useEffect(() => {
  fetchAccounts();
},[]);

  const handleInputChange = (event) => {
    const value = event.target.type === 'checkbox'? event.target.checked: event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  };

  const handleFormatSumbit = async (event) => {
    event.preventDefault();
    await api.post('/accounts/',formData);
    fetchAccounts();
    setFormData({
      user_name: '',
      password: ''
    });
  };


  return(
    <div>
      <Routes>
        <Route path="/" exact element={<HomePage/>} />
        <Route path="/trainee" element={<Trainee/>} />
        <Route path="/admin" element={<AdminPage/>} />
      </Routes>
     
     
      {/* <Trainee /> */}
    </div>
  )
}

export default App;
