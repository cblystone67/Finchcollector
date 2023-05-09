import './App.css';
import { useState } from 'react';
import {Routes, Route} from 'react-router-dom';
import MovieListPage from '../../pages/MoviesListPage/MoviesListPage';
import LoginPage from '../../pages/LoginPage/LoginPage';
import ActorListPage from '../../pages/ActorListPage/ActorListPage';
import NavBar from '../../components/NavBar/NavBar';
function App() {
  const [user, setUser] = useState(null);
  return (
    <main className="App">
      {user ? (
        <>
        <NavBar />
      <Routes>
        <Route path="/ActorListPage" element={<ActorListPage />}/>
        <Route path="/MoviesListPage" element={<MovieListPage />}/>
      </Routes>
      </>
      ):(
      <LoginPage/>
      )}
    </main>
  );
}

export default App;
