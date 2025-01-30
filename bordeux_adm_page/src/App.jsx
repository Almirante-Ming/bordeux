import axios from 'axios';
import { useState, useEffect } from 'react';


function App() {
  const [body, setBody] = useState('')

  useEffect(() => {
    axios.get('http://localhost:7777/')
    .then((res) => {
      const data = res.data;
      setBody(data['message']);
    })
    .catch((err) => {console.log(err)})
  }, []);


  return (
    <div>
      {body}
    </div>
  );
}

export default App;
