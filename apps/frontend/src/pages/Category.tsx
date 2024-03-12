import {useState,  useEffect } from "react";

type Category = {
  id: number;
  name: string;
  slug: string;
};

export default function Category(){

    const [data, setData] = useState<Category[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
   
  
    useEffect(() => {
      fetch(`http://0.0.0.0:8000/monsite-api/categories/`)
        .then((response) => {
          if (!response.ok) {
            throw new Error(
              `This is an HTTP error: The status is ${response.status}`
            );
          }
          return response.json();
        })
        .then((actualData) => {
          setData(actualData);
          setError(null);
        })
        .catch((err) => {
          setError(err.message);
         // setData(null);
        })
        .finally(() => {
          setLoading(false);
        });
    }, []);
  
    return (
      <div className="App">
        <h1>Category</h1>
        {loading && <div>A moment please...</div>}
        {error && (
          <div>{`There is a problem fetching the post data - ${error}`}</div>
        )}
        <ul>
          {data &&
            data.map(({ id, name}) => (
              <li key={id}>
                <h3>{name}</h3>
              </li>
            ))}
        </ul>
      </div>
    );
}