import React from 'react';
import '../../App.css';
import {UserIDInput, ClientData, CommandForm, FlashMessage} from '../index';
import make_request from '../../api/APIcall';



export default class Landingpage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
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

  getClientById = (clientId) => {
    let route = `/client/${clientId}`
    make_request(route, this.handleSuccess, this.handleError)
  }

  updateClientIdInput = (evt) => {
    this.setState({
      clientId: evt.target.value
    });
  }

  handleMessage = (result) => {
    this.setState({cmdMsg: result.data});
  }

  addCommand = (obj) => {
    let route = `/client/${this.state.data.id}/command`;
    let data = {data: {...obj}};
    make_request(route, this.handleMessage, this.handleError, data , 'POST');
  }

  componentDidMount(prevProps, prevState) {
    make_request('/', this.msgSuccess, this.handleError)
  }

  render() {
    return (
      <div className="App">
        <strong>
          <p>SuervreuS: an IoT microservice</p>
        </strong><br></br>
        <label>Enter a client ID you wish to view data for: </label>
        <UserIDInput onSubmit={this.getClientById}/>
        {this.state.data && this.state.showData ? <ClientData data={this.state.data}/> : ''}
        <FlashMessage message={this.state.cmdMsg}/>
        {this.state.data ? <CommandForm addCommand={this.addCommand}/> : ''}
      </div>
    );
  }
}