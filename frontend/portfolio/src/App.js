import logo from './logo.svg';
import './App.css';
import Navbar from './components/navbar.js'
import Login from './components/token.js'
function App() {
  return (
    <div className="background">
      <Navbar/>
      <Login />
    </div>
  );

}


export default App;
