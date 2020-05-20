import React, {Fragment} from 'react';
import './App.css';
import { LandingPage, LoginPage }from './components';

import './App.css'

class App extends React.Component {

  render() {
    return (
      <Fragment>
      <header id="Header">
        <p>SuervreuS: an IoT microservice </p>
      </header>
      <LoginPage/>
       {/* <Landingpage/> */}
      </Fragment>
    );
  }
}

export default App;
