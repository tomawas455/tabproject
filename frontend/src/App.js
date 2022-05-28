import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Header from './Header';
import Login from './login';
import Register from './register';
//import CreateCourseForWorker from './createCourseForWorker';
import Protected from './Protected';

function App() {
  return (
    <div className="App">
        <BrowserRouter>
        <Routes>
             <Route exact path="/login" element={<Login />} />
             <Route exact path="/register" element={<Register />} />

        </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
