import {useState,  useEffect } from "react";

type Products = {
  id: number;
  title: string;
  published: boolean;
  date: string;

};
export default function Products(){

  const [data, setData] = useState<Products[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
 

  useEffect(() => {
    fetch(`http://0.0.0.0:8000/monsite-api/articles/`)
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
      <h1>API Products</h1>
      {loading && <div>A moment please...</div>}
      {error && (
        <div>{`There is a problem fetching the post data - ${error}`}</div>
      )}
      <ul>
        {data &&
          data.map(({ id, title, published, date }) => (
            <li key={id}>
              <h3>{title }</h3>
              <h3>{published }</h3>
              <h3>{date }</h3>
            </li>
          ))}
      </ul>
    </div>
  );

}