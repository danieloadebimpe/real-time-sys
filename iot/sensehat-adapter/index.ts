import axios, { AxiosResponse } from 'axios';
import { Handler } from 'aws-lambda';

import { SensorPayload, WeatherMetricResponse, weatherParamEnum } from './types';


export const getSensorData = async (inputData: SensorPayload) =>  {
    // no data field when invoking locally 
    //console.info(inputData['sensorMetric']);
    //const argToPost = inputData['sensorMetric'];
    console.info(inputData.data['sensorMetric']);
    const argToPost = inputData.data['sensorMetric'];
    if (Object.values(weatherParamEnum).includes(argToPost)) {
        //console.log("True")
        try {
            const { data }: AxiosResponse<WeatherMetricResponse> = await axios
                // will need to change as you start new ngrok instances (random)
                // string is generated each time
                .get(`https://2049-73-182-155-254.ngrok.io/pi/${argToPost}`);
            const responseArg = argToPost;
            //console.info(data);
            if (responseArg === 'temperature') {
                //console.info(data[weatherParamEnum.TEMPERATURE])
                return data[weatherParamEnum.TEMPERATURE]

            } else if (responseArg === 'humditity') {
                //console.info(data[weatherParamEnum.HUMIDITY]);
                return data[weatherParamEnum.HUMIDITY]
        
            } else if(responseArg === 'pressure') {
                //console.info(data[weatherParamEnum.PRESSURE]);
                return data[weatherParamEnum.PRESSURE];
            }
        } catch (err) {
            console.error(err)
            return {}
        }
    
    } else {
        return ("incorrect Sensor Reading Input");
    }

}

export const main: Handler = async (event, context, callback) => {
    const inputPayload = JSON.parse(event.body);
    // cannot use json.parse() when invoking lambda locally
    //const inputPayload = event.data;
    console.info(inputPayload);
    try {
        const response = await getSensorData(inputPayload);
        //console.info(response);
        return {
            weatherMetric: response,
        }
    } catch (err) {
        console.error(err);
    }   

}

