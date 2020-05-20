import React, {useState} from 'react';
import Parameter from '../Parameters/Parameters';

function CommandForm(props) {
  const [params, setParams] = useState('');
  const [name, setName] = useState('');

  const handleClick = (e) => {
    e.preventDefault();
    props.addCommand({params, name });
  }
  const showParams = () => {
    let paramData = [];
    for (let key in params) {
      paramData.push(<p>{key} : {params[key]}</p>);
    }
    paramData.unshift(<p><strong>Current parameters set for this command</strong></p>)
    return paramData;
  }
 
  return (
    <form>
      <p><strong>You can add commands for this client here</strong></p><br></br>

      <label>Command Name </label>
      <input 
        onChange={e => setName(e.target.value)} 
        value={name}
      /><br></br>
      <Parameter addParameters={setParams} params={params}/>
      {params ? showParams() : null}
      <button onClick={e => handleClick(e)}>Add New Command</button>
    </form>
  )
}

export default CommandForm;