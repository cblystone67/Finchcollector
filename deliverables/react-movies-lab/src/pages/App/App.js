import './App.css';
import { useState } from 'react';
import {Routes, Route} from 'react-router-dom';
import MovieListPage from '../../pages/MoviesListPage/MoviesListPage';
import LoginPage from '../../pages/LoginPage/LoginPage';
import ActorListPage from '../../pages/ActorListPage/ActorListPage';
import MovieDetailPage from '../MovieDetailPage/MovieDetailPage';
import NavBar from '../../components/NavBar/NavBar';
import { movies } from '../../components/data';
function App() {
  const [user, setUser] = useState(null);

  return (
    <main className="App">
      {user ? (
        <>
        <NavBar user={user}/>
      <Routes>
        <Route path="/" element={<MovieListPage movies={movies} />}/>
        <Route path="/movies/:movieName" element={<MovieDetailPage movies={movies}/>}/>
        <Route path="/actors" element={<ActorListPage />}/>
      </Routes>
      </>
      ):(
        
          <LoginPage setUser={setUser}/>
      )}
    </main>
  );
}

export default App;
