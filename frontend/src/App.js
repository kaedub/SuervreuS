import React from 'react';
import './App.css';

const API_URL = 'http://localhost:5000';

function make_request(route, success, error, data={}, method='GET') {
  console.log(API_URL + route);
  console.log(method);
  fetch(API_URL + route, {method: method})
  .then(res => res.json())
  .then(success, error);  
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      clientId: '',
      showData: true,
      openCmdForm: false,
    };
  }

  msgSuccess = (result) => {
    this.setState({msg: result.data})
  }

  handleError = (error) => {
    this.setState({error});
  }

  handleSuccess = (result) => {
    this.setState({data: result.data})
  }

  openCommandForm = () => {
    this.setState({openCmdForm: true});
  }

  getClientById = () => {
    let route = `/client/${this.state.clientId}`
    make_request(route, this.handleSuccess, this.handleError)
  }

  updateClientIdInput = (evt) => {
    this.setState({
      clientId: evt.target.value
    });
  }

  componentDidMount(prevProps, prevState) {
    make_request('/', this.msgSuccess, this.handleError)
  }

  renderAddCommandBtn() {
    return (
      <button onClick={this.openCommandForm}>Add New Command</button>
    );
  }
  renderCommandForm() {
    return (
      <div>
        <p><strong>You can add commands for this client here</strong></p><br></br>

        <label>Command Name </label>
        <input/><br></br>

        <p><i>Add params for this client (optional)</i></p>
        <label>Parameter Name </label>
        <input ></input><br></br>

        <label>Parameter Type </label>
        <select>
          <option value="int">int</option>
          <option value="bigint">bigint</option>
          <option value="float">float</option>
          <option value="bool">bool</option>
          <option value="string">string</option>
        </select>
        <button>Add a parameter</button><br></br>
      </div>
    )
  }

  renderClient() {
    const cmdParams = Object.keys(this.state.data.commands).map((i) => {
      let value = this.state.data.commands[i];

      return (
        <p key={i}>{value.name.toUpperCase()} : {JSON.stringify(value.parameters)}</p>
      )
    });

    return (
      <div>{Object.keys(this.state.data).map((key, i) => {
        let value = this.state.data[key];

        if (key === 'commands') {
          value = cmdParams;
        }
        return (
          <p key={i}><strong>{key.toUpperCase()}</strong> : {value}</p>
        )
      })}</div>
    )
  }

  render() {
    let msg = this.state.msg;
    return (
      <div className="App">
        <strong>
          <p>{!this.state.error ? msg : 'Something went wrong loading the page...'}</p>
        </strong><br></br>
        <label>Enter a client ID you wish to view data for: </label>
        <input value={this.state.clientId} onChange={evt => this.updateClientIdInput(evt)}></input>
        <button onClick={this.getClientById}>Submit</button>

        {this.state.data && this.state.showData ? this.renderClient() : ''}
        {this.state.data ? this.renderCommandForm() : ''}
        {this.state.data ? this.renderAddCommandBtn() : ''}
      </div>
    );
  }
}

export default App;
