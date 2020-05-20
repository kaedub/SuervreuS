import React from 'react';

const LoginPage = () => {

    return (
        <form>
            <label for="user_id">User Id</label>
            <input type="text" name="user_id" value=""/>
            <label for="password">Password</label>
            <input type="text" name="password" value=""/>
            <button>Submit</button>
        </form>
    )
}

export default LoginPage;