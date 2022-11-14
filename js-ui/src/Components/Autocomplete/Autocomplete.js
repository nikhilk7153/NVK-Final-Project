import { useEffect, useState } from "react";
import Select from "react-select";
import styled from "styled-components";
import axios from 'axios';

import useGoogle from "react-google-autocomplete/lib/usePlacesAutocompleteService";
import { usePrevious } from "../../shared/hooks/usePrev";

export const AutoComplete = (props) => {
  const { placePredictions, getPlacePredictions, isPlacePredictionsLoading } =
    useGoogle({
      apiKey: "AIzaSyDBlcm5umGwbO8xPO96CGUp-dQ8-Md1isg",
    });
  const [selectedValue, setSelectedValue] = useState("");
  const [options, setOptions] = useState(null);
  const placeDirectionsHasChanged =
    usePrevious(placePredictions) !== placePredictions;

  useEffect(() => {
    if (placeDirectionsHasChanged) {
      let optionValues = placePredictions.map((place) => {
        return {
          value: place.place_id,
          label: place.description,
        };
      });
      setOptions(optionValues);
    }
  }, [placeDirectionsHasChanged]);

  useEffect(() => {
    if (selectedValue !== "" && selectedValue) {
      axios.get('http://127.0.0.1:5000/api/keywords/' + selectedValue.value, {
        params: {}
      })
      .then(function (response) {
        props.onGetProsCons(response.data);
      })
      .catch(function (error){
        //console.log(error);
      })
    }
    else {
      props.onGetProsCons("");
    }
  }, [selectedValue]);

  const handleInputChange = (inputValue) => {
    getPlacePredictions({ input: inputValue });
  };

  return (
    <AutoCompleteContainer>
      <>
        <Select
          className="basic-single"
          classNamePrefix="select"
          isLoading={isPlacePredictionsLoading}
          isClearable={true}
          isSearchable={true}
          value={selectedValue}
          name="color"
          onChange={(selectedOption) => {
            setSelectedValue(selectedOption);
          }}
          onInputChange={(inputValue) => {
            handleInputChange(inputValue);
          }}
          options={options}
        />
      </>
    </AutoCompleteContainer>
  );
};

const AutoCompleteContainer = styled.div`
  width: 20rem;
  margin-left: calc(50% - 10rem);
  margin-top: 2rem;
`;
