import axios, { AxiosResponse } from 'axios';
import { Handler } from 'aws-lambda';

import { SensorPayload, WeatherMetricResponse, weatherParamEnum } from './types';


export const getSensorData = async (inputData: SensorPayload) =>  {
    //console.info(inputData['sensorMetric']);
    const argToPost = inputData['sensorMetric'];
    if (Object.values(weatherParamEnum).includes(argToPost)) {
        //console.log("True")
        try {
            const { data }: AxiosResponse<WeatherMetricResponse> = await axios
                .get(`https://a72e-73-182-155-254.ngrok.io/pi/${argToPost}`);
            const responseArg = argToPost;
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
    const inputPayload = event.data;
    try {
        const response = await getSensorData(inputPayload);
        //console.info(response);
        return {
            body: JSON.stringify(response),
            isBase64Encoded: false
         
        }
    } catch (err) {
        console.error(err);
    }   

}

