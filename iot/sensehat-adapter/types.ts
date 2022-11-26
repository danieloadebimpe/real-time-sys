

export enum weatherParamEnum {
    PRESSURE = 'pressure',
    HUMIDITY = 'humidity',
    TEMPERATURE = 'temperature'
}

type weatherParam = {
    weatherReading: string
}

export type WeatherMetricResponse = {
    weatherMetric: string
}

export type SensorPayload = {
    id: number,
    data: weatherParam

}


export type SensorReading = {
    sensorReading: string,
    physicalDetection: WeatherMetricResponse
}