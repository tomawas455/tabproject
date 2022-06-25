import logo from "./logo.svg";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./login";
import Register from "./register";
import CreateCourseForWorker from "./createCourseForWorker";
import Protected from "./Protected";
import CourseList from "./courseList";
import UpdateProduct from "./UpdateProduct";
import GetUsers from "./GetUsers";
import TrainingList from "./trainingList";
import CreateTraining from "./createTraining";


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route exact path="/login" element={<Login />} />
          <Route exact path="/register" element={<Register />} />
          <Route exact path="/" element={<CourseList />} />
          <Route
            exact
            path="/createCourseForWorker"
            element={<Protected Cmp={CreateCourseForWorker} />}
          />
          <Route
              exact
              path="/createTraining/:id"
              element={<Protected Cmp={CreateTraining} />}
          />
          <Route exact path="/" element={<Protected Cmp={CourseList} />} />
          <Route
            exact
            path="/trainingList"
            element={<Protected Cmp={TrainingList} />}
          />
          <Route
            exact
            path="updateProduct/:id"
            element={<Protected Cmp={UpdateProduct} />}
          />
          <Route
            exact
            path="/GetUsers"
            element={<Protected Cmp={GetUsers} />}
          />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
