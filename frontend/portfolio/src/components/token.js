import  {useState, UseEffect, useEffect} from 'react';
import Cookies from 'js-cookie';
function Login() {
    const FetchSession = async () => {
        let token = prompt("You need a token to see this page")
        let url = "localhost/token?token=" + token;
        let response = await fetch(url);
        
        return;
    }
    useEffect(() => {
        const GetSession = () => {
            return Cookies.get("session")
        }

        const Session = GetSession();
        if (typeof Session === 'undefined') {
            const fetchsession = FetchSession();
            return;
        } 
        
    })
}
export default Login;