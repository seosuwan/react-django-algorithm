import React from "react";
import {Link} from 'react-router-dom';

const Navi = () => (
    <div>
        <ul>
            <li><Link to='./Home'>Home</Link></li>
            <li><Link to='./UserAdd'>userAdd</Link></li>
            <li><Link to='./UserDetail'>userDetail</Link></li>
            <li><Link to='./UserList'>userList</Link></li>
            <li><Link to='./UserLogin'>userLogin</Link></li>
            <li><Link to='./UserModify'>userModify</Link></li>
            <li><Link to='./UserRemove'>userRemove</Link></li>
        </ul>
        </div>
)

export default Navi
