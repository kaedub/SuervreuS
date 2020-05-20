import React, {useState, Fragment} from 'react';

function Parameters(props){
  const [parameter, setParameter] = useState('');
  const [value, setValue] = useState('int');

  const handleClick = (event) => {
    event.preventDefault();
    props.addParameters({ ...props.params, [parameter]: value})
    setParameter('');
  };

    return (  
      <Fragment>
        <p><i>Add params for this client (optional)</i></p>
        <label>Parameter Name </label>
        <input name="parameter" onChange={e => setParameter(e.target.value)} value={parameter}></input><br></br>

       <label>Parameter Type </label>
        <select onChange={e => setValue(e.target.value)} name="value">
          <option value="int">int</option>
          <option value="bigint">bigint</option>
          <option value="float">float</option>
          <option value="bool">bool</option>
          <option value="string">string</option>
        </select>
       <button onClick={e => handleClick(e)}> Add a parameter</button><br></br>
      </Fragment>    

    )

}
export default Parameters;