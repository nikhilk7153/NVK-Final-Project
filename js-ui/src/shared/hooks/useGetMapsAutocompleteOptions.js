import React, { useState, useEffect } from "react";

export const useGetMapsAutocompleteOptions = (initialOption) => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [value, setValue] = useState(initialOption);

  const inputChange = (inputValue) => {
    setValue(inputValue);
  };

  useEffect(() => {
    (async function () {
      try {
        setLoading(true);
        const response = await fetch(
          `https://maps.googleapis.com/maps/api/place/autocomplete/json?input=deloitte&key=AIzaSyDBlcm5umGwbO8xPO96CGUp-dQ8-Md1isg
          `,
          { mode: "no-cors" }
        );
        setData(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    })();
  }, [value]);

  return { data, error, loading, inputChange };
};
