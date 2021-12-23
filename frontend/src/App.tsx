import "bootstrap/dist/css/bootstrap.min.css";
import {Navigate, Route, Routes} from "react-router-dom";
import SiteNavbar from "./components/SiteNavbar";
import FileCreate from "./routes/Files/FileCreate";
import {Container, Row} from "react-bootstrap";
import Home from "./routes/Home";
import Login from "./routes/Login";
import Register from "./routes/Register";
import Profile from "./routes/Profile";
import authService from "./services/auth.service";
import FileIndex from "./routes/Files/FileIndex";
import "./styles/app.css";
import TagIndex from "./routes/Tags/TagIndex";
import FileShow from "./routes/Files/FileShow";

interface AuthChildren {
  children: JSX.Element; // Maybe there is a way to define this better and directly in RequireAuth
}

function RequireAuth({children}: AuthChildren) {
  const authenticated = authService.getCurrentUser() ?? undefined;

  return authenticated ? children : <Navigate to='/login' replace/>;
}

function App() {
  return (
    <>
      <SiteNavbar
        url={window.location.href.substr(window.location.href.lastIndexOf("/"))}
      />
      <Container>
        <Row>
          <Routes>
            <Route path='/' element={<Home/>}/>
            <Route path='/login' element={<Login/>}/>
            <Route path='/register' element={<Register/>}/>
            <Route
              path='/upload'
              element={
                <RequireAuth>
                  <FileCreate/>
                </RequireAuth>
              }
            />
            <Route
              path='/files'
              element={
                <RequireAuth>
                  <FileIndex/>
                </RequireAuth>
              }
            />
            <Route
              path='/profile'
              element={
                <RequireAuth>
                  <Profile/>
                </RequireAuth>
              }
            />
            <Route
              path='/files/:id'
              element={
                <RequireAuth>
                  <FileShow/>
                </RequireAuth>
              }
            />
            <Route
              path='/tags'
              element={
                <RequireAuth>
                  <TagIndex/>
                </RequireAuth>
              }
            />
          </Routes>
        </Row>
      </Container>
    </>
  );
}

export default App;
