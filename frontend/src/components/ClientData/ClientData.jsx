import React from 'react';

  function ClientData(props) {
    // const cmdParams = Object.keys(props.data.commands).map((i) => {
    //   let value = props.data.commands[i];

    //   return (
    //     <p key={i}>{value.name.toUpperCase()} : {JSON.stringify(value.parameters)}</p>
    //   )
    // });

    return (
      <div>{Object.keys(props.data).map((key, i) => {
        let value = props.data[key];

        // if (key === 'commands') {
        //   value = cmdParams;
        // }
        return (
          <p key={i}><strong>{key.toUpperCase()}</strong> : {value}</p>
        )
      })}</div>
    )
  }

  export default ClientData;