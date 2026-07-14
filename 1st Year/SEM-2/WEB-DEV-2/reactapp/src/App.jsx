import React, { useState } from 'react';
import './App.css';
import Menu from './component/Menu';
import Article from './component/Article';
import Homepage from './component/Homepage';
import Contact from './component/Contact';
import Profile from './component/Profile';
import Search from './component/Search';
import { Route, Routes } from 'react-router-dom';

function App() {
  const [data] = useState('Sample data');

  return (
    <>
      <Routes>
        <Route path="/article" element={<Article data={data} />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/search" element={<Search />} />
        <Route
          path="/"
          element={
            <>
              <Homepage />
              <Menu />
            </>
          }
        />
        <Route path="/profile/:username" element={<Profile />} />
      </Routes>
    </>
  );
}

export default App;